from datetime import datetime
from django.db import models
from django.db.models import Q
from livefield import LiveModel
from base.models import Profiel
from base.utils import Choices

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
  plaatje = models.CharField(max_length=255)

  AUDIENCE = Choices(
    PUBLIC="PUB",
    LEDEN="LID",
    OUDLEDEN="OUD"
  )
  audience = models.CharField(max_length=3, choices=AUDIENCE.choices(), default=AUDIENCE.LEDEN)

  @classmethod
  def get_viewable_by(cls, user):
    """ Find all announcements viewable by the given user.
        Permissions are granted in the publiek < oudlid < lid hierarchy
    """
    q = Q(audience=cls.AUDIENCE.PUBLIC)

    # authenticated users see more
    if user.is_authenticated():
      # ... depending on there status
      status = user.profiel.status
      if status == Profiel.STATUS.OUDLID or status == Profiel.STATUS.LID:
        q |= Q(audience=cls.AUDIENCE.OUDLEDEN)
      if status == Profiel.STATUS.LID:
        q |= Q(audience=cls.AUDIENCE.LID)

    return cls.objects.filter(q)

  def __str__(self):
    return "Mededeling: %s" % self.titel
