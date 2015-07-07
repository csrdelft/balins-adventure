from django.db import models
from django.contrib.auth.models import User

class Profiel(models.Model):
  class Meta:
    db_table = 'profielen'

  user = models.OneToOneField(User, null=True, related_name="profiel")
  uid = models.CharField(primary_key=True, max_length=4)

  nickname = models.CharField(max_length=255)
  duckname = models.CharField(max_length=255, blank=True)
  voornaam = models.CharField(max_length=255)
  tussenvoegsel = models.CharField(max_length=255, blank=True)
  achternaam = models.CharField(max_length=255)
  voorletters = models.CharField(max_length=255)
  postfix = models.CharField(max_length=255, blank=True)
  adres = models.CharField(max_length=255)
  postcode = models.CharField(max_length=255)
  woonplaats = models.CharField(max_length=255)
  land = models.CharField(max_length=255, blank=True)
  telefoon = models.CharField(max_length=255, blank=True)
  mobiel = models.CharField(max_length=255, blank=True)
  geslacht = models.CharField(max_length=1)
  voornamen = models.CharField(max_length=255)
  echtgenoot = models.CharField(max_length=4, blank=True)
  adresseringechtpaar = models.CharField(max_length=255, blank=True)
  icq = models.CharField(max_length=255, blank=True)
  msn = models.CharField(max_length=255, blank=True)
  skype = models.CharField(max_length=255, blank=True)
  jid = models.CharField(max_length=255, blank=True)
  linkedin = models.CharField(max_length=255, blank=True)
  website = models.CharField(max_length=255, blank=True)
  beroep = models.CharField(max_length=255, blank=True)
  studie = models.CharField(max_length=255, blank=True)
  patroon = models.CharField(max_length=4, blank=True)
  studienr = models.IntegerField(blank=True, null=True)
  studiejaar = models.IntegerField(blank=True, null=True)
  lidjaar = models.IntegerField()
  lidafdatum = models.DateField(blank=True, null=True)
  gebdatum = models.DateField(blank=True, null=True)
  sterfdatum = models.DateField(blank=True, null=True)
  bankrekening = models.CharField(max_length=255, blank=True)
  machtiging = models.IntegerField()
  moot = models.CharField(max_length=1)
  verticaleleider = models.IntegerField()
  kringcoach = models.CharField(max_length=1, blank=True)
  o_adres = models.CharField(max_length=255, blank=True)
  o_postcode = models.CharField(max_length=255, blank=True)
  o_woonplaats = models.CharField(max_length=255, blank=True)
  o_land = models.CharField(max_length=255, blank=True)
  o_telefoon = models.CharField(max_length=255, blank=True)
  email = models.CharField(max_length=255)
  kerk = models.CharField(max_length=255, blank=True)
  muziek = models.CharField(max_length=255, blank=True)
  status = models.CharField(max_length=11)
  eetwens = models.CharField(max_length=255, blank=True)
  corvee_punten = models.IntegerField()
  corvee_punten_bonus = models.IntegerField()
  ontvangtcontactueel = models.CharField(max_length=8)
  kgb = models.TextField(blank=True)
  soccieid = models.IntegerField(db_column='soccieID')  # Field name made lowercase.
  createterm = models.CharField(db_column='createTerm', max_length=255)  # Field name made lowercase.
  socciesaldo = models.FloatField(db_column='soccieSaldo')  # Field name made lowercase.
  maalciesaldo = models.FloatField(db_column='maalcieSaldo')  # Field name made lowercase.
  changelog = models.TextField(blank=True)
  ovkaart = models.CharField(max_length=255)
  zingen = models.CharField(max_length=255)
  novitiaat = models.TextField()
  lengte = models.IntegerField()
  vrienden = models.TextField()
  middelbareschool = models.CharField(db_column='middelbareSchool', max_length=255, blank=True)  # Field name made lowercase.
  novietsoort = models.CharField(db_column='novietSoort', max_length=255, blank=True)  # Field name made lowercase.
  matrixplek = models.CharField(db_column='matrixPlek', max_length=255)  # Field name made lowercase.
  startkamp = models.CharField(max_length=255, blank=True)
  medisch = models.TextField(blank=True)
  novitiaatbijz = models.TextField(db_column='novitiaatBijz', blank=True)  # Field name made lowercase.

  def commissies(self):
    return map(lambda cl: cl.groep, CommissieLid.objects.filter(user=self))

  def verticale(self):
    vert_lid = VerticaleLid.objects.filter(user=self).first()
    if vert_lid is not None:
      return vert_lid.groep

    return None

  def kring(self):
    kring_lid = KringLid.objects.filter(user=self).first()
    if kring_lid is not None:
      return kring_lid.groep

    return None

  def werkgroepen(self):
    return map(lambda cl: cl.groep, WerkgroepDeelnemer.objects.filter(user=self))

  def onderverenigingen(self):
    return map(lambda cl: cl.groep, OnderverenigingsLid.objects.filter(user=self))

  def overige_groepen(self):
    return map(lambda cl: cl.groep, GroepsLid.objects.filter(user=self))

  def __str__(self):
    return "%s (%s)" % (self.formal_name(), self.uid)

  def full_name(self):
    return "%s %s %s" % (self.voornaam,self.tussenvoegsel,self.achternaam)

  def formal_name(self):
    if self.geslacht == 'm':
      return "Am. %s" % self.achternaam
    else:
      return "Ama. %s" % self.achternaam

