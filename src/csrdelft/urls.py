from django.conf.urls import patterns, include, url
from django.contrib import admin

import base.views, base.api
import forum.views, forum.api
import maaltijden.views, maaltijden.api
import legacy.views

# apply the permission logics
import permission; permission.autodiscover()

api_urls = patterns('',
  url(r'^', include(base.api.urls)),
  url(r'forum/', include(forum.api.urls)),
)

urlpatterns = patterns('',
  # app views
  url(r'^', include(base.views.urls)),
  url(r'^forum/', include(forum.views.urls)),

  # app apis
  url(r'^api/v1/', include(api_urls)),

  url(r'^admin/', include(admin.site.urls)),
  url(r'', include(legacy.views.urls)),
)
