# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mededelingen', '0003_populatelive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mededeling',
            name='verborgen',
        ),
        migrations.RemoveField(
            model_name='mededeling',
            name='verwijderd',
        ),
    ]
