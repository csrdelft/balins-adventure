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
        migrations.AlterField(
            model_name='mededeling',
            name='audience',
            field=models.CharField(choices=[('L', 'E'), ('P', 'U'), ('O', 'U')], default='LID', max_length=3),
        ),
    ]
