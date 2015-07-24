# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_data_laatste_post_to_foreignkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumdraad',
            name='laatste_post_old',
        ),
    ]
