# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations

def set_audience(apps, schema_editor):
  Mededeling = apps.get_model("mededelingen", "Mededeling")

  for m in Mededeling.objects.all():
    if m.doelgroep == "iedereen":
      m.audience = 'PUB'
    elif m.doelgroep == "(oud)leden":
      m.audience = 'OUD'
    else:
      m.audience = 'LID'

    m.save()

class Migration(migrations.Migration):

  dependencies = [
    ('mededelingen', '0005_new_target_audience_field'),
  ]

  operations = [
    migrations.RunPython(set_audience)
  ]
