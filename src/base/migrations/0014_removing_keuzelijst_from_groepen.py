# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_x999_user_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commissie',
            options={'ordering': ['-eind_moment']},
        ),
        migrations.RemoveField(
            model_name='bestuur',
            name='keuzelijst',
        ),
        migrations.RemoveField(
            model_name='commissie',
            name='keuzelijst',
        ),
        migrations.RemoveField(
            model_name='kring',
            name='keuzelijst',
        ),
        migrations.RemoveField(
            model_name='lichting',
            name='keuzelijst',
        ),
        migrations.RemoveField(
            model_name='ondervereniging',
            name='keuzelijst',
        ),
        migrations.RemoveField(
            model_name='verticale',
            name='keuzelijst',
        ),
        migrations.RemoveField(
            model_name='woonoord',
            name='keuzelijst',
        ),
        migrations.AlterField(
            model_name='activiteitdeelnemer',
            name='user',
            field=models.ForeignKey(related_name='activiteitdeelnemer', to='base.Profiel', db_column='uid'),
        ),
        migrations.AlterField(
            model_name='bestuurslid',
            name='user',
            field=models.ForeignKey(related_name='bestuurslid', to='base.Profiel', db_column='uid'),
        ),
        migrations.AlterField(
            model_name='bewoners',
            name='user',
            field=models.ForeignKey(related_name='bewoners', to='base.Profiel', db_column='uid'),
        ),
        migrations.AlterField(
            model_name='commissielid',
            name='user',
            field=models.ForeignKey(related_name='commissielid', to='base.Profiel', db_column='uid'),
        ),
        migrations.AlterField(
            model_name='groepslid',
            name='user',
            field=models.ForeignKey(related_name='groepslid', to='base.Profiel', db_column='uid'),
        ),
        migrations.AlterField(
            model_name='ketzerdeelnemer',
            name='user',
            field=models.ForeignKey(related_name='ketzerdeelnemer', to='base.Profiel', db_column='uid'),
        ),
        migrations.AlterField(
            model_name='kringlid',
            name='user',
            field=models.ForeignKey(related_name='kringlid', to='base.Profiel', db_column='uid'),
        ),
        migrations.AlterField(
            model_name='lichtinglid',
            name='user',
            field=models.ForeignKey(related_name='lichtinglid', to='base.Profiel', db_column='uid'),
        ),
        migrations.AlterField(
            model_name='onderverenigingslid',
            name='user',
            field=models.ForeignKey(related_name='onderverenigingslid', to='base.Profiel', db_column='uid'),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='status',
            field=models.CharField(max_length=11, choices=[('OVE', 'OVERLEDEN'), ('KRI', 'KRINGEL'), ('LID', 'LID'), ('NOB', 'NOBODY'), ('OUD', 'OUDLID'), ('ERE', 'ERELID'), ('EXL', 'EXLID'), ('GAS', 'GASTLID'), ('NOV', 'NOVIET'), ('CIE', 'COMMISSIE')], default='NOB'),
        ),
        migrations.AlterField(
            model_name='verticalelid',
            name='user',
            field=models.ForeignKey(related_name='verticalelid', to='base.Profiel', db_column='uid'),
        ),
        migrations.AlterField(
            model_name='werkgroepdeelnemer',
            name='user',
            field=models.ForeignKey(related_name='werkgroepdeelnemer', to='base.Profiel', db_column='uid'),
        ),
    ]
