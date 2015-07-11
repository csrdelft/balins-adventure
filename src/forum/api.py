from django.views.decorators.http import condition
from django.utils.decorators import method_decorator
from django.conf import settings

from rest_framework import views, response, generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter

from .models import *
from .serializers import *
from base.utils import notification_client, deny_on_fail
from base.serializers import *

from datetime import datetime
import logging
import json
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

  def list(self, request):
    delen = ForumDeel.get_viewable_by(self.request.user)

    return Response(self.get_serializer(delen, many=True).data)

  def retrieve(self, request, pk):
    deel = self.get_object()

    # permission check
    deny_on_fail(request.user.has_perm('forum.view_forumdeel', deel))

    return Response(EntireForumDeelSerializer(deel).data)

class ForumDraadViewSet(
  mixins.CreateModelMixin,
  mixins.RetrieveModelMixin,
  viewsets.GenericViewSet):

  serializer_class = ForumDraadSerializer
  queryset = ForumDraad.objects\
    .prefetch_related("posts", "forum")

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

  def retrieve(self, request, pk):
    draad = self.get_object()

    # make sure the user can view the forum draad
    deny_on_fail(request.user.has_perm('forum.view_forumdeel', draad.forum))

    return Response(EntireForumDraadSerializer(draad).data)

  @detail_route(methods=['post'])
  def post(self, request, pk):
    """ Forum post in draad
        ---
        serializer: ForumPostSerializer
        parameters_strategy: replace
        parameters:
          - name: tekst
            required: true
            type: string
          - name: pk
            required: true
            paramType: path
    """
    draad = self.get_object()

    # make sure the user can post in the forum draad
    deny_on_fail(request.user.has_perm('forum.post_in_forumdeel', draad.forum))
    deny_on_fail(not draad.gesloten)

    request.data.update({
      'draad': draad.pk,
      'user': request.profiel.pk,
      'datum_tijd': datetime.now(),
      'laatst_gewijzigd': datetime.now(),
      'bewerkt_tekst': "",
      'auteur_ip': ""
    })

    # check if we can validly deserialize the json data
    serializer = ForumPostSerializer(data=request.data)
    if serializer.is_valid():
      # create the post
      post = serializer.save()

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
router.register('forum', ForumViewSet, base_name="forum")
router.register('forum/draad', ForumDraadViewSet, base_name="forumdraad")
urls = router.urls
