# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def createX999(apps, schema_editor):
  User = apps.get_model('auth', 'User')
  Profiel = apps.get_model('base', 'Profiel')
  Verticale = apps.get_model('base', 'Verticale')

  if not Profiel.objects.filter(uid='x999').exists():
    # get (or create) the related requirements
    migration_user = User.objects.get(username='migratie').profiel
    geen_verticale = Verticale.objects.get_or_create(naam='Geen', defaults={
      'familie': 'Verticale',
      'letter': '_',
      'maker_user': migration_user,
      'status': 'ht'
    })

    print("Creating x999")
    x999 = Profiel.objects.create(
      uid='x999',
      user=None, # anonymous user has no auth account
      nickname= "nobody",
      duckname= "",
      voornaam= "Niet",
      tussenvoegsel= "",
      achternaam= "ingelogd",
      voorletters= "Niet",
      postfix= "",
      adres= "",
      postcode= "",
      woonplaats= "",
      land= "Nederland",
      telefoon= "",
      mobiel= "",
      geslacht= "m",
      voornamen= "",
      echtgenoot= "",
      adresseringechtpaar= "",
      icq= "",
      msn= "",
      skype= "",
      jid= "",
      linkedin= "",
      website= "",
      beroep= "",
      studie= "",
      patroon= "",
      studienr= None,
      studiejaar= 0,
      lidjaar= 0,
      lidafdatum= None,
      gebdatum= None,
      sterfdatum= None,
      bankrekening= "",
      machtiging= 0,
      verticaleleider= 0,
      kringcoach= "",
      email= "",
      kerk= "",
      muziek= "",
      status= "NOB",
      eetwens= "",
      corvee_punten= 0,
      corvee_punten_bonus= 0,
      soccieid= 0,
      createterm= "barvoor",
      socciesaldo= 0.0,
      maalciesaldo= 0.0,
      lengte= 0,
      vrienden= "",
      middelbareschool= ""
    )

    x999.verticale = geen_verticale
    x999.save()



class Migration(migrations.Migration):

  dependencies = [
    ('base', '0012_minor_parameter_fixes'),
  ]

  operations = [
    migrations.RunPython(createX999)
  ]
