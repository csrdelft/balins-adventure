# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def set_live(apps, schema_editor):
  Maaltijd = apps.get_model("maaltijden", "Maaltijd")
  for mlt in Maaltijd.objects.all():
    mlt.live = not mlt.verwijderd
    mlt.save()

class Migration(migrations.Migration):

    dependencies = [
        ('maaltijden', '0002_maaltijd_live'),
    ]

    operations = [
        migrations.RunPython(set_live)
    ]
