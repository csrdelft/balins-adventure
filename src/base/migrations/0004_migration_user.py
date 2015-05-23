# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.models import User
import datetime

def create_migration_user(apps, schema_editor):
  Profiel = apps.get_model("base", "Profiel")

  user = User.objects.create_user(username="migratie")
  profiel = Profiel.objects.create(
    achternaam='Graties',
    adres='Server',
    adresseringechtpaar='',
    bankrekening='',
    beroep='',
    changelog='',
    corvee_punten=1000,
    corvee_punten_bonus=1000,
    createterm='soccie',
    duckname='',
    echtgenoot='',
    eetwens='',
    email='pubcie@csrdelft.nl',
    gebdatum=datetime.date(1970, 1, 1),
    geslacht='m',
    icq='',
    jid='',
    kerk='',
    kgb='',
    kringcoach='',
    land='',
    lengte=250,
    lidafdatum=None,
    lidjaar=1970,
    linkedin='',
    maalciesaldo=0.0,
    machtiging=0,
    matrixplek='13',
    medisch='',
    middelbareschool='',
    mobiel='',
    moot='0',
    msn='',
    muziek='',
    nickname='migratie',
    novietsoort='0',
    novitiaat='',
    novitiaatbijz='',
    o_adres='',
    o_land='',
    o_postcode='',
    o_telefoon='',
    o_woonplaats='',
    ontvangtcontactueel='nee',
    ovkaart='week',
    patroon='',
    postcode='',
    postfix='',
    skype='',
    soccieid=-1,
    socciesaldo=0,
    startkamp='0',
    status='S_LID',
    sterfdatum=None,
    studie='TU Delft - TI',
    studiejaar=2000,
    studienr=0,
    telefoon='',
    tussenvoegsel='',
    uid='9999',
    user_id=user.pk,
    verticale='G',
    verticaleleider=0,
    voorletters='M.',
    voornaam='Mi',
    voornamen='Mi',
    vrienden='Jij!',
    website='',
    woonplaats='Delft',
    zingen='nee')

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_create_groepen'),
    ]

    operations = [
        migrations.RunPython(create_migration_user),
    ]
