from django.views.decorators.http import condition
from django.utils.decorators import method_decorator
from django.conf import settings
from django.db.models import Prefetch

from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.routers import DefaultRouter

from .serializers import *
from base.utils import notification_client, deny_on_fail
from base.serializers import *
from base.api import StekPaginator, StekViewSet

from datetime import datetime
import logging

logger = logging.getLogger(__name__)
redis = notification_client()

def most_recent_forum_change(request):
  """ Cheap check for latest change at the forums.
  """
  # Don't take into account user permissions here: too expensive; query wisely
  return ForumDraad.objects.latest("laatst_gewijzigd").laatst_gewijzigd

def notify_subscribers(draad, post):
  """ Given a ForumDraad instance `draad`, notify all subscribers of `post`
  """
  # skip if redis is disabled
  if settings.NO_REDIS: return

  for profiel_id, auth_id in draad.subscribers.all().values_list('user__pk', 'user__user__pk'):
    # don't notify the poster
    if profiel_id == post.user.pk: continue

    # push the event into the user's notification channel on the redis cluster
    key = "notifications:" + str(auth_id)
    redis.publish(key, {
      'draad': ShortForumDraadSerializer(draad).data,
      'post': {
        'user': ShortProfielSerializer(post.user).data,
        'tekst': post.tekst
      }
    })

class ForumViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, StekViewSet):

  detail_serializer_class = DetailForumDeelSerializer
  list_serializer_class = ListForumDeelSerializer

  def get_queryset(self):
    return ForumDeel.objects.all()

  def list(self, request, *args, **kwargs):
    delen = ForumDeel.get_viewable_by(self.request.user)

    return Response(self.get_serializer(delen, many=True).data)

  def retrieve(self, request, *args, **kwargs):
    deel = self.get_object()

    # permission check
    deny_on_fail(request.user.has_perm('forum.view_forumdeel', deel))

    return Response(self.get_serializer(deel).data)

class ForumDraadViewSet(
  mixins.DestroyModelMixin,
  mixins.CreateModelMixin,
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  StekViewSet):

  detail_serializer_class = DetailForumDraadSerializer
  list_serializer_class = ListForumDraadSerializer

  queryset = ForumDraad.objects\
    .prefetch_related("forum", "posts")\
    .order_by("-laatste_post__laatst_gewijzigd")
  filter_fields = ('forum',)

  @method_decorator(condition(last_modified_func=most_recent_forum_change))
  @list_route(methods=['get'])
  def recent(self, request):
    """ Gets the n forum draadjes that changed most recently.
        It uses the most_recent_forum_change function to handle if-modified-since
        correctly.
    """
    n = int(request.GET.get('n', 10))

    # find the forumdelen that may be seen by the user
    delen = list(ForumDeel.get_viewable_by(request.user))
    queryset = ForumDraad.objects\
      .filter(forum__in=delen)\
      .order_by('-laatst_gewijzigd')[:n]

    return Response(self.get_serializer(queryset, many=True).data)

  def destroy(self, request, *args, **kwargs):
    post = self.get_object()

    # check delete permission
    deny_on_fail(request.user.has_perm('forum.delete_forumdraad', post))

    return super().destroy(request, *args, **kwargs)

  def create(self, request, *args, **kwargs):
    """ Create a new forum thread including the first post
        ---
        parameters:
          - name: tekst
            description: Text of the first post
            required: true
            type: string
    """
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    forum = serializer.validated_data['forum']

    # check that the user can create a thread in this forum
    deny_on_fail(request.user.has_perm('forum.post_in_forumdeel', forum))

    # validate the tekst field
    tekst = request.data.get('tekst', None)
    if tekst is None or len(tekst.strip()) < 15:
      raise ValidationError("Tekst moet minstens 15 tekens bevatten")

    # save the new thread...
    thread = serializer.save(user=request.profiel, datum_tijd=datetime.now())

    # create the first post
    post = ForumPost.objects.create(
      user=request.profiel,
      tekst=request.data.get('tekst', None),
      draad=thread
    )

    # close the loop
    thread.laatste_post = post
    thread.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def retrieve(self, request, *args, **kwargs):
    draad = self.get_object()

    # make sure the user can view the forum draad
    deny_on_fail(request.user.has_perm('forum.view_forumdeel', draad.forum))

    return Response(self.get_serializer(draad).data)

class ForumPostViewSet(
  mixins.DestroyModelMixin,
  mixins.CreateModelMixin,
  StekViewSet):

  serializer_class = ForumPostSerializer
  queryset = ForumPost.objects.all()

  def destroy(self, request, *args, **kwargs):
    post = self.get_object()

    # check delete permission
    deny_on_fail(request.user.has_perm('forum.delete_forumpost', post))

    return super().destroy(request, *args, **kwargs)

  def create(self, request, *args, **kwargs):
    # check if we can validly deserialize the json data
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      draad = serializer.validated_data['draad']

      # make sure the user can post in the forum draad
      deny_on_fail(request.user.has_perm('forum.post_in_forumdeel', draad.forum))
      deny_on_fail(not draad.gesloten)

      # create the post
      post = serializer.save(user=request.profiel, datum_tijd=datetime.now(), laatst_gewijzigd=datetime.now())

      # update the draad
      draad.laatste_post_id = post.pk
      draad.save()

      # subscribe to the draad
      ForumDraadVolgen.objects.get_or_create(draad=draad, user=request.profiel)

      # notify subscribers of this draad
      notify_subscribers(draad, post)

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

router = DefaultRouter()
router.register('forums', ForumViewSet, base_name="forum-part")
router.register('draadjes', ForumDraadViewSet, base_name="forum-thread")
router.register('posts', ForumPostViewSet, base_name="forum-post")
urls = router.urls
