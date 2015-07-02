# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import livefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maaltijden', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maaltijd',
            name='live',
            field=livefield.fields.LiveField(default=True),
        ),
    ]
