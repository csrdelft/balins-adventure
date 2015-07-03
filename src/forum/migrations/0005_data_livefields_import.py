# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def set_live(apps, schema_editor):
  ForumPost = apps.get_model("forum", "ForumPost")
  ForumDraad = apps.get_model("forum", "ForumDraad")
  for draad in ForumDraad.objects.all():
    draad.live = not draad.verwijderd
    draad.save()
  for post in ForumPost.objects.all():
    post.live = not post.verwijderd
    post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_forum_fix_fields'),
    ]

    operations = [
        migrations.RunPython(set_live)
    ]
