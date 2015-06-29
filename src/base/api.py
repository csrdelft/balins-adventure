from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from django.views.decorators.http import condition
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

def api_profiel(request, uid):
  prof = Profiel.objects.get(pk=uid)

  return json_response(ProfielSerializer().to_representation(prof))

urls = patterns('',
  url(r'^profiel/(\d+)$', api_profiel, name='base.api.profiel'),
)
