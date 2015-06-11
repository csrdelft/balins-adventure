# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_cleaning_up_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activiteit',
            name='aanmelden_tot',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='aanmelden_vanaf',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='omschrijving',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='samenvatting',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bestuur',
            name='omschrijving',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bestuur',
            name='samenvatting',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='commissie',
            name='omschrijving',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='commissie',
            name='samenvatting',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='groep',
            name='omschrijving',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='groep',
            name='samenvatting',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ketzer',
            name='aanmelden_tot',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ketzer',
            name='aanmelden_vanaf',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ketzer',
            name='omschrijving',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ketzer',
            name='samenvatting',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kring',
            name='omschrijving',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kring',
            name='samenvatting',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lichting',
            name='omschrijving',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='lichting',
            name='samenvatting',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ondervereniging',
            name='omschrijving',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ondervereniging',
            name='samenvatting',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='gebdatum',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='verticale',
            name='omschrijving',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='verticale',
            name='samenvatting',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='werkgroep',
            name='aanmelden_tot',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='werkgroep',
            name='aanmelden_vanaf',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='werkgroep',
            name='omschrijving',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='werkgroep',
            name='samenvatting',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='woonoord',
            name='omschrijving',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='woonoord',
            name='samenvatting',
            field=models.TextField(blank=True),
        ),
    ]
