import os
import logging

from django.conf.urls import patterns, include, url
from django.shortcuts import render
from base.views import render_with_layout
from django.conf import settings

logger = logging.getLogger(__name__)

def embed(embed_path, title=""):
  def view_func(request, *args, **kwargs):
    return render(request, 'legacy.jade', {
      'embed_url' : os.path.join(settings.LEGACY_HOST, embed_path)
    })

  return view_func

urls = patterns('',
  url('groepen', embed('groepen/'), name="legacy.groepen"),
)
