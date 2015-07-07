import datetime
from django.db import models
from livefield import LiveModel
from base.models import Profiel

class Mededeling(LiveModel):
  datum = models.DateTimeField(default=datetime.date.today)
  vervaltijd = models.DateTimeField(blank=True, null=True)
  titel = models.TextField()
  tekst = models.TextField()
  prive = models.CharField(max_length=1)
  prioriteit = models.IntegerField()
  user = models.ForeignKey(Profiel, max_length=4, db_column="uid")
  doelgroep = models.CharField(max_length=10)
  plaatje = models.CharField(max_length=255)

  #READ Permissions

  class Meta:
    db_table = 'mededeling'

  def __str__(self):
    return "Mededeling: %s" % self.titel