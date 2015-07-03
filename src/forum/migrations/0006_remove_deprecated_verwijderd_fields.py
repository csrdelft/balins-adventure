# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_data_livefields_import'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumdraad',
            name='verwijderd',
        ),
        migrations.RemoveField(
            model_name='forumpost',
            name='verwijderd',
        ),
    ]
