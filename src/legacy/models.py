from django.db.models import *

class LegacyProfiel(Model):

  class Meta:
    db_table = 'profielen'

  uid = CharField(primary_key=True, max_length=4)
  nickname = CharField(max_length=255)
  duckname = CharField(max_length=255)
  voornaam = CharField(max_length=255)
  tussenvoegsel = CharField(max_length=255)
  achternaam = CharField(max_length=255)
  voorletters = CharField(max_length=255)
  postfix = CharField(max_length=255)
  adres = CharField(max_length=255)
  postcode = CharField(max_length=255)
  woonplaats = CharField(max_length=255)
  land = CharField(max_length=255)
  telefoon = CharField(max_length=255)
  mobiel = CharField(max_length=255)
  geslacht = CharField(max_length=1)
  voornamen = CharField(max_length=255)
  echtgenoot = CharField(max_length=4, blank=True)
  adresseringechtpaar = CharField(max_length=255)
  icq = CharField(max_length=255)
  msn = CharField(max_length=255)
  skype = CharField(max_length=255)
  jid = CharField(max_length=255)
  linkedin = CharField(max_length=255)
  website = CharField(max_length=255)
  beroep = CharField(max_length=255)
  studie = CharField(max_length=255)
  patroon = CharField(max_length=4, blank=True)
  studienr = IntegerField(blank=True, null=True)
  studiejaar = IntegerField(blank=True, null=True)
  lidjaar = IntegerField()
  lidafdatum = DateField(blank=True, null=True)
  gebdatum = DateField()
  sterfdatum = DateField(blank=True, null=True)
  bankrekening = CharField(max_length=255)
  machtiging = IntegerField()
  moot = CharField(max_length=1)
  verticale = CharField(max_length=1)
  verticaleleider = IntegerField()
  kringcoach = CharField(max_length=1, blank=True)
  o_adres = CharField(max_length=255)
  o_postcode = CharField(max_length=255)
  o_woonplaats = CharField(max_length=255)
  o_land = CharField(max_length=255)
  o_telefoon = CharField(max_length=255)
  email = CharField(max_length=255)
  kerk = CharField(max_length=255)
  muziek = CharField(max_length=255)
  status = CharField(max_length=11)
  eetwens = CharField(max_length=255)
  corvee_punten = IntegerField()
  corvee_punten_bonus = IntegerField()
  ontvangtcontactueel = CharField(max_length=8)
  kgb = TextField()
  soccieid = IntegerField(db_column='soccieID')  # Field name made lowercase.
  createterm = CharField(db_column='createTerm', max_length=255)  # Field name made lowercase.
  socciesaldo = FloatField(db_column='soccieSaldo')  # Field name made lowercase.
  maalciesaldo = FloatField(db_column='maalcieSaldo')  # Field name made lowercase.
  changelog = TextField()
  ovkaart = CharField(max_length=255)
  zingen = CharField(max_length=255)
  novitiaat = TextField()
  lengte = IntegerField()
  vrienden = TextField()
  middelbareschool = CharField(db_column='middelbareSchool', max_length=255)  # Field name made lowercase.
  novietsoort = CharField(db_column='novietSoort', max_length=255)  # Field name made lowercase.
  matrixplek = CharField(db_column='matrixPlek', max_length=255)  # Field name made lowercase.
  startkamp = CharField(max_length=255)
  medisch = TextField()
  novitiaatbijz = TextField(db_column='novitiaatBijz')  # Field name made lowercase.

  def __str__(self):
    return "%s (%s)" % (self.formal_name(), self.uid)

  def formal_name(self):
    if self.geslacht == 'm':
      return "Am. %s" % self.achternaam
    else:
      return "Ama. %s" % self.achternaam

class Accounts(Model):
  uid = CharField(max_length=4, primary_key=True)
  username = CharField(unique=True, max_length=255)
  email = CharField(max_length=255)
  pass_hash = CharField(max_length=255)
  pass_since = DateTimeField()
  last_login_success = DateTimeField(blank=True, null=True)
  last_login_attempt = DateTimeField(blank=True, null=True)
  failed_login_attempts = IntegerField()
  blocked_reason = TextField(blank=True)
  perm_role = CharField(max_length=9)
  private_token = CharField(max_length=255, blank=True)
  private_token_since = DateTimeField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'accounts'