class AbstractGroep(models.Model):
  naam = models.CharField(max_length=255)
  status = models.CharField(max_length=2, default="ht")
  familie = models.CharField(max_length=255)
  samenvatting = models.TextField(blank=True)
  omschrijving = models.TextField(blank=True)
  begin_moment = models.DateTimeField(blank=True, null=True)
  eind_moment = models.DateTimeField(blank=True, null=True)
  maker_user = models.ForeignKey(Profiel, db_column='maker_uid', related_name='+')
  keuzelijst = models.CharField(max_length=255, blank=True)

  ## !! IMPORTANT
  ## abstract related object manager `leden` expected on any child class

  class Meta:
    abstract = True

class GroepDoodlijnenMixin(models.Model):
  aanmeld_limiet = models.IntegerField(blank=True, null=True)
  aanmelden_vanaf = models.DateTimeField(blank=True, null=True)
  aanmelden_tot = models.DateTimeField(blank=True, null=True)
  bewerken_tot = models.DateTimeField(blank=True, null=True)
  afmelden_tot = models.DateTimeField(blank=True, null=True)

  class Meta:
    abstract = True

class Groep(AbstractGroep):
  rechten_aanmelden = models.CharField(max_length=255)

  def __str__(self):
    return "Groep: %s" % self.naam

  class Meta:
    db_table = 'groepen'

class Ketzer(GroepDoodlijnenMixin, AbstractGroep):

  def __str__(self):
    return "Ketzer: %s" % self.naam

  class Meta:
    db_table = 'ketzers'

class Lichting(AbstractGroep):
  lidjaar = models.IntegerField(unique=True)

  def __str__(self):
    return "Lichting: %s" % self.naam

  class Meta:
    db_table = 'lichtingen'

class Ondervereniging(AbstractGroep):
  soort = models.CharField(max_length=1)

  def __str__(self):
    return "Ondervereniging: %s" % self.naam

  class Meta:
    db_table = 'onderverenigingen'

class Verticale(AbstractGroep):
  letter = models.CharField(unique=True, max_length=1)

  def __str__(self):
    return "Verticale: %s" % self.naam

  class Meta:
    db_table = 'verticalen'

class Woonoord(AbstractGroep):

  def __str__(self):
    return "Woonoord: %s" % self.naam

  class Meta:
    db_table = 'woonoorden'

class Kring(AbstractGroep):
  verticale = models.ForeignKey(Verticale, db_column='verticale')
  kring_nummer = models.IntegerField()

  def __str__(self):
    return "Kring: %s" % self.naam

  class Meta:
    db_table = 'kringen'

class Werkgroep(GroepDoodlijnenMixin, AbstractGroep):

  def __str__(self):
    return "Werkgroep: %s" % self.naam

  class Meta:
    db_table = 'werkgroepen'

class Activiteit(GroepDoodlijnenMixin, AbstractGroep):
  soort = models.CharField(max_length=15) # TODO choicefield ??
  rechten_aanmelden = models.CharField(max_length=255, blank=True)
  locatie = models.CharField(max_length=255, blank=True)
  in_agenda = models.BooleanField()

  def __str__(self):
    return "Activiteit: %s" % self.naam

  class Meta:
    db_table = 'activiteiten'

class Bestuur(AbstractGroep):
  bijbeltekst = models.TextField()

  def __str__(self):
    return "Bestuur: %s" % self.naam

  class Meta:
    db_table = 'besturen'

class Commissie(AbstractGroep):
  soort = models.CharField(max_length=1)

  def __str__(self):
    return "Commissie: %s" % self.naam

  class Meta:
    db_table = 'commissies'

class AbstractLid(models.Model):
  user = models.ForeignKey(Profiel, db_column='uid', related_name='+')
  opmerking = models.CharField(max_length=255, blank=True)
  lid_sinds = models.DateTimeField()
  door_user = models.ForeignKey(Profiel, db_column='door_uid', related_name='+')

  ## !! IMPORTANT
  ## foreignkey `groep` expected on any child class

  def __str__(self):
    return "Groepslid: %s" % self.user_id

  class Meta:
    unique_together = (('groep', 'user'),)
    abstract = True

class GroepsLid(AbstractLid):
  groep = models.ForeignKey(Groep, related_name="leden")

  class Meta:
    db_table = 'groep_leden'

class KringLid(AbstractLid):
  groep = models.ForeignKey(Kring, related_name="leden")

  class Meta:
    db_table = 'kring_leden'

class CommissieLid(AbstractLid):
  groep = models.ForeignKey(Commissie, related_name="leden")

  class Meta:
    db_table = 'commissie_leden'

class BestuursLid(AbstractLid):
  groep = models.ForeignKey(Bestuur, related_name="leden")

  class Meta:
    db_table = 'bestuurs_leden'

class VerticaleLid(AbstractLid):
  groep = models.ForeignKey(Verticale, related_name="leden")

  class Meta:
    db_table = 'verticale_leden'

class Bewoners(AbstractLid):
  groep = models.ForeignKey(Woonoord, related_name="leden")

  class Meta:
    db_table = 'bewoners'

class LichtingLid(AbstractLid):
  groep = models.ForeignKey(Lichting, related_name="leden")

  class Meta:
    db_table = 'lichting_leden'

class OnderverenigingsLid(AbstractLid):
  groep = models.ForeignKey(Ondervereniging, related_name="leden")

  class Meta:
    db_table = 'ondervereniging_leden'

class KetzerDeelnemer(AbstractLid):
  groep = models.ForeignKey(Ketzer, related_name="leden")

  class Meta:
    db_table = 'ketzer_deelnemers'

class WerkgroepDeelnemer(AbstractLid):
  groep = models.ForeignKey(Werkgroep, related_name="leden")

  class Meta:
    db_table = 'werkgroep_deelnemers'

class ActiviteitDeelnemer(AbstractLid):
  groep = models.ForeignKey(Activiteit, related_name="leden")

  class Meta:
    db_table = 'activiteit_deelnemers'

