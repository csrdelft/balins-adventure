from django.db.models import *
from django.contrib.auth.models import User

class Profiel(Model):
  class Meta:
    db_table = 'profielen'

  user = OneToOneField(User, null=True)
  uid = CharField(primary_key=True, max_length=4)

  nickname = CharField(max_length=255)
  duckname = CharField(max_length=255, blank=True)
  voornaam = CharField(max_length=255)
  tussenvoegsel = CharField(max_length=255, blank=True)
  achternaam = CharField(max_length=255)
  voorletters = CharField(max_length=255)
  postfix = CharField(max_length=255, blank=True)
  adres = CharField(max_length=255)
  postcode = CharField(max_length=255)
  woonplaats = CharField(max_length=255)
  land = CharField(max_length=255, blank=True)
  telefoon = CharField(max_length=255, blank=True)
  mobiel = CharField(max_length=255, blank=True)
  geslacht = CharField(max_length=1)
  voornamen = CharField(max_length=255)
  echtgenoot = CharField(max_length=4, blank=True)
  adresseringechtpaar = CharField(max_length=255, blank=True)
  icq = CharField(max_length=255, blank=True)
  msn = CharField(max_length=255, blank=True)
  skype = CharField(max_length=255, blank=True)
  jid = CharField(max_length=255, blank=True)
  linkedin = CharField(max_length=255, blank=True)
  website = CharField(max_length=255, blank=True)
  beroep = CharField(max_length=255, blank=True)
  studie = CharField(max_length=255, blank=True)
  patroon = CharField(max_length=4, blank=True)
  studienr = IntegerField(blank=True, null=True)
  studiejaar = IntegerField(blank=True, null=True)
  lidjaar = IntegerField()
  lidafdatum = DateField(blank=True, null=True)
  gebdatum = DateField()
  sterfdatum = DateField(blank=True, null=True)
  bankrekening = CharField(max_length=255, blank=True)
  machtiging = IntegerField()
  moot = CharField(max_length=1)
  verticale = CharField(max_length=1)
  verticaleleider = IntegerField()
  kringcoach = CharField(max_length=1, blank=True)
  o_adres = CharField(max_length=255, blank=True)
  o_postcode = CharField(max_length=255, blank=True)
  o_woonplaats = CharField(max_length=255, blank=True)
  o_land = CharField(max_length=255, blank=True)
  o_telefoon = CharField(max_length=255, blank=True)
  email = CharField(max_length=255)
  kerk = CharField(max_length=255, blank=True)
  muziek = CharField(max_length=255, blank=True)
  status = CharField(max_length=11)
  eetwens = CharField(max_length=255, blank=True)
  corvee_punten = IntegerField()
  corvee_punten_bonus = IntegerField()
  ontvangtcontactueel = CharField(max_length=8)
  kgb = TextField(blank=True)
  soccieid = IntegerField(db_column='soccieID')  # Field name made lowercase.
  createterm = CharField(db_column='createTerm', max_length=255)  # Field name made lowercase.
  socciesaldo = FloatField(db_column='soccieSaldo')  # Field name made lowercase.
  maalciesaldo = FloatField(db_column='maalcieSaldo')  # Field name made lowercase.
  changelog = TextField(blank=True)
  ovkaart = CharField(max_length=255)
  zingen = CharField(max_length=255)
  novitiaat = TextField()
  lengte = IntegerField()
  vrienden = TextField()
  middelbareschool = CharField(db_column='middelbareSchool', max_length=255, blank=True)  # Field name made lowercase.
  novietsoort = CharField(db_column='novietSoort', max_length=255, blank=True)  # Field name made lowercase.
  matrixplek = CharField(db_column='matrixPlek', max_length=255)  # Field name made lowercase.
  startkamp = CharField(max_length=255, blank=True)
  medisch = TextField(blank=True)
  novitiaatbijz = TextField(db_column='novitiaatBijz', blank=True)  # Field name made lowercase.

  def __str__(self):
    return "%s (%s)" % (self.formal_name(), self.uid)

  def formal_name(self):
    if self.geslacht == 'm':
      return "Am. %s" % self.achternaam
    else:
      return "Ama. %s" % self.achternaam

