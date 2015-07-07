from django.db import models
from base.models import Profiel
from livefield import LiveModel
from datetime import datetime, time

class MaaltijdRepetitie(models.Model):
  id = models.AutoField(primary_key=True, db_column='mlt_repetitie_id')
  dag_vd_week = models.IntegerField()
  periode_in_dagen = models.IntegerField()
  standaard_titel = models.CharField(max_length=255)
  standaard_tijd = models.TimeField(default=time(hour=18))
  standaard_prijs = models.IntegerField(default=300)
  abonneerbaar = models.IntegerField()
  standaard_limiet = models.IntegerField(default=100)
  abonnement_filter = models.CharField(max_length=255, blank=True)

  def __str__(self):
    return "Repetitie: %s" % self.standaard_titel

  class Meta:
    db_table = 'mlt_repetities'

class Maaltijd(LiveModel):
  # fields
  id = models.AutoField(primary_key=True, db_column="maaltijd_id")
  repetitie = models.ForeignKey(MaaltijdRepetitie, blank=True, null=True, db_column="mlt_repetitie_id")
  titel = models.CharField(max_length=255)
  datum = models.DateField()
  tijd = models.TimeField(default=time(hour=18))
  prijs = models.IntegerField(default=300)
  omschrijving = models.CharField(max_length=255, blank=True)

  gesloten = models.BooleanField(default=False)
  laatst_gesloten = models.DateTimeField(blank=True, null=True)

  aanmeld_filter = models.CharField(max_length=255, blank=True) # permissions specifier
  aanmeld_limiet = models.IntegerField(default=100)

  def __str__(self):
    return "Maaltijd: %s" % self.titel

  class Meta:
    db_table = 'mlt_maaltijden'

class MaaltijdAanmelding(models.Model):
  maaltijd = models.ForeignKey(Maaltijd, related_name="aanmeldingen")
  user = models.ForeignKey(Profiel, db_column='uid')
  aantal_gasten = models.IntegerField()
  gasten_eetwens = models.CharField(max_length=255, blank=True)

  door_abonnement = models.ForeignKey(MaaltijdRepetitie, db_column='door_abonnement', blank=True, null=True)
  door_user = models.ForeignKey(Profiel, null=True, db_column='door_uid', related_name='+')
  laatst_gewijzigd = models.DateTimeField()

  def __str__(self):
    return "Aanmelding: lid %s bij %s" % (self.user_id, self.maaltijd_id)

  class Meta:
    unique_together = (('maaltijd', 'user'),)
    db_table = 'mlt_aanmeldingen'

class MaaltijdAbo(models.Model):
  repetitie = models.ForeignKey(MaaltijdRepetitie, db_column="mlt_repetitie_id")
  user = models.ForeignKey(Profiel, db_column='uid')
  wanneer_ingeschakeld = models.DateTimeField()

  def __str__(self):
    return "Abo voor lid %s bij repetitie %s" % (self.user_id, self.repetitie_id)
  class Meta:
    unique_together = (('user', 'repetitie'))
    db_table = 'mlt_abonnementen'
