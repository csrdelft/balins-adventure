# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maaltijden', '0003_set_live_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maaltijd',
            name='verwijderd',
        ),
        migrations.AlterField(
            model_name='maaltijdaanmelding',
            name='gasten_eetwens',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
