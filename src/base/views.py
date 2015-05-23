from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.template import loader, RequestContext
from .models import *

from collections import OrderedDict
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

def profiel(request, uid):
  try:
    user = Profiel.objects.get(pk=uid)
  except Profiel.DoesNotExist:
    raise Http404("Geen gebruiker met lidnummer %s" % uid)

  return render_with_layout(request, 'profiel.jade', title=user.full_name(), ctx={
    "user": user,
    "kring": user.kring(),
    "verticale": user.verticale(),
    "commissies": user.commissies(),
    "werkgroepen": user.werkgroepen(),
    "onderverenigingen": user.onderverenigingen(),
    "groepen": user.overige_groepen()
  })

def make_groep_view(groepen_qs, leden_qs, name):
  def groep_view(request):
    groepen = OrderedDict(list(map(lambda g: (g.pk, (g, [])), groepen_qs)))
    leden   = leden_qs

    # sort the members
    for lid in leden:
      # if somehow the group doesn't exist, skip the member
      groep = groepen.get(lid.groep_id)
      if groep is not None:
        groep[1].append(lid)

    return render_with_layout(request, 'groep.jade', title=name, ctx={
      'groepen':groepen,
      'leden'  :leden
    })

  return groep_view

verticalen_view = make_groep_view(
  Verticale.objects.all(),
  VerticaleLid.objects.filter(user__status="S_LID"),
  "Verticalen")

lichtingen_view = make_groep_view(
  Lichting.objects.all().order_by('-lidjaar'),
  LichtingLid.objects.all().exclude(groep=Lichting.objects.get(lidjaar=0)),
  "Lichtingen")

commissies_view = make_groep_view(
  Commissie.objects.filter(status='ht').order_by('naam'),
  CommissieLid.objects.filter(groep__status='ht'),
  "Lichtingen")

urls = patterns('',
  url(r'^$', index, name='index'),
  url(r'^profiel/(.{4})/$', profiel, name='base.profiel'),
  url(r'^verticalen/$', verticalen_view, name='base.verticalen'),
  url(r'^lichtingen/$', lichtingen_view, name='base.lichtingen'),
  url(r'^commissies/$', commissies_view, name='base.commissies'),
)
