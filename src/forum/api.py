from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from django.http import *
from django.core.urlresolvers import reverse
from .models import *
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

  return HttpResponse(json.dumps(list(queryset), indent=2))

urls = patterns('',
   url(r'^recent$', api_most_recent, name='forum.api.recent'),
)
