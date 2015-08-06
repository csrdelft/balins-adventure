# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_x999_user_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activiteitdeelnemer',
            name='user',
            field=models.OneToOneField(related_name='activiteitdeelnemer', db_column='uid', to='base.Profiel'),
        ),
        migrations.AlterField(
            model_name='bestuurslid',
            name='user',
            field=models.OneToOneField(related_name='bestuurslid', db_column='uid', to='base.Profiel'),
        ),
        migrations.AlterField(
            model_name='bewoners',
            name='user',
            field=models.OneToOneField(related_name='bewoners', db_column='uid', to='base.Profiel'),
        ),
        migrations.AlterField(
            model_name='commissielid',
            name='user',
            field=models.OneToOneField(related_name='commissielid', db_column='uid', to='base.Profiel'),
        ),
        migrations.AlterField(
            model_name='groepslid',
            name='user',
            field=models.OneToOneField(related_name='groepslid', db_column='uid', to='base.Profiel'),
        ),
        migrations.AlterField(
            model_name='ketzerdeelnemer',
            name='user',
            field=models.OneToOneField(related_name='ketzerdeelnemer', db_column='uid', to='base.Profiel'),
        ),
        migrations.AlterField(
            model_name='kringlid',
            name='user',
            field=models.OneToOneField(related_name='kringlid', db_column='uid', to='base.Profiel'),
        ),
        migrations.AlterField(
            model_name='lichtinglid',
            name='user',
            field=models.OneToOneField(related_name='lichtinglid', db_column='uid', to='base.Profiel'),
        ),
        migrations.AlterField(
            model_name='onderverenigingslid',
            name='user',
            field=models.OneToOneField(related_name='onderverenigingslid', db_column='uid', to='base.Profiel'),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='status',
            field=models.CharField(default='NOB', choices=[('NOV', 'NOVIET'), ('CIE', 'COMMISSIE'), ('LID', 'LID'), ('OVE', 'OVERLEDEN'), ('ERE', 'ERELID'), ('EXL', 'EXLID'), ('KRI', 'KRINGEL'), ('GAS', 'GASTLID'), ('NOB', 'NOBODY'), ('OUD', 'OUDLID')], max_length=11),
        ),
        migrations.AlterField(
            model_name='verticalelid',
            name='user',
            field=models.OneToOneField(related_name='verticalelid', db_column='uid', to='base.Profiel'),
        ),
        migrations.AlterField(
            model_name='werkgroepdeelnemer',
            name='user',
            field=models.OneToOneField(related_name='werkgroepdeelnemer', db_column='uid', to='base.Profiel'),
        ),
    ]
