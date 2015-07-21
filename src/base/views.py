from django.conf.urls import patterns, include, url
from django.shortcuts import render
import hijack.helpers as hijack
from .models import *

import logging
logger = logging.getLogger(__name__)

def index(request):
  return render(request, 'main.html')

def login(request):
  return render(request, 'login.html')

def su(request, uid):
  user = Profiel.objects.get(pk=uid)
  return hijack.login_user(request, user.user)

def end_su(request):
  return hijack.release_hijack(request)

urls = patterns('',
  url(r'^$', index, name='index'),
  url(r'^su/(.{4})/$', su, name='base.su'),
  url(r'^endsu/$', end_su, name='base.end_su'), )
