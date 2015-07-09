# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mededelingen', '0006_data_doelgroep_to_audience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mededeling',
            name='doelgroep',
        ),
        migrations.RemoveField(
            model_name='mededeling',
            name='prive',
        ),
        migrations.AlterField(
            model_name='mededeling',
            name='audience',
            field=models.CharField(max_length=3, default='LID', choices=[('LEDEN', 'LID'), ('PUBLIC', 'PUB'), ('OUDLEDEN', 'OUD')]),
        ),
    ]
