# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_cleaning_up_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maaltijd',
            fields=[
                ('id', models.AutoField(db_column='maaltijd_id', primary_key=True, serialize=False)),
                ('titel', models.CharField(max_length=255)),
                ('datum', models.DateField()),
                ('tijd', models.TimeField()),
                ('prijs', models.IntegerField()),
                ('omschrijving', models.CharField(max_length=255, blank=True)),
                ('verwijderd', models.BooleanField()),
                ('gesloten', models.BooleanField()),
                ('laatst_gesloten', models.DateTimeField(blank=True, null=True)),
                ('aanmeld_filter', models.CharField(max_length=255, blank=True)),
                ('aanmeld_limiet', models.IntegerField()),
            ],
            options={
                'db_table': 'mlt_maaltijden',
            },
        ),
        migrations.CreateModel(
            name='MaaltijdAanmelding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('standaard_tijd', models.TimeField()),
                ('standaard_prijs', models.IntegerField()),
                ('abonneerbaar', models.IntegerField()),
                ('standaard_limiet', models.IntegerField()),
                ('abonnement_filter', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'mlt_repetities',
            },
        ),
        migrations.AddField(
            model_name='maaltijdabo',
            name='mlt_repetitie',
            field=models.ForeignKey(to='maaltijden.MaaltijdRepetitie'),
        ),
        migrations.AddField(
            model_name='maaltijdabo',
            name='user',
            field=models.ForeignKey(db_column='uid', to='base.Profiel'),
        ),
        migrations.AddField(
            model_name='maaltijdaanmelding',
            name='door_abonnement',
            field=models.ForeignKey(blank=True, null=True, to='maaltijden.MaaltijdRepetitie', db_column='door_abonnement'),
        ),
        migrations.AddField(
            model_name='maaltijdaanmelding',
            name='door_user',
            field=models.ForeignKey(related_name='+', null=True, to='base.Profiel', db_column='door_uid'),
        ),
        migrations.AddField(
            model_name='maaltijdaanmelding',
            name='maaltijd',
            field=models.ForeignKey(to='maaltijden.Maaltijd'),
        ),
        migrations.AddField(
            model_name='maaltijdaanmelding',
            name='user',
            field=models.ForeignKey(db_column='uid', to='base.Profiel'),
        ),
        migrations.AddField(
            model_name='maaltijd',
            name='repetitie',
            field=models.ForeignKey(blank=True, null=True, to='maaltijden.MaaltijdRepetitie', db_column='mlt_repetitie_id'),
        ),
        migrations.AlterUniqueTogether(
            name='maaltijdabo',
            unique_together=set([('user', 'mlt_repetitie')]),
        ),
        migrations.AlterUniqueTogether(
            name='maaltijdaanmelding',
            unique_together=set([('maaltijd', 'user')]),
        ),
    ]
