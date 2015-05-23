# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_profiel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activiteit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('naam', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=2)),
                ('familie', models.CharField(max_length=255)),
                ('samenvatting', models.TextField()),
                ('omschrijving', models.TextField(blank=True)),
                ('begin_moment', models.DateTimeField()),
                ('eind_moment', models.DateTimeField(null=True, blank=True)),
                ('keuzelijst', models.CharField(blank=True, max_length=255)),
                ('aanmeld_limiet', models.IntegerField(null=True, blank=True)),
                ('aanmelden_vanaf', models.DateTimeField()),
                ('aanmelden_tot', models.DateTimeField()),
                ('bewerken_tot', models.DateTimeField(null=True, blank=True)),
                ('afmelden_tot', models.DateTimeField(null=True, blank=True)),
                ('soort', models.CharField(max_length=15)),
                ('rechten_aanmelden', models.CharField(blank=True, max_length=255)),
                ('locatie', models.CharField(blank=True, max_length=255)),
                ('in_agenda', models.IntegerField()),
                ('maker_user', models.ForeignKey(to='base.Profiel', db_column='maker_uid', related_name='+')),
            ],
            options={
                'db_table': 'activiteiten',
            },
        ),
        migrations.CreateModel(
            name='ActiviteitDeelnemer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opmerking', models.CharField(blank=True, max_length=255)),
                ('lid_sinds', models.DateTimeField()),
                ('door_user', models.ForeignKey(to='base.Profiel', db_column='door_uid', related_name='+')),
                ('groep', models.ForeignKey(to='base.Activiteit')),
                ('user', models.ForeignKey(to='base.Profiel', db_column='uid', related_name='+')),
            ],
            options={
                'db_table': 'activiteit_deelnemers',
            },
        ),
        migrations.CreateModel(
            name='Bestuur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('naam', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=2)),
                ('familie', models.CharField(max_length=255)),
                ('samenvatting', models.TextField()),
                ('omschrijving', models.TextField(blank=True)),
                ('begin_moment', models.DateTimeField()),
                ('eind_moment', models.DateTimeField(null=True, blank=True)),
                ('keuzelijst', models.CharField(blank=True, max_length=255)),
                ('bijbeltekst', models.TextField()),
                ('maker_user', models.ForeignKey(to='base.Profiel', db_column='maker_uid', related_name='+')),
            ],
            options={
                'db_table': 'besturen',
            },
        ),
        migrations.CreateModel(
            name='BestuursLid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opmerking', models.CharField(blank=True, max_length=255)),
                ('lid_sinds', models.DateTimeField()),
                ('door_user', models.ForeignKey(to='base.Profiel', db_column='door_uid', related_name='+')),
                ('groep', models.ForeignKey(to='base.Bestuur')),
                ('user', models.ForeignKey(to='base.Profiel', db_column='uid', related_name='+')),
            ],
            options={
                'db_table': 'bestuurs_leden',
            },
        ),
        migrations.CreateModel(
            name='Commissie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('naam', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=2)),
                ('familie', models.CharField(max_length=255)),
                ('samenvatting', models.TextField()),
                ('omschrijving', models.TextField(blank=True)),
                ('begin_moment', models.DateTimeField()),
                ('eind_moment', models.DateTimeField(null=True, blank=True)),
                ('keuzelijst', models.CharField(blank=True, max_length=255)),
                ('soort', models.CharField(max_length=1)),
                ('maker_user', models.ForeignKey(to='base.Profiel', db_column='maker_uid', related_name='+')),
            ],
            options={
                'db_table': 'commissies',
            },
        ),
        migrations.CreateModel(
            name='CommissieLid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opmerking', models.CharField(blank=True, max_length=255)),
                ('lid_sinds', models.DateTimeField()),
                ('door_user', models.ForeignKey(to='base.Profiel', db_column='door_uid', related_name='+')),
                ('groep', models.ForeignKey(to='base.Commissie')),
                ('user', models.ForeignKey(to='base.Profiel', db_column='uid', related_name='+')),
            ],
            options={
                'db_table': 'commissie_leden',
            },
        ),
        migrations.CreateModel(
            name='Groep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('naam', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=2)),
                ('familie', models.CharField(max_length=255)),
                ('samenvatting', models.TextField()),
                ('omschrijving', models.TextField(blank=True)),
                ('begin_moment', models.DateTimeField()),
                ('eind_moment', models.DateTimeField(null=True, blank=True)),
                ('keuzelijst', models.CharField(blank=True, max_length=255)),
                ('rechten_aanmelden', models.CharField(max_length=255)),
                ('maker_user', models.ForeignKey(to='base.Profiel', db_column='maker_uid', related_name='+')),
            ],
            options={
                'db_table': 'groepen',
            },
        ),
        migrations.CreateModel(
            name='GroepLeden',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opmerking', models.CharField(blank=True, max_length=255)),
                ('lid_sinds', models.DateTimeField()),
                ('door_user', models.ForeignKey(to='base.Profiel', db_column='door_uid', related_name='+')),
                ('groep', models.ForeignKey(to='base.Groep')),
                ('user', models.ForeignKey(to='base.Profiel', db_column='uid', related_name='+')),
            ],
            options={
                'db_table': 'groep_leden',
            },
        ),
        migrations.CreateModel(
            name='Ketzer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('naam', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=2)),
                ('familie', models.CharField(max_length=255)),
                ('samenvatting', models.TextField()),
                ('omschrijving', models.TextField(blank=True)),
                ('begin_moment', models.DateTimeField()),
                ('eind_moment', models.DateTimeField(null=True, blank=True)),
                ('keuzelijst', models.CharField(blank=True, max_length=255)),
                ('aanmeld_limiet', models.IntegerField(null=True, blank=True)),
                ('aanmelden_vanaf', models.DateTimeField()),
                ('aanmelden_tot', models.DateTimeField()),
                ('bewerken_tot', models.DateTimeField(null=True, blank=True)),
                ('afmelden_tot', models.DateTimeField(null=True, blank=True)),
                ('maker_user', models.ForeignKey(to='base.Profiel', db_column='maker_uid', related_name='+')),
            ],
            options={
                'db_table': 'ketzers',
            },
        ),
        migrations.CreateModel(
            name='KetzerDeelnemer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opmerking', models.CharField(blank=True, max_length=255)),
                ('lid_sinds', models.DateTimeField()),
                ('door_user', models.ForeignKey(to='base.Profiel', db_column='door_uid', related_name='+')),
                ('groep', models.ForeignKey(to='base.Ketzer')),
                ('user', models.ForeignKey(to='base.Profiel', db_column='uid', related_name='+')),
            ],
            options={
                'db_table': 'ketzer_deelnemers',
            },
        ),
        migrations.CreateModel(
            name='Kring',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('naam', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=2)),
                ('familie', models.CharField(max_length=255)),
                ('samenvatting', models.TextField()),
                ('omschrijving', models.TextField(blank=True)),
                ('begin_moment', models.DateTimeField()),
                ('eind_moment', models.DateTimeField(null=True, blank=True)),
                ('keuzelijst', models.CharField(blank=True, max_length=255)),
                ('kring_nummer', models.IntegerField()),
                ('maker_user', models.ForeignKey(to='base.Profiel', db_column='maker_uid', related_name='+')),
            ],
            options={
                'db_table': 'kringen',
            },
        ),
        migrations.CreateModel(
            name='KringLid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opmerking', models.CharField(blank=True, max_length=255)),
                ('lid_sinds', models.DateTimeField()),
                ('door_user', models.ForeignKey(to='base.Profiel', db_column='door_uid', related_name='+')),
                ('groep', models.ForeignKey(to='base.Kring')),
                ('user', models.ForeignKey(to='base.Profiel', db_column='uid', related_name='+')),
            ],
            options={
                'db_table': 'kring_leden',
            },
        ),
        migrations.CreateModel(
            name='Lichting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('naam', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=2)),
                ('familie', models.CharField(max_length=255)),
                ('samenvatting', models.TextField()),
                ('omschrijving', models.TextField(blank=True)),
                ('begin_moment', models.DateTimeField()),
                ('eind_moment', models.DateTimeField(null=True, blank=True)),
                ('keuzelijst', models.CharField(blank=True, max_length=255)),
                ('lidjaar', models.IntegerField(unique=True)),
                ('maker_user', models.ForeignKey(to='base.Profiel', db_column='maker_uid', related_name='+')),
            ],
            options={
                'db_table': 'lichtingen',
            },
        ),
        migrations.CreateModel(
            name='LichtingLid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opmerking', models.CharField(blank=True, max_length=255)),
                ('lid_sinds', models.DateTimeField()),
                ('door_user', models.ForeignKey(to='base.Profiel', db_column='door_uid', related_name='+')),
                ('groep', models.ForeignKey(to='base.Lichting')),
                ('user', models.ForeignKey(to='base.Profiel', db_column='uid', related_name='+')),
            ],
            options={
                'db_table': 'lichting_leden',
            },
        ),
        migrations.CreateModel(
            name='Ondervereniging',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('naam', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=2)),
                ('familie', models.CharField(max_length=255)),
                ('samenvatting', models.TextField()),
                ('omschrijving', models.TextField(blank=True)),
                ('begin_moment', models.DateTimeField()),
                ('eind_moment', models.DateTimeField(null=True, blank=True)),
                ('keuzelijst', models.CharField(blank=True, max_length=255)),
                ('soort', models.CharField(max_length=1)),
                ('maker_user', models.ForeignKey(to='base.Profiel', db_column='maker_uid', related_name='+')),
            ],
            options={
                'db_table': 'onderverenigingen',
            },
        ),
        migrations.CreateModel(
            name='OnderverenigingsLid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opmerking', models.CharField(blank=True, max_length=255)),
                ('lid_sinds', models.DateTimeField()),
                ('door_user', models.ForeignKey(to='base.Profiel', db_column='door_uid', related_name='+')),
                ('groep', models.ForeignKey(to='base.Ondervereniging')),
                ('user', models.ForeignKey(to='base.Profiel', db_column='uid', related_name='+')),
            ],
            options={
                'db_table': 'ondervereniging_leden',
            },
        ),
        migrations.CreateModel(
            name='Verticale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('naam', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=2)),
                ('familie', models.CharField(max_length=255)),
                ('samenvatting', models.TextField()),
                ('omschrijving', models.TextField(blank=True)),
                ('begin_moment', models.DateTimeField()),
                ('eind_moment', models.DateTimeField(null=True, blank=True)),
                ('keuzelijst', models.CharField(blank=True, max_length=255)),
                ('letter', models.CharField(max_length=1, unique=True)),
                ('maker_user', models.ForeignKey(to='base.Profiel', db_column='maker_uid', related_name='+')),
            ],
            options={
                'db_table': 'verticalen',
            },
        ),
        migrations.CreateModel(
            name='VerticaleLid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opmerking', models.CharField(blank=True, max_length=255)),
                ('lid_sinds', models.DateTimeField()),
                ('door_user', models.ForeignKey(to='base.Profiel', db_column='door_uid', related_name='+')),
                ('groep', models.ForeignKey(to='base.Verticale')),
                ('user', models.ForeignKey(to='base.Profiel', db_column='uid', related_name='+')),
            ],
            options={
                'db_table': 'verticale_leden',
            },
        ),
        migrations.CreateModel(
            name='Werkgroep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('naam', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=2)),
                ('familie', models.CharField(max_length=255)),
                ('samenvatting', models.TextField()),
                ('omschrijving', models.TextField(blank=True)),
                ('begin_moment', models.DateTimeField()),
                ('eind_moment', models.DateTimeField(null=True, blank=True)),
                ('keuzelijst', models.CharField(blank=True, max_length=255)),
                ('aanmeld_limiet', models.IntegerField(null=True, blank=True)),
                ('aanmelden_vanaf', models.DateTimeField()),
                ('aanmelden_tot', models.DateTimeField()),
                ('bewerken_tot', models.DateTimeField(null=True, blank=True)),
                ('afmelden_tot', models.DateTimeField(null=True, blank=True)),
                ('maker_user', models.ForeignKey(to='base.Profiel', db_column='maker_uid', related_name='+')),
            ],
            options={
                'db_table': 'werkgroepen',
            },
        ),
        migrations.CreateModel(
            name='WerkgroepDeelnemer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('opmerking', models.CharField(blank=True, max_length=255)),
                ('lid_sinds', models.DateTimeField()),
                ('door_user', models.ForeignKey(to='base.Profiel', db_column='door_uid', related_name='+')),
                ('groep', models.ForeignKey(to='base.Werkgroep')),
                ('user', models.ForeignKey(to='base.Profiel', db_column='uid', related_name='+')),
            ],
            options={
                'db_table': 'werkgroep_deelnemers',
            },
        ),
        migrations.AddField(
            model_name='kring',
            name='verticale',
            field=models.ForeignKey(to='base.Verticale', db_column='verticale'),
        ),
    ]