class AbstractGroep(Model):
  naam = CharField(max_length=255)
  status = CharField(max_length=2)
  familie = CharField(max_length=255)
  samenvatting = TextField(blank=True, null=True)
  omschrijving = TextField(blank=True, null=True)
  begin_moment = DateTimeField(blank=True, null=True)
  eind_moment = DateTimeField(blank=True, null=True)
  maker_user = ForeignKey(Profiel, db_column='maker_uid', related_name='+')
  keuzelijst = CharField(max_length=255, blank=True)

  class Meta:
    abstract = True

class GroepDoodlijnenMixin(Model):
  aanmeld_limiet = IntegerField(blank=True, null=True)
  aanmelden_vanaf = DateTimeField()
  aanmelden_tot = DateTimeField()
  bewerken_tot = DateTimeField(blank=True, null=True)
  afmelden_tot = DateTimeField(blank=True, null=True)

  class Meta:
    abstract = True

class Groep(AbstractGroep):
  rechten_aanmelden = CharField(max_length=255)

  class Meta:
    db_table = 'groepen'

class Ketzer(GroepDoodlijnenMixin, AbstractGroep):

  class Meta:
    db_table = 'ketzers'

class Lichting(AbstractGroep):
  lidjaar = IntegerField(unique=True)

  class Meta:
    db_table = 'lichtingen'

class Ondervereniging(AbstractGroep):
  soort = CharField(max_length=1)

  class Meta:
    db_table = 'onderverenigingen'

class Verticale(AbstractGroep):
  letter = CharField(unique=True, max_length=1)

  class Meta:
    db_table = 'verticalen'

class Kring(AbstractGroep):
  verticale = ForeignKey(Verticale, db_column='verticale')
  kring_nummer = IntegerField()

  class Meta:
    db_table = 'kringen'

class Werkgroep(GroepDoodlijnenMixin, AbstractGroep):

  class Meta:
    db_table = 'werkgroepen'

class Activiteit(GroepDoodlijnenMixin, AbstractGroep):
  soort = CharField(max_length=15)
  rechten_aanmelden = CharField(max_length=255, blank=True)
  locatie = CharField(max_length=255, blank=True)
  in_agenda = IntegerField()

  class Meta:
    db_table = 'activiteiten'

class Bestuur(AbstractGroep):
  bijbeltekst = TextField()

  class Meta:
    db_table = 'besturen'

class Commissie(AbstractGroep):
  soort = CharField(max_length=1)

  class Meta:
    db_table = 'commissies'

class AbstractLid(Model):
  user = ForeignKey(Profiel, db_column='uid', related_name='+')
  opmerking = CharField(max_length=255, blank=True)
  lid_sinds = DateTimeField()
  door_user = ForeignKey(Profiel, db_column='door_uid', related_name='+')

  class Meta:
    unique_together = (('groep', 'user'),)
    abstract = True

class GroepLeden(AbstractLid):
  groep = ForeignKey(Groep, related_name="leden")

  class Meta:
    db_table = 'groep_leden'

class KringLid(AbstractLid):
  groep = ForeignKey(Kring, related_name="leden")

  class Meta:
    db_table = 'kring_leden'

class CommissieLid(AbstractLid):
  groep = ForeignKey(Commissie, related_name="leden")

  class Meta:
    db_table = 'commissie_leden'

class BestuursLid(AbstractLid):
  groep = ForeignKey(Bestuur, related_name="leden")

  class Meta:
    db_table = 'bestuurs_leden'

class VerticaleLid(AbstractLid):
  groep = ForeignKey(Verticale, related_name="leden")

  class Meta:
    db_table = 'verticale_leden'

class LichtingLid(AbstractLid):
  groep = ForeignKey(Lichting, related_name="leden")

  class Meta:
    db_table = 'lichting_leden'

class OnderverenigingsLid(AbstractLid):
  groep = ForeignKey(Ondervereniging, related_name="leden")

  class Meta:
    db_table = 'ondervereniging_leden'

class KetzerDeelnemer(AbstractLid):
  groep = ForeignKey(Ketzer, related_name="leden")

  class Meta:
    db_table = 'ketzer_deelnemers'

class WerkgroepDeelnemer(AbstractLid):
  groep = ForeignKey(Werkgroep, related_name="leden")

  class Meta:
    db_table = 'werkgroep_deelnemers'

class ActiviteitDeelnemer(AbstractLid):
  groep = ForeignKey(Activiteit, related_name="leden")

  class Meta:
    db_table = 'activiteit_deelnemers'
