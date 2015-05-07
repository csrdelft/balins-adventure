from django.conf.urls import patterns, include, url
from django.contrib import admin

import forum.views

urlpatterns = patterns('',
  url(r'^$', 'base.views.index', name='index'),
  url(r'^forum/', include(forum.views.urls)),

  url(r'^admin/', include(admin.site.urls)),
)
