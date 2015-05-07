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
                ('categorie', models.ForeignKey(db_column='categorie_id', to='forum.ForumCategorie')),
            ],
            options={
                'db_table': 'forum_delen',
            },
        ),
        migrations.CreateModel(
            name='ForumDraad',
            fields=[
                ('draad_id', models.AutoField(serialize=False, primary_key=True)),
                ('gedeeld_met', models.IntegerField(blank=True, null=True)),
                ('titel', models.CharField(max_length=255)),
                ('datum_tijd', models.DateTimeField()),
                ('laatst_gewijzigd', models.DateTimeField(blank=True, null=True)),
                ('laatste_post_id', models.IntegerField(blank=True, null=True)),
                ('belangrijk', models.CharField(blank=True, max_length=255)),
                ('gesloten', models.IntegerField()),
                ('verwijderd', models.IntegerField()),
                ('wacht_goedkeuring', models.IntegerField()),
                ('plakkerig', models.IntegerField()),
                ('eerste_post_plakkerig', models.IntegerField()),
                ('pagina_per_post', models.IntegerField()),
                ('forum', models.ForeignKey(db_column='forum_id', to='forum.ForumDeel')),
                ('laatste_wijziging_user', models.ForeignKey(db_column='laatste_wijziging_uid', related_name='+', blank=True, to='base.Profiel')),
                ('user', models.ForeignKey(db_column='uid', to='base.Profiel')),
            ],
            options={
                'db_table': 'forum_draden',
            },
        ),
        migrations.CreateModel(
            name='ForumDraadGelezen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_tijd', models.DateTimeField()),
                ('draad', models.ForeignKey(db_column='draad_id', to='forum.ForumDraad')),
                ('user', models.ForeignKey(db_column='uid', to='base.Profiel')),
            ],
            options={
                'db_table': 'forum_draden_gelezen',
            },
        ),
        migrations.CreateModel(
            name='ForumDraadReageren',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('datum_tijd', models.DateTimeField()),
                ('concept', models.TextField(blank=True)),
                ('titel', models.CharField(blank=True, max_length=255)),
                ('draad', models.ForeignKey(db_column='draad_id', to='forum.ForumDraad')),
                ('forum', models.ForeignKey(db_column='forum_id', to='forum.ForumDeel')),
                ('user', models.ForeignKey(db_column='uid', to='base.Profiel')),
            ],
            options={
                'db_table': 'forum_draden_reageren',
            },
        ),
        migrations.CreateModel(
            name='ForumDraadVerbergen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('draad', models.ForeignKey(db_column='draad_id', to='forum.ForumDraad')),
                ('user', models.ForeignKey(db_column='uid', to='base.Profiel')),
            ],
            options={
                'db_table': 'forum_draden_verbergen',
            },
        ),
        migrations.CreateModel(
            name='ForumDraadVolgen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('draad', models.ForeignKey(db_column='draad_id', to='forum.ForumDraad')),
                ('user', models.ForeignKey(db_column='uid', to='base.Profiel')),
            ],
            options={
                'db_table': 'forum_draden_volgen',
            },
        ),
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('post_id', models.AutoField(serialize=False, primary_key=True)),
                ('tekst', models.TextField()),
                ('datum_tijd', models.DateTimeField()),
                ('laatst_gewijzigd', models.DateTimeField()),
                ('bewerkt_tekst', models.TextField(blank=True)),
                ('verwijderd', models.IntegerField()),
                ('auteur_ip', models.CharField(max_length=255)),
                ('wacht_goedkeuring', models.IntegerField()),
                ('draad', models.ForeignKey(db_column='draad_id', to='forum.ForumDraad')),
                ('user', models.ForeignKey(db_column='uid', to='base.Profiel')),
            ],
            options={
                'db_table': 'forum_posts',
            },
        ),
        migrations.AlterUniqueTogether(
            name='forumdraadvolgen',
            unique_together=set([('draad', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='forumdraadverbergen',
            unique_together=set([('draad', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='forumdraadreageren',
            unique_together=set([('forum', 'draad', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='forumdraadgelezen',
            unique_together=set([('draad', 'user')]),
        ),
    ]
