# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_optional_fields_fixes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maaltijd',
            fields=[
                ('id', models.AutoField(db_column='maaltijd_id', primary_key=True, serialize=False)),
                ('titel', models.CharField(max_length=255)),
                ('datum', models.DateField()),
                ('tijd', models.TimeField(default=datetime.time(18, 0))),
                ('prijs', models.IntegerField(default=3)),
                ('omschrijving', models.CharField(blank=True, max_length=255)),
                ('gesloten', models.BooleanField(default=False)),
                ('verwijderd', models.BooleanField(default=False)),
                ('laatst_gesloten', models.DateTimeField(blank=True, null=True)),
                ('aanmeld_filter', models.CharField(blank=True, max_length=255)),
                ('aanmeld_limiet', models.IntegerField(default=100)),
            ],
            options={
                'db_table': 'mlt_maaltijden',
            },
        ),
        migrations.CreateModel(
            name='MaaltijdAanmelding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('aantal_gasten', models.IntegerField()),
                ('gasten_eetwens', models.CharField(max_length=255)),
                ('laatst_gewijzigd', models.DateTimeField()),
            ],
            options={
                'db_table': 'mlt_aanmeldingen',
            },
        ),
        migrations.CreateModel(
            name='MaaltijdAbo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('wanneer_ingeschakeld', models.DateTimeField()),
            ],
            options={
                'db_table': 'mlt_abonnementen',
            },
        ),
        migrations.CreateModel(
            name='MaaltijdRepetitie',
            fields=[
                ('id', models.AutoField(db_column='mlt_repetitie_id', primary_key=True, serialize=False)),
                ('dag_vd_week', models.IntegerField()),
                ('periode_in_dagen', models.IntegerField()),
                ('standaard_titel', models.CharField(max_length=255)),
                ('standaard_tijd', models.TimeField(default=datetime.time(18, 0))),
                ('standaard_prijs', models.IntegerField(default=3)),
                ('abonneerbaar', models.IntegerField()),
                ('standaard_limiet', models.IntegerField(default=100)),
                ('abonnement_filter', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'mlt_repetities',
            },
        ),
        migrations.AddField(
            model_name='maaltijdabo',
            name='repetitie',
            field=models.ForeignKey(db_column='mlt_repetitie_id', to='maaltijden.MaaltijdRepetitie'),
        ),
        migrations.AddField(
            model_name='maaltijdabo',
            name='user',
            field=models.ForeignKey(db_column='uid', to='base.Profiel'),
        ),
        migrations.AddField(
            model_name='maaltijdaanmelding',
            name='door_abonnement',
            field=models.ForeignKey(db_column='door_abonnement', null=True, to='maaltijden.MaaltijdRepetitie', blank=True),
        ),
        migrations.AddField(
            model_name='maaltijdaanmelding',
            name='door_user',
            field=models.ForeignKey(db_column='door_uid', null=True, to='base.Profiel', related_name='+'),
        ),
        migrations.AddField(
            model_name='maaltijdaanmelding',
            name='maaltijd',
            field=models.ForeignKey(related_name='aanmeldingen', to='maaltijden.Maaltijd'),
        ),
        migrations.AddField(
            model_name='maaltijdaanmelding',
            name='user',
            field=models.ForeignKey(db_column='uid', to='base.Profiel'),
        ),
        migrations.AddField(
            model_name='maaltijd',
            name='repetitie',
            field=models.ForeignKey(db_column='mlt_repetitie_id', null=True, to='maaltijden.MaaltijdRepetitie', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='maaltijdabo',
            unique_together=set([('user', 'repetitie')]),
        ),
        migrations.AlterUniqueTogether(
            name='maaltijdaanmelding',
            unique_together=set([('maaltijd', 'user')]),
        ),
    ]
