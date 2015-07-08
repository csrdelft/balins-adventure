from datetime import datetime
from django.db import models
from django.db.models import Q
from livefield import LiveModel
from base.models import Profiel

class Mededeling(LiveModel):

  class Meta:
    db_table = 'mededeling'

  datum = models.DateTimeField(default=datetime.now)
  vervaltijd = models.DateTimeField(blank=True, null=True)
  titel = models.TextField()
  tekst = models.TextField()
  prive = models.CharField(max_length=1)
  prioriteit = models.IntegerField()
  user = models.ForeignKey(Profiel, max_length=4, db_column="uid")
  doelgroep = models.CharField(max_length=10)
  plaatje = models.CharField(max_length=255)

  @classmethod
  def get_viewable_by(cls, user):
    #Filter to find public announcements
    #Return only public or both public and 'doelgroep' for user within 'doelgroep'

    public_filter = cls.objects.filter(Q(doelgroep='PUBLIEK'))
    if not user.is_authenticated():
      return public_filter
    else:
      return public_filter | cls.objects.filter(Q(doelgroep=user.profiel.status))

  def __str__(self):
    return "Mededeling: %s" % self.titel
