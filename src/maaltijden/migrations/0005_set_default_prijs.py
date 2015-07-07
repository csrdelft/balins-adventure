# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maaltijden', '0004_remove_verwijderd_in_favor_of_live'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maaltijd',
            name='prijs',
            field=models.IntegerField(default=300),
        ),
        migrations.AlterField(
            model_name='maaltijdrepetitie',
            name='standaard_prijs',
            field=models.IntegerField(default=300),
        ),
    ]
