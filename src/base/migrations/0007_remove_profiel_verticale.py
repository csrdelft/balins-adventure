# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_data_verticale_leden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiel',
            name='verticale',
        ),
    ]
