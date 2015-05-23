# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_migration_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activiteit',
            name='begin_moment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='omschrijving',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activiteit',
            name='samenvatting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activiteitdeelnemer',
            name='groep',
            field=models.ForeignKey(related_name='leden', to='base.Activiteit'),
        ),
        migrations.AlterField(
            model_name='bestuur',
            name='begin_moment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bestuur',
            name='omschrijving',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bestuur',
            name='samenvatting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bestuurslid',
            name='groep',
            field=models.ForeignKey(related_name='leden', to='base.Bestuur'),
        ),
        migrations.AlterField(
            model_name='commissie',
            name='begin_moment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commissie',
            name='omschrijving',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commissie',
            name='samenvatting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commissielid',
            name='groep',
            field=models.ForeignKey(related_name='leden', to='base.Commissie'),
        ),
        migrations.AlterField(
            model_name='groep',
            name='begin_moment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='groep',
            name='omschrijving',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='groep',
            name='samenvatting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='groepleden',
            name='groep',
            field=models.ForeignKey(related_name='leden', to='base.Groep'),
        ),
        migrations.AlterField(
            model_name='ketzer',
            name='begin_moment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ketzer',
            name='omschrijving',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ketzer',
            name='samenvatting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ketzerdeelnemer',
            name='groep',
            field=models.ForeignKey(related_name='leden', to='base.Ketzer'),
        ),
        migrations.AlterField(
            model_name='kring',
            name='begin_moment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kring',
            name='omschrijving',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kring',
            name='samenvatting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kringlid',
            name='groep',
            field=models.ForeignKey(related_name='leden', to='base.Kring'),
        ),
        migrations.AlterField(
            model_name='lichting',
            name='begin_moment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lichting',
            name='omschrijving',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lichting',
            name='samenvatting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lichtinglid',
            name='groep',
            field=models.ForeignKey(related_name='leden', to='base.Lichting'),
        ),
        migrations.AlterField(
            model_name='ondervereniging',
            name='begin_moment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ondervereniging',
            name='omschrijving',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ondervereniging',
            name='samenvatting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='onderverenigingslid',
            name='groep',
            field=models.ForeignKey(related_name='leden', to='base.Ondervereniging'),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='adresseringechtpaar',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='bankrekening',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='beroep',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='changelog',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='duckname',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='eetwens',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='icq',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='jid',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='kerk',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='kgb',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='land',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='linkedin',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='medisch',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='middelbareschool',
            field=models.CharField(db_column='middelbareSchool', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='mobiel',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='msn',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='muziek',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='novietsoort',
            field=models.CharField(db_column='novietSoort', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='novitiaatbijz',
            field=models.TextField(db_column='novitiaatBijz', blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='o_adres',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='o_land',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='o_postcode',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='o_telefoon',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='o_woonplaats',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='postfix',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='skype',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='startkamp',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='studie',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='telefoon',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='tussenvoegsel',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='website',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='verticale',
            name='begin_moment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='verticale',
            name='omschrijving',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='verticale',
            name='samenvatting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='verticalelid',
            name='groep',
            field=models.ForeignKey(related_name='leden', to='base.Verticale'),
        ),
        migrations.AlterField(
            model_name='werkgroep',
            name='begin_moment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='werkgroep',
            name='omschrijving',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='werkgroep',
            name='samenvatting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='werkgroepdeelnemer',
            name='groep',
            field=models.ForeignKey(related_name='leden', to='base.Werkgroep'),
        ),
    ]
