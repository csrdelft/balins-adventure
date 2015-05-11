# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20150509_2011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forumdeel',
            options={'default_permissions': ('add', 'change', 'delete', 'moderate', 'post_in')},
        ),
    ]
