# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='item_id')),
                ('begin_moment', models.DateTimeField()),
                ('eind_moment', models.DateTimeField()),
                ('beschrijving', models.TextField(blank=True)),
                ('locatie', models.CharField(max_length=255, blank=True)),
                ('titel', models.CharField(max_length=255)),
                ('rechten_bekijken', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'agenda',
            },
        ),
        migrations.CreateModel(
            name='AgendaVerbergen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=4)),
                ('uuid', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'agenda_verbergen',
            },
        ),
        migrations.AlterUniqueTogether(
            name='agendaverbergen',
            unique_together=set([('uid', 'uuid')]),
        ),
    ]
