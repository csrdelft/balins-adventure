# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import livefield.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mededelingen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mededeling',
            name='zichtbaarheid',
        ),
        migrations.AddField(
            model_name='mededeling',
            name='live',
            field=livefield.fields.LiveField(default=True),
        ),
        migrations.AlterField(
            model_name='mededeling',
            name='datum',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
