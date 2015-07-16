from django.views.decorators.http import condition
from django.utils.decorators import method_decorator
from django.conf import settings

from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.routers import DefaultRouter
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from base.utils import notification_client, deny_on_fail
from base.serializers import *
from base.api import StekPaginator

from datetime import datetime
import logging
import redis

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

class ForumViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

  serializer_class = ForumDeelSerializer

  def get_queryset(self):
    return ForumDeel.objects.all()

  def list(self, request, *args, **kwargs):
    delen = ForumDeel.get_viewable_by(self.request.user)

    return Response(self.get_serializer(delen, many=True).data)

  def retrieve(self, request, *args, **kwargs):
    deel = self.get_object()

    # permission check
    deny_on_fail(request.user.has_perm('forum.view_forumdeel', deel))

    return Response(EntireForumDeelSerializer(deel).data)

class ForumDraadViewSet(
  mixins.CreateModelMixin,
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  viewsets.GenericViewSet):

  serializer_class = ForumDraadSerializer
  queryset = ForumDraad.objects\
    .prefetch_related("posts", "forum")\
    .order_by("-datum_tijd")
  filter_fields = ('forum',)
  pagination_class = StekPaginator

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

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    forum = serializer.validated_data['forum']

    # check that the user can create a draadje in this forum
    deny_on_fail(request.user.has_perm('forum.post_in_forumdeel', forum))

    # save the forumdeel
    serializer.save(user=request.profiel, datum_tijd=datetime.now(), laatste_wijziging_user=request.profiel)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def retrieve(self, request, *args, **kwargs):
    draad = self.get_object()

    # make sure the user can view the forum draad
    deny_on_fail(request.user.has_perm('forum.view_forumdeel', draad.forum))

    # we cannot elegantly handle pagination by request parameters
    # of a related object in a serializer
    data = ForumDraadSerializer(draad).data
    posts_query = draad.posts.all().order_by("datum_tijd")
    data['posts'] = ForumPostSerializer(
      StekPaginator().paginate_queryset(posts_query, request),
      many=True
    ).data

    return Response(data)

class ForumPostViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

  serializer_class = ForumPostSerializer
  queryset = ForumPost.objects.all()

  def create(self, request, *args, **kwargs):
    # check if we can validly deserialize the json data
    serializer = ForumPostSerializer(data=request.data)
    if serializer.is_valid():
      draad = ForumDraad.objects.get(serializer.validated_data['draad_id'])

      # make sure the user can post in the forum draad
      deny_on_fail(request.user.has_perm('forum.post_in_forumdeel', draad.forum))
      deny_on_fail(not draad.gesloten)

      # create the post
      post = serializer.save(datum_tijd=datetime.now(), laatst_gewijzigd=datetime.now())

      # update the draad
      draad.laatst_gewijzigd = request.data['laatst_gewijzigd']
      draad.laatste_wijziging_user_id = request.profiel.pk
      draad.laatste_post_id = post.pk
      draad.save()

      # subscribe to the draad
      ForumDraadVolgen.objects.get_or_create(draad=draad, user=request.profiel)

      # notify subscribers of this draad
      notify_subscribers(draad, post)

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

router = DefaultRouter()
router.register('parts', ForumViewSet, base_name="forum-part")
router.register('threads', ForumDraadViewSet, base_name="forum-thread")
router.register('posts', ForumPostViewSet, base_name="forum-post")
urls = router.urls
