# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mededelingen', '0004_delete_verborgen_verwijderd'),
    ]

    operations = [
        migrations.AddField(
            model_name='mededeling',
            name='audience',
            field=models.CharField(default='LID', max_length=3, choices=[('O', 'U'), ('O', 'U'), ('P', 'U'), ('L', 'E')]),
        ),
        migrations.AlterField(
            model_name='mededeling',
            name='datum',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
