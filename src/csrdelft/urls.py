from django.conf.urls import patterns, include, url
from django.contrib import admin

import base.views
import forum.views
import maaltijden.views, maaltijden.api
import legacy.views

# apply the permission logics
import permission; permission.autodiscover()

api_urls = []

urlpatterns = patterns('',
  url(r'^', include(base.views.urls)),
  url(r'^forum/', include(forum.views.urls)),

  url(r'^api/', include(api_urls)),

  url(r'^admin/', include(admin.site.urls)),
  url(r'', include(legacy.views.urls))
)
