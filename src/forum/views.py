from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from base.views import render_with_layout
from base.utils import grouped_dict
from .models import *

import logging
logger = logging.getLogger(__name__)

import django_tables2 as tables
from django_tables2.utils import A

class ForumTable(tables.Table):
  class Meta:
    orderable = False
    attrs = {
      "class" : 'table table-striped table-hover table-condensed'
    }

class ForumMostRecentTable(ForumTable):
  titel = tables.LinkColumn('forum.draad', args=[A('draad_id')])
  laatst_gewijzigd = tables.DateTimeColumn(orderable=True)

  class Meta(ForumTable.Meta):
    model = ForumDraad
    fields = ('uid_id', 'titel', 'laatst_gewijzigd', 'laatste_wijziging_uid_id')
    order_by = ('-laatst_gewijzigd',)

def forum_root(request):
  # TODO filter viewable by user
  queryset = ForumDraad.objects.all()

  # filter on forum deel
  if 'forum' in request.GET:
    titel = ForumDeel.objects.get(pk=request.GET['forum']).titel + " Reformaforum"
    queryset = queryset.filter(forum_id=request.GET['forum'])
  else:
    titel = "Reformaforum"

  table = ForumMostRecentTable(queryset)
  table.paginate(page=request.GET.get('page', 1), per_page=25)

  delen = ForumDeel.get_viewable_by(request.user)
  cats = grouped_dict(map(lambda d: (d.categorie, d), delen))

  return render_with_layout(request, 'forum_main.jade', title=titel, ctx={
    'categories': cats,
    'posts': table
  })

def forum_draad(request, draad_id):
  draad = ForumDraad.objects.get(pk=draad_id)
  posts = ForumPost.objects.all()\
    .filter(draad_id=draad_id)\
    .order_by('datum_tijd')

  return render_with_layout(request, 'forum_draad.jade', title="Forum draad %s" % draad.titel, ctx={
    'draad': draad,
    'posts': posts
  })

urls = patterns('',
   url(r'^$', forum_root, name='forum.main'),
   url(r'^(\d+)/', forum_draad, name='forum.draad'),
)
