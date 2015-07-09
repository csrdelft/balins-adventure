# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def set_live(apps, schema_editor):
  Mededeling = apps.get_model("mededelingen", "Mededeling")
  for m in Mededeling.objects.all():
    m.live = (m.verwijderd == '0') and (m.verborgen == '0')
    m.save()

class Migration(migrations.Migration):

    dependencies = [
        ('mededelingen', '0002_live_model'),
    ]

    operations = [
        migrations.RunPython(set_live)
    ]
