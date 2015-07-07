from django.db import models
from base.models import Profiel


class Mededeling(models.Model):
  datum = models.DateTimeField(blank=True, null=True)
  vervaltijd = models.DateTimeField(blank=True, null=True)
  titel = models.TextField()
  tekst = models.TextField()
  prive = models.CharField(max_length=1)
  prioriteit = models.IntegerField()
  user = models.ForeignKey(Profiel, max_length=4, db_column="uid")
  doelgroep = models.CharField(max_length=10)
  verborgen = models.CharField(max_length=1)
  verwijderd = models.CharField(max_length=1)
  plaatje = models.CharField(max_length=255)

  #READ Permissions

  class Meta:
    db_table = 'mededeling'