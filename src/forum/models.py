from django.db import models
from base.models import Profiel
from livefield import LiveModel

class ForumCategorie(models.Model):
  categorie_id = models.AutoField(primary_key=True)
  titel = models.CharField(max_length=255)
  rechten_lezen = models.CharField(max_length=255)
  volgorde = models.IntegerField()

  def __str__(self):
    return self.titel

  class Meta:
    db_table = 'forum_categorien'

class ForumDeel(models.Model):
  forum_id = models.AutoField(primary_key=True)
  categorie = models.ForeignKey(ForumCategorie, db_column="categorie_id")
  titel = models.CharField(max_length=255)
  omschrijving = models.TextField()
  rechten_lezen = models.CharField(max_length=255)
  rechten_posten = models.CharField(max_length=255)
  rechten_modereren = models.CharField(max_length=255)
  volgorde = models.IntegerField()

  @classmethod
  def get_viewable_by(cls, user, qs=None):
    if qs is None:
      qs = cls.objects.all()

    return filter(
      lambda d: user.has_perm('forum.view_forumdeel', d),
      qs.prefetch_related('categorie'))

  def __str__(self):
    return self.titel

  class Meta:
    db_table = 'forum_delen'
    default_permissions = ('add', 'change', 'delete', 'moderate', 'post_in')

class ForumDraad(LiveModel):

  draad_id = models.AutoField(primary_key=True)
  forum = models.ForeignKey(ForumDeel, db_column="forum_id", related_name="draden")
  gedeeld_met = models.IntegerField(blank=True, null=True)
  user = models.ForeignKey(Profiel, db_column='uid')
  titel = models.CharField(max_length=255)
  datum_tijd = models.DateTimeField()
  belangrijk = models.CharField(max_length=255, blank=True)
  gesloten = models.BooleanField(default=False)
  wacht_goedkeuring = models.IntegerField(default=False)
  plakkerig = models.IntegerField(default=False)

  # TODO freeze this to true and delete the field
  eerste_post_plakkerig = models.IntegerField(default=True)

  # keep this here to prevent expensive MAX(..) sql queries
  # because we use the last post in the forum overview all the time
  laatste_post = models.ForeignKey("ForumPost", blank=True, null=True)

  def __str__(self):
    return self.titel

  class Meta:
    db_table = 'forum_draden'

class ForumDraadGelezen(models.Model):
  id = models.AutoField(primary_key=True)
  draad = models.ForeignKey(ForumDraad, db_column="draad_id")
  user = models.ForeignKey(Profiel, db_column='uid')
  datum_tijd = models.DateTimeField()

  def __str__(self):
    return "draad %s gelezen door %s" % (self.draad_id, self.uid_id)

  class Meta:
    db_table = 'forum_draden_gelezen'
    unique_together = (('draad', 'user'),)

class ForumDraadReageren(models.Model):
  id = models.AutoField(primary_key=True)
  forum = models.ForeignKey(ForumDeel, db_column="forum_id")
  draad = models.ForeignKey(ForumDraad, db_column="draad_id")
  user = models.ForeignKey(Profiel, db_column='uid')
  datum_tijd = models.DateTimeField()
  concept = models.TextField(blank=True)
  titel = models.CharField(max_length=255, blank=True)

  def __str__(self):
    return "forum %s draad %s gelezen door %s" % (self.forum_id, self.draad_id, self.uid_id)

  class Meta:
    db_table = 'forum_draden_reageren'
    unique_together = (('forum', 'draad', 'user'),)

class ForumDraadVerbergen(models.Model):
  id = models.AutoField(primary_key=True)
  draad = models.ForeignKey(ForumDraad, db_column="draad_id")
  user = models.ForeignKey(Profiel, db_column='uid')

  def __str__(self):
    return "draad %s verbergen voor %s" % (self.draad_id, self.uid_id)

  class Meta:
    unique_together = (('draad', 'user'),)
    db_table = 'forum_draden_verbergen'

class ForumDraadVolgen(models.Model):
  id = models.AutoField(primary_key=True)
  draad = models.ForeignKey(ForumDraad, db_column="draad_id", related_name="subscribers")
  user = models.ForeignKey(Profiel, db_column='uid')

  def __str__(self):
    return "draad %s gevolgd door %s" % (self.draad_id, self.uid_id)

  class Meta:
    unique_together = (('draad', 'user'),)
    db_table = 'forum_draden_volgen'

class ForumPost(LiveModel):
  post_id = models.AutoField(primary_key=True)
  draad = models.ForeignKey(ForumDraad, db_column="draad_id", related_name='posts')
  user = models.ForeignKey(Profiel, db_column='uid')
  tekst = models.TextField()
  datum_tijd = models.DateTimeField()
  laatst_gewijzigd = models.DateTimeField()
  bewerkt_tekst = models.TextField(blank=True)
  auteur_ip = models.CharField(max_length=255, blank=True)
  wacht_goedkeuring = models.BooleanField(default=False)

  def __str__(self):
    return self.tekst[:50]

  class Meta:
    db_table = 'forum_posts'
