# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20150724_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forumdraad',
            old_name='laatste_post_id',
            new_name='laatste_post_old',
        ),
        migrations.AddField(
            model_name='forumdraad',
            name='laatste_post',
            field=models.ForeignKey(to='forum.ForumPost', blank=True, null=True),
        ),
    ]
