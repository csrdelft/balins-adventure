# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_remove_deprecated_verwijderd_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumdraad',
            name='forum',
            field=models.ForeignKey(related_name='draden', db_column='forum_id', to='forum.ForumDeel'),
        ),
        migrations.AlterField(
            model_name='forumdraadvolgen',
            name='draad',
            field=models.ForeignKey(related_name='subscribers', db_column='draad_id', to='forum.ForumDraad'),
        ),
    ]
