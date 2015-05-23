# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime

def create_lichtingen(apps, schema_editor):
  Profiel = apps.get_model("base", "Profiel")
  Lichting = apps.get_model("base", "Lichting")
  migration_user = Profiel.objects.get(uid="9999")

  Lichting.objects.create(
    naam="Onbekende lichting",
    status = "ht",
    familie = "Lichting",
    maker_user = migration_user,
    lidjaar=0
  )

  for lidjaar in range(1950, 2015):
    Lichting.objects.create(
      naam="Lichting %s" % str(lidjaar),
      lidjaar=lidjaar,
      status = "ht",
      familie = "Lichting",
      maker_user = migration_user,
    )

def lichting_groep_fill(apps, schema_editor):
  Profiel = apps.get_model("base", "Profiel")
  Lichting = apps.get_model("base", "Lichting")
  lichtingen = dict(list(map(lambda l: (l.lidjaar, l), Lichting.objects.all())))
  migration_user = Profiel.objects.get(uid="9999")

  for prof in Profiel.objects.all():
    if prof.lidjaar in lichtingen.keys():
      lichting = lichtingen.get(prof.lidjaar)
      lichting.leden.create(
        user=prof,
        opmerking="",
        lid_sinds=datetime.date(max(prof.lidjaar, datetime.MINYEAR), 1, 1),
        door_user=migration_user
      )
    else:
      print("Lid %s has invalid lidjaar %s" % (str(prof.uid), str(prof.lidjaar)))

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_profiel_verticale'),
    ]

    operations = [
        # inside transaction by default
        migrations.RunPython(create_lichtingen),
        migrations.RunPython(lichting_groep_fill),
    ]
