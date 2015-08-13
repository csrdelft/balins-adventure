# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_x999_user_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoccieBestelling',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('soccieid', models.IntegerField(db_column='socCieId', null=True, blank=True)),
                ('totaal', models.IntegerField(null=True, blank=True)),
                ('tijd', models.DateTimeField(null=True, blank=True)),
                ('deleted', models.IntegerField()),
            ],
            options={
                'db_table': 'socCieBestelling',
            },
        ),
        migrations.CreateModel(
            name='SoccieBestellingInhoud',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('aantal', models.IntegerField(null=True, blank=True)),
                ('bestellingid', models.ForeignKey(to='soccie.SoccieBestelling', db_column='bestellingId')),
            ],
            options={
                'db_table': 'socCieBestellingInhoud',
            },
        ),
        migrations.CreateModel(
            name='SoccieGrootboekType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'socCieGrootboekType',
            },
        ),
        migrations.CreateModel(
            name='SoccieKlanten',
            fields=[
                ('soccieid', models.IntegerField(primary_key=True, db_column='socCieId', serialize=False)),
                ('saldo', models.IntegerField(null=True, blank=True)),
                ('naam', models.TextField(blank=True)),
                ('deleted', models.IntegerField()),
                ('stekuid', models.ForeignKey(to='base.Profiel', blank=True, db_column='stekUID')),
            ],
            options={
                'db_table': 'socCieKlanten',
            },
        ),
        migrations.CreateModel(
            name='SoccieLog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('ip', models.CharField(max_length=15)),
                ('type', models.CharField(max_length=6)),
                ('value', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'db_table': 'socCieLog',
            },
        ),
        migrations.CreateModel(
            name='SocciePrijs',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('van', models.DateTimeField()),
                ('tot', models.DateTimeField()),
                ('prijs', models.IntegerField()),
            ],
            options={
                'db_table': 'socCiePrijs',
            },
        ),
        migrations.CreateModel(
            name='SoccieProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('beschrijving', models.TextField(blank=True)),
                ('prioriteit', models.IntegerField()),
                ('beheer', models.IntegerField()),
                ('grootboekid', models.ForeignKey(to='soccie.SoccieGrootboekType', db_column='grootboekId')),
            ],
            options={
                'db_table': 'socCieProduct',
            },
        ),
        migrations.AddField(
            model_name='soccieprijs',
            name='productid',
            field=models.ForeignKey(to='soccie.SoccieProduct', db_column='productId'),
        ),
        migrations.AddField(
            model_name='socciebestellinginhoud',
            name='productid',
            field=models.ForeignKey(to='soccie.SoccieProduct', db_column='productId'),
        ),
    ]
