from django.db.models import *
from base.models import Profiel
from livefield import LiveModel

class ForumCategorie(Model):
  categorie_id = AutoField(primary_key=True)
  titel = CharField(max_length=255)
  rechten_lezen = CharField(max_length=255)
  volgorde = IntegerField()

  def __str__(self):
    return self.titel

  class Meta:
    db_table = 'forum_categorien'

class ForumDeel(Model):
  forum_id = AutoField(primary_key=True)
  categorie = ForeignKey(ForumCategorie, db_column="categorie_id")
  titel = CharField(max_length=255)
  omschrijving = TextField()
  rechten_lezen = CharField(max_length=255)
  rechten_posten = CharField(max_length=255)
  rechten_modereren = CharField(max_length=255)
  volgorde = IntegerField()

  @classmethod
  def get_viewable_by(cls, user):
    return filter(
      lambda d: user.has_perm('forum.view_forumdeel', d),
      cls.objects.all().prefetch_related('categorie'))

  def __str__(self):
    return self.titel

  class Meta:
    db_table = 'forum_delen'
    default_permissions = ('add', 'change', 'delete', 'moderate', 'post_in')

class ForumDraad(LiveModel):

  draad_id = AutoField(primary_key=True)
  forum = ForeignKey(ForumDeel, db_column="forum_id")
  gedeeld_met = IntegerField(blank=True, null=True)
  user = ForeignKey(Profiel, db_column='uid')
  titel = CharField(max_length=255)
  datum_tijd = DateTimeField()
  belangrijk = CharField(max_length=255, blank=True)
  gesloten = BooleanField(default=False)
  wacht_goedkeuring = IntegerField(default=False)
  plakkerig = IntegerField(default=False)
  eerste_post_plakkerig = IntegerField(default=True)

  laatst_gewijzigd = DateTimeField(blank=True, null=True)
  laatste_wijziging_user = ForeignKey(Profiel, blank=True, related_name='+', db_column="laatste_wijziging_uid")

  # TODO verwijderen? anders in services opnemen
  laatste_post_id = IntegerField(blank=True, null=True)
  pagina_per_post = IntegerField()

  # reverse relations:
  #   - subscribers (ForumDraadVolgen)

  def __str__(self):
    return self.titel

  class Meta:
    db_table = 'forum_draden'

class ForumDraadGelezen(Model):
  id = AutoField(primary_key=True)
  draad = ForeignKey(ForumDraad, db_column="draad_id")
  user = ForeignKey(Profiel, db_column='uid')
  datum_tijd = DateTimeField()

  def __str__(self):
    return "draad %s gelezen door %s" % (self.draad_id, self.uid_id)

  class Meta:
    db_table = 'forum_draden_gelezen'
    unique_together = (('draad', 'user'),)

class ForumDraadReageren(Model):
  id = AutoField(primary_key=True)
  forum = ForeignKey(ForumDeel, db_column="forum_id")
  draad = ForeignKey(ForumDraad, db_column="draad_id")
  user = ForeignKey(Profiel, db_column='uid')
  datum_tijd = DateTimeField()
  concept = TextField(blank=True)
  titel = CharField(max_length=255, blank=True)

  def __str__(self):
    return "forum %s draad %s gelezen door %s" % (self.forum_id, self.draad_id, self.uid_id)

  class Meta:
    db_table = 'forum_draden_reageren'
    unique_together = (('forum', 'draad', 'user'),)

class ForumDraadVerbergen(Model):
  id = AutoField(primary_key=True)
  draad = ForeignKey(ForumDraad, db_column="draad_id")
  user = ForeignKey(Profiel, db_column='uid')

  def __str__(self):
    return "draad %s verbergen voor %s" % (self.draad_id, self.uid_id)

  class Meta:
    unique_together = (('draad', 'user'),)
    db_table = 'forum_draden_verbergen'

class ForumDraadVolgen(Model):
  id = AutoField(primary_key=True)
  draad = ForeignKey(ForumDraad, db_column="draad_id", related_name="subscribers")
  user = ForeignKey(Profiel, db_column='uid')

  def __str__(self):
    return "draad %s gevolgd door %s" % (self.draad_id, self.uid_id)

  class Meta:
    unique_together = (('draad', 'user'),)
    db_table = 'forum_draden_volgen'

class ForumPost(LiveModel):
  post_id = AutoField(primary_key=True)
  draad = ForeignKey(ForumDraad, db_column="draad_id", related_name='posts')
  user = ForeignKey(Profiel, db_column='uid')
  tekst = TextField()
  datum_tijd = DateTimeField()
  laatst_gewijzigd = DateTimeField()
  bewerkt_tekst = TextField(blank=True)
  auteur_ip = CharField(max_length=255, blank=True)
  wacht_goedkeuring = BooleanField(default=False)

  def __str__(self):
    return self.tekst[:50]

  class Meta:
    db_table = 'forum_posts'
