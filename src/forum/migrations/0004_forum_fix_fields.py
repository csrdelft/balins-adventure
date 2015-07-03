# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import livefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20150511_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumdraad',
            name='live',
            field=livefield.fields.LiveField(default=True),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='live',
            field=livefield.fields.LiveField(default=True),
        ),
        migrations.AlterField(
            model_name='forumdraad',
            name='eerste_post_plakkerig',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='forumdraad',
            name='gesloten',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='forumdraad',
            name='plakkerig',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='forumdraad',
            name='verwijderd',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='forumdraad',
            name='wacht_goedkeuring',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='auteur_ip',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='draad',
            field=models.ForeignKey(to='forum.ForumDraad', related_name='posts', db_column='draad_id'),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='verwijderd',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='wacht_goedkeuring',
            field=models.BooleanField(default=False),
        ),
    ]
