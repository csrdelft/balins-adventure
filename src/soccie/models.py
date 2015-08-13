from django.db import models

from base.models import Profiel

class SoccieBestelling(models.Model):
  soccieid = models.IntegerField(db_column='socCieId', blank=True, null=True)
  totaal = models.IntegerField(blank=True, null=True)
  tijd = models.DateTimeField(blank=True, null=True)
  deleted = models.IntegerField()

  class Meta:
    db_table = 'socCieBestelling'

class SoccieBestellingInhoud(models.Model):
  bestellingid = models.ForeignKey(SoccieBestelling, db_column='bestellingId')
  productid = models.ForeignKey("SoccieProduct", db_column='productId')
  aantal = models.IntegerField(blank=True, null=True)

  class Meta:
    db_table = 'socCieBestellingInhoud'

class SoccieGrootboekType(models.Model):
  type = models.CharField(max_length=255)

  class Meta:
    db_table = 'socCieGrootboekType'

class SoccieKlanten(models.Model):
  soccieid = models.IntegerField(db_column='socCieId', primary_key=True)
  stekuid = models.ForeignKey(Profiel, db_column='stekUID', blank=True)
  saldo = models.IntegerField(blank=True, null=True)
  naam = models.TextField(blank=True)
  deleted = models.IntegerField()

  class Meta:
    db_table = 'socCieKlanten'

class SoccieLog(models.Model):
  ip = models.CharField(max_length=15)
  type = models.CharField(max_length=6)
  value = models.TextField()
  timestamp = models.DateTimeField()

  class Meta:
    db_table = 'socCieLog'

class SocciePrijs(models.Model):
  van = models.DateTimeField()
  tot = models.DateTimeField()
  productid = models.ForeignKey("SoccieProduct", db_column='productId')
  prijs = models.IntegerField()

  class Meta:
    db_table = 'socCiePrijs'

class SoccieProduct(models.Model):
  status = models.IntegerField(blank=True, null=True)
  beschrijving = models.TextField(blank=True)
  prioriteit = models.IntegerField()
  grootboekid = models.ForeignKey(SoccieGrootboekType, db_column='grootboekId')
  beheer = models.IntegerField()

  class Meta:
    db_table = 'socCieProduct'
