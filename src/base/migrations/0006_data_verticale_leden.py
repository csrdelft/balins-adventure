# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime

def ensure_verticale_valid_id(apps, schema_editor):
  Verticale = apps.get_model("base", "Verticale")
  try:
    # clone any object with id zero (not allowed in db)
    vertzero = Verticale.objects.get(pk=0)
    vertzero.delete()
    vertzero.pk = None
    vertzero.save()

    # delete original afterwards
  except Exception as e:
    print(str(e))
    pass

def verticale_groep_fill(apps, schema_editor):
  Profiel = apps.get_model("base", "Profiel")
  Verticale = apps.get_model("base", "Verticale")
  verticalen = dict(list(map(lambda v: (v.letter, v), Verticale.objects.all())))
  migration_user = Profiel.objects.get(uid="9999")

  for prof in Profiel.objects.all():
    if prof.verticale in verticalen.keys():
      vert = verticalen.get(prof.verticale)
      vert.leden.create(
        user=prof,
        opmerking="",
        lid_sinds=datetime.date(max(prof.lidjaar, datetime.MINYEAR), 1, 1),
        door_user=migration_user
      )
    else:
      print("Lid %s has invalid verticale %s" % (str(prof.uid), str(prof.verticale)))

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_make_profiel_and_groepen_more_flexible'),
    ]

    operations = [
        # inside transaction by default
        migrations.RunPython(ensure_verticale_valid_id),
        migrations.RunPython(verticale_groep_fill),
    ]
