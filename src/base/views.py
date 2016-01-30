from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.template.defaultfilters import escapejs
import hijack.helpers as hijack
from .models import *
from .serializers import ShortProfielSerializer

import json
import logging
logger = logging.getLogger(__name__)

def index(request):
  preloadData = dict()

  if request.user.is_authenticated():
    preloadData["user"] = ShortProfielSerializer(request.profiel).data

  return render(request, 'main.html', context={
    'preload_data': escapejs(json.dumps(preloadData))
  })

def su(request, uid):
  user = Profiel.objects.get(pk=uid)
  return hijack.login_user(request, user.user)

def end_su(request):
  return hijack.release_hijack(request)

urls = patterns('',
  url(r'^su/(.{4})/$', su, name='base.su'),
  url(r'^endsu/$', end_su, name='base.end_su'),
  url(r'^.*$', index, name='index')
)
