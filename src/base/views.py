from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.template import loader, RequestContext
from .models import *

import logging
logger = logging.getLogger(__name__)

DEFAULT_TITLE = "Civitas Studiosorum Reformatorum"


def render_with_layout(request, template, ctx={}, title=DEFAULT_TITLE):
  """ Renders content in the csr layout
  """
  t = loader.get_template(template)
  r = t.render(ctx, request)

  return render(request, 'index.jade', {"content": r, "title": title})

def index(request):
  return render_with_layout(request, 'main.jade')

def make_groep_view(category_model, name):
  def groep_view(request):
    groepen = dict(list(map(lambda g: (g.pk, (g, [])), category_model.objects.all())))
    leden   = category_model.lidmodel.objects.filter(user__status='S_LID')

    # sort the members
    for lid in leden:
      # if somehow the group doesn't exist, skip the member
      try:
        groepen.get(lid.groep_id)[1].append(lid)
      except Exception as e:
        logger.error(str(e))
        pass

    logger.error(groepen)
    return render_with_layout(request, 'groep.jade', title=name, ctx={
      'groepen':groepen,
      'leden'  :leden
    })

  return groep_view

urls = patterns('',
  url(r'^$', index, name='index'),
  url(r'^verticalen/$', make_groep_view(Verticale, "Verticalen"), name='index')
)
