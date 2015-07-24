# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20150709_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumdraad',
            name='laatst_gewijzigd',
        ),
        migrations.RemoveField(
            model_name='forumdraad',
            name='laatste_wijziging_user',
        ),
        migrations.RemoveField(
            model_name='forumdraad',
            name='pagina_per_post',
        ),
    ]
