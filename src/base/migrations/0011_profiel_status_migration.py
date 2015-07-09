# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations

def set_status(apps, schema_editor):
  Profiel = apps.get_model("base", "Profiel")

  for p in Profiel.objects.all():
    if p.status == "S_OUDLID":
      p.status = 'OUD'
    elif p.status == "S_EXLID":
      p.status = 'EXL'
    elif p.status == 'S_LID':
      p.status = 'LID'
    elif p.status == 'S_NOBODY':
      p.status = 'NOB'
    elif p.status == 'S_OVERLEDEN':
      p.status = 'OVE'
    elif p.status == 'S_GASTLID':
      p.status = 'GAS'
    elif p.status == 'S_NOVIET':
      p.status = 'NOV'
    elif p.status == 'S_ERELID':
      p.status = 'ERE'
    elif p.status == 'S_CIE':
      p.status = 'CIE'
    elif p.status == 'S_KRINGEL':
      p.status = 'KRI'
    else:
      p.status = 'NOB'

    p.save()

class Migration(migrations.Migration):

  dependencies = [
    ('base', '0010_optional_fields_fixes'),
  ]

  operations = [
    migrations.RunPython(set_status)
  ]
