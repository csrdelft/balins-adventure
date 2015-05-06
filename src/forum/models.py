from django.db.models import *
from base.models import Profiel

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

  def __str__(self):
    return self.titel

  class Meta:
    db_table = 'forum_delen'

class ForumDraad(Model):
  draad_id = AutoField(primary_key=True)
  forum_id = IntegerField()
  gedeeld_met = IntegerField(blank=True, null=True)
  uid = ForeignKey(Profiel, db_column='uid')
  titel = CharField(max_length=255)
  datum_tijd = DateTimeField()
  laatst_gewijzigd = DateTimeField(blank=True, null=True)
  laatste_post_id = IntegerField(blank=True, null=True)
  laatste_wijziging_uid = ForeignKey(Profiel, blank=True, related_name='+', db_column="laatste_wijziging_uid")
  belangrijk = CharField(max_length=255, blank=True)
  gesloten = IntegerField()
  verwijderd = IntegerField()
  wacht_goedkeuring = IntegerField()
  plakkerig = IntegerField()
  eerste_post_plakkerig = IntegerField()
  pagina_per_post = IntegerField()

  def __str__(self):
    return self.titel

  class Meta:
    db_table = 'forum_draden'

class ForumDraadGelezen(Model):
  id = AutoField(primary_key=True)
  draad_id = IntegerField()
  uid = ForeignKey(Profiel, db_column='uid')
  datum_tijd = DateTimeField()

  def __str__(self):
    return "draad %s gelezen door %s" % (self.draad_id, self.uid_id)

  class Meta:
    db_table = 'forum_draden_gelezen'
    unique_together = (('draad_id', 'uid'),)

class ForumDraadReageren(Model):
  id = AutoField(primary_key=True)
  forum_id = IntegerField()
  draad_id = IntegerField()
  uid = ForeignKey(Profiel, db_column='uid')
  datum_tijd = DateTimeField()
  concept = TextField(blank=True)
  titel = CharField(max_length=255, blank=True)

  def __str__(self):
    return "forum %s draad %s gelezen door %s" % (self.forum_id, self.draad_id, self.uid_id)

  class Meta:
    db_table = 'forum_draden_reageren'
    unique_together = (('forum_id', 'draad_id', 'uid'),)

class ForumDraadVerbergen(Model):
  id = AutoField(primary_key=True)
  draad_id = IntegerField()
  uid = ForeignKey(Profiel, db_column='uid')

  def __str__(self):
    return "draad %s verbergen voor %s" % (self.draad_id, self.uid_id)

  class Meta:
    unique_together = (('draad_id', 'uid'),)
    db_table = 'forum_draden_verbergen'

class ForumDraadVolgen(Model):
  id = AutoField(primary_key=True)
  draad_id = IntegerField()
  uid = ForeignKey(Profiel, db_column='uid')

  def __str__(self):
    return "draad %s gevolgd door %s" % (self.draad_id, self.uid_id)

  class Meta:
    unique_together = (('draad_id', 'uid'),)
    db_table = 'forum_draden_volgen'

class ForumPost(Model):
  post_id = AutoField(primary_key=True)
  draad_id = IntegerField()
  uid = ForeignKey(Profiel, db_column='uid')
  tekst = TextField()
  datum_tijd = DateTimeField()
  laatst_gewijzigd = DateTimeField()
  bewerkt_tekst = TextField(blank=True)
  verwijderd = IntegerField()
  auteur_ip = CharField(max_length=255)
  wacht_goedkeuring = IntegerField()

  def __str__(self):
    return self.tekst[:50]

  class Meta:
    db_table = 'forum_posts'
