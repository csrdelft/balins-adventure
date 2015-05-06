# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumCategorie',
            fields=[
                ('categorie_id', models.AutoField(serialize=False, primary_key=True)),
                ('titel', models.CharField(max_length=255)),
                ('rechten_lezen', models.CharField(max_length=255)),
                ('volgorde', models.IntegerField()),
            ],
            options={
                'db_table': 'forum_categorien',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ForumDeel',
            fields=[
                ('forum_id', models.AutoField(serialize=False, primary_key=True)),
                ('titel', models.CharField(max_length=255)),
                ('omschrijving', models.TextField()),
                ('rechten_lezen', models.CharField(max_length=255)),
                ('rechten_posten', models.CharField(max_length=255)),
                ('rechten_modereren', models.CharField(max_length=255)),
                ('volgorde', models.IntegerField()),
                ('categorie', models.ForeignKey(to='forum.ForumCategorie', db_column='categorie_id')),
            ],
            options={
                'db_table': 'forum_delen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ForumDraad',
            fields=[
                ('draad_id', models.AutoField(serialize=False, primary_key=True)),
                ('forum_id', models.IntegerField()),
                ('gedeeld_met', models.IntegerField(blank=True, null=True)),
                ('titel', models.CharField(max_length=255)),
                ('datum_tijd', models.DateTimeField()),
                ('laatst_gewijzigd', models.DateTimeField(blank=True, null=True)),
                ('laatste_post_id', models.IntegerField(blank=True, null=True)),
                ('belangrijk', models.CharField(max_length=255, blank=True)),
                ('gesloten', models.IntegerField()),
                ('verwijderd', models.IntegerField()),
                ('wacht_goedkeuring', models.IntegerField()),
                ('plakkerig', models.IntegerField()),
                ('eerste_post_plakkerig', models.IntegerField()),
                ('pagina_per_post', models.IntegerField()),
                ('laatste_wijziging_uid', models.ForeignKey(to='base.Profiel', related_name='+', blank=True, db_column='laatste_wijziging_uid')),
                ('uid', models.ForeignKey(to='base.Profiel', db_column='uid')),
            ],
            options={
                'db_table': 'forum_draden',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ForumDraadGelezen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('draad_id', models.IntegerField()),
                ('datum_tijd', models.DateTimeField()),
                ('uid', models.ForeignKey(to='base.Profiel', db_column='uid')),
            ],
            options={
                'db_table': 'forum_draden_gelezen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ForumDraadReageren',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('forum_id', models.IntegerField()),
                ('draad_id', models.IntegerField()),
                ('datum_tijd', models.DateTimeField()),
                ('concept', models.TextField(blank=True)),
                ('titel', models.CharField(max_length=255, blank=True)),
                ('uid', models.ForeignKey(to='base.Profiel', db_column='uid')),
            ],
            options={
                'db_table': 'forum_draden_reageren',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ForumDraadVerbergen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('draad_id', models.IntegerField()),
                ('uid', models.ForeignKey(to='base.Profiel', db_column='uid')),
            ],
            options={
                'db_table': 'forum_draden_verbergen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ForumDraadVolgen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('draad_id', models.IntegerField()),
                ('uid', models.ForeignKey(to='base.Profiel', db_column='uid')),
            ],
            options={
                'db_table': 'forum_draden_volgen',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('post_id', models.AutoField(serialize=False, primary_key=True)),
                ('draad_id', models.IntegerField()),
                ('tekst', models.TextField()),
                ('datum_tijd', models.DateTimeField()),
                ('laatst_gewijzigd', models.DateTimeField()),
                ('bewerkt_tekst', models.TextField(blank=True)),
                ('verwijderd', models.IntegerField()),
                ('auteur_ip', models.CharField(max_length=255)),
                ('wacht_goedkeuring', models.IntegerField()),
                ('uid', models.ForeignKey(to='base.Profiel', db_column='uid')),
            ],
            options={
                'db_table': 'forum_posts',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='forumdraadvolgen',
            unique_together=set([('draad_id', 'uid')]),
        ),
        migrations.AlterUniqueTogether(
            name='forumdraadverbergen',
            unique_together=set([('draad_id', 'uid')]),
        ),
        migrations.AlterUniqueTogether(
            name='forumdraadreageren',
            unique_together=set([('forum_id', 'draad_id', 'uid')]),
        ),
        migrations.AlterUniqueTogether(
            name='forumdraadgelezen',
            unique_together=set([('draad_id', 'uid')]),
        ),
    ]
