# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_data_lichting_leden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bewoners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opmerking', models.CharField(blank=True, max_length=255)),
                ('lid_sinds', models.DateTimeField()),
                ('door_user', models.ForeignKey(to='base.Profiel', related_name='+', db_column='door_uid')),
            ],
            options={
                'db_table': 'bewoners',
            },
        ),
        migrations.CreateModel(
            name='Woonoord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('naam', models.CharField(max_length=255)),
                ('status', models.CharField(default='ht', max_length=2)),
                ('familie', models.CharField(max_length=255)),
                ('samenvatting', models.TextField(default='', blank=True)),
                ('omschrijving', models.TextField(default='', blank=True)),
                ('begin_moment', models.DateTimeField(blank=True, null=True)),
                ('eind_moment', models.DateTimeField(blank=True, null=True)),
                ('keuzelijst', models.CharField(blank=True, max_length=255)),
                ('maker_user', models.ForeignKey(to='base.Profiel', related_name='+', db_column='maker_uid')),
            ],
            options={
                'db_table': 'woonoorden',
            },
        ),
        migrations.RenameModel('GroepLeden', 'GroepsLid'),
        migrations.AlterField(
            model_name='activiteit',
            name='in_agenda',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='omschrijving',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='samenvatting',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='status',
            field=models.CharField(default='ht', max_length=2),
        ),
        migrations.AlterField(
            model_name='bestuur',
            name='omschrijving',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='bestuur',
            name='samenvatting',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='bestuur',
            name='status',
            field=models.CharField(default='ht', max_length=2),
        ),
        migrations.AlterField(
            model_name='commissie',
            name='omschrijving',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='commissie',
            name='samenvatting',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='commissie',
            name='status',
            field=models.CharField(default='ht', max_length=2),
        ),
        migrations.AlterField(
            model_name='groep',
            name='omschrijving',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='groep',
            name='samenvatting',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='groep',
            name='status',
            field=models.CharField(default='ht', max_length=2),
        ),
        migrations.AlterField(
            model_name='ketzer',
            name='omschrijving',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='ketzer',
            name='samenvatting',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='ketzer',
            name='status',
            field=models.CharField(default='ht', max_length=2),
        ),
        migrations.AlterField(
            model_name='kring',
            name='omschrijving',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='kring',
            name='samenvatting',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='kring',
            name='status',
            field=models.CharField(default='ht', max_length=2),
        ),
        migrations.AlterField(
            model_name='lichting',
            name='omschrijving',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='lichting',
            name='samenvatting',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='lichting',
            name='status',
            field=models.CharField(default='ht', max_length=2),
        ),
        migrations.AlterField(
            model_name='ondervereniging',
            name='omschrijving',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='ondervereniging',
            name='samenvatting',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='ondervereniging',
            name='status',
            field=models.CharField(default='ht', max_length=2),
        ),
        migrations.AlterField(
            model_name='verticale',
            name='omschrijving',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='verticale',
            name='samenvatting',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='verticale',
            name='status',
            field=models.CharField(default='ht', max_length=2),
        ),
        migrations.AlterField(
            model_name='werkgroep',
            name='omschrijving',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='werkgroep',
            name='samenvatting',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='werkgroep',
            name='status',
            field=models.CharField(default='ht', max_length=2),
        ),
        migrations.AddField(
            model_name='bewoners',
            name='groep',
            field=models.ForeignKey(related_name='leden', to='base.Woonoord'),
        ),
        migrations.AddField(
            model_name='bewoners',
            name='user',
            field=models.ForeignKey(to='base.Profiel', related_name='+', db_column='uid'),
        ),
    ]
