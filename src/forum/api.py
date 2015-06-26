from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from django.http import *
from django.core.urlresolvers import reverse
from .models import *
from .serializers import *
from base.utils import *
from base.http import *

from datetime import datetime
import logging
import json

logger = logging.getLogger(__name__)

def api_most_recent(request):
  n = int(request.GET.get('n', 10))
  # find the forumdelen that may be seen by the user
  delen = list(ForumDeel.get_viewable_by(request.user))
  queryset = ForumDraad.objects\
    .filter(forum__in=delen)\
    .order_by('-laatst_gewijzigd')[:n]\
    .values('titel')

  return json_response(list(queryset))

def api_forum_draad(request, draad_id):
  draad = ForumDraad.objects.prefetch_related('forum').get(pk=draad_id)

  # make sure the user can view the forum draad
  deny_on_fail(request.user.has_perm('forum.view_forumdeel', draad.forum))

  return json_response(ForumDraadSerializer().to_representation(draad))

urls = patterns('',
   url(r'^recent$', api_most_recent, name='forum.api.recent'),
   url(r'^(\d+)/$', api_forum_draad, name='forum.api.draad')
)
