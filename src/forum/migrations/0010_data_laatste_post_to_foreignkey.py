# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def set_laatste_post(apps, schema_editor):
  ForumDraad = apps.get_model("forum", "ForumDraad")
  ForumPost = apps.get_model("forum", "ForumPost")

  for draad in ForumDraad.objects.all():
    laatste_post = list(ForumPost.objects.filter(pk=draad.laatste_post_old))
    if(len(laatste_post) == 0):
      draad.laatste_post = None
    else:
      draad.laatste_post = laatste_post[0]

    draad.save()

class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20150724_2251'),
    ]

    operations = [
        migrations.RunPython(set_laatste_post)
    ]
