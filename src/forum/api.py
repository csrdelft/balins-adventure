from django.contrib.auth.models import User
from django.views.decorators.http import condition
from django.utils.decorators import method_decorator
from django.http import *

from rest_framework import views, response, generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from base.utils import *
from base.http import *

from datetime import datetime
import logging
import json

logger = logging.getLogger(__name__)

def most_recent_forum_change(request):
  """ Cheap check for latest change at the forums.
  """
  # Don't take into account user permissions here: too expensive; query wisely
  return ForumDraad.objects.latest("laatst_gewijzigd").laatst_gewijzigd

class ForumDraadViewSet(viewsets.GenericViewSet):

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

    return Response(ShortForumDraadSerializer(queryset, many=True).data)

  @detail_route(methods=['get'])
  def get(self, request, pk):
    draad = self.get_object()

    # make sure the user can view the forum draad
    deny_on_fail(request.user.has_perm('forum.view_forumdeel', draad.forum))

    return Response(self.get_serializer(draad).data)

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

    serializer = ForumPostSerializer(data=request.data)
    if serializer.is_valid():
      inst = serializer.save()

      # update the draad
      draad.laatst_gewijzigd = request.data['laatst_gewijzigd']
      draad.laatste_wijziging_user_id = request.profiel.pk
      draad.laatste_post_id = inst.pk
      draad.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
