# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20150707_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mededeling',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('datum', models.DateTimeField(null=True, blank=True)),
                ('vervaltijd', models.DateTimeField(null=True, blank=True)),
                ('titel', models.TextField()),
                ('tekst', models.TextField()),
                ('prive', models.CharField(max_length=1)),
                ('prioriteit', models.IntegerField()),
                ('doelgroep', models.CharField(max_length=10)),
                ('verborgen', models.CharField(max_length=1)),
                ('verwijderd', models.CharField(max_length=1)),
                ('plaatje', models.CharField(max_length=255)),
                ('user', models.ForeignKey(max_length=4, db_column='uid', to='base.Profiel')),
            ],
            options={
                'db_table': 'mededeling',
            },
        ),
    ]
