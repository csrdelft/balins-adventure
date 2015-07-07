# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_optional_fields_fixes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mededeling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datum', models.DateTimeField(null=True, blank=True)),
                ('vervaltijd', models.DateTimeField(null=True, blank=True)),
                ('titel', models.TextField()),
                ('tekst', models.TextField()),
                ('prive', models.CharField(max_length=1)),
                ('zichtbaarheid', models.CharField(max_length=17)),
                ('prioriteit', models.IntegerField()),
                ('doelgroep', models.CharField(max_length=10)),
                ('verborgen', models.CharField(max_length=1)),
                ('verwijderd', models.CharField(max_length=1)),
                ('plaatje', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to='base.Profiel', db_column='uid', max_length=4)),
            ],
            options={
                'db_table': 'mededeling',
            },
        ),
    ]
