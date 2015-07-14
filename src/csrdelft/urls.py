from django.conf.urls import patterns, include, url
from django.contrib import admin

import base.views, base.api
import forum.views, forum.api
import mededelingen.api
import maaltijden.views, maaltijden.api
import legacy.views

from rest_framework.routers import DefaultRouter

from django.http import HttpResponse
import json

# apply the permission logics
import permission;

permission.autodiscover()

router = DefaultRouter()
router.register('maaltijden', maaltijden.api.MaaltijdViewSet, base_name="maaltijd")
router.register('mededelingen', mededelingen.api.MededelingenViewSet, base_name='mededeling')

api_urls = patterns('',
  url(r'^', include(base.api.urls)),
  # react tutorial data
  url(r'^data.json$', lambda r: HttpResponse(json.dumps([
    {"author": "Pete Hunt", "text": "This is one comment"},
    {"author": "Jordan Walke", "text": "This is *another* comment"}
  ]))),

  url(r'^', include(router.urls)),
  url(r'^forum/', include(forum.api.urls)),
  url(r'^docs/', include('rest_framework_swagger.urls')),
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
