# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_profiel_status_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiel',
            name='status',
            field=models.CharField(default='NOB', max_length=11, choices=[('ERE', 'ERELID'), ('NOV', 'NOVIET'), ('KRI', 'KRINGEL'), ('NOB', 'NOBODY'), ('OVE', 'OVERLEDEN'), ('OUD', 'OUDLID'), ('CIE', 'COMMISSIE'), ('GAS', 'GASTLID'), ('EXL', 'EXLID'), ('LID', 'LID')]),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='user',
            field=models.OneToOneField(related_name='profiel', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
