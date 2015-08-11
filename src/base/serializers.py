from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class LichtingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lichting

class KringSerializer(serializers.ModelSerializer):
  class Meta:
    model = Kring

class VerticaleListSerializer(serializers.ModelSerializer):
  aantal_leden = serializers.SerializerMethodField()

  def get_aantal_leden(self, verticale):
    return verticale.leden.count()

  class Meta:
    model = Verticale
    fields = ("pk", "naam", "aantal_leden")

class CommissieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Commissie

class WerkgroepSerializer(serializers.ModelSerializer):
  class Meta:
    model = Werkgroep

class OnderverenigingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ondervereniging

class GroepSerializer(serializers.ModelSerializer):
  class Meta:
    model = Groep

class ShortProfielSerializer(serializers.ModelSerializer):

  lidjaar = serializers.ReadOnlyField()

  class Meta:
    model = Profiel
    fields = (
      'user',
      'pk',
      'voornaam',
      'achternaam',
      'full_name',
      'lidjaar'
    )
    read_only_fields = ('full_name', 'lidjaar')

class ProfielSerializer(serializers.ModelSerializer):
  kring = KringSerializer()
  verticale = VerticaleListSerializer()
  commissies = CommissieSerializer(many=True)
  werkgroepen = WerkgroepSerializer(many=True)
  onderverenigingen = OnderverenigingSerializer(many=True)
  overige_groepen = GroepSerializer(many=True)

  class Meta:
    model = Profiel
    fields = (
      'pk',
      'user',
      'full_name',
      'nickname',
      'duckname',
      'voornaam',
      'tussenvoegsel',
      'achternaam',
      'voorletters',
      'postfix',
      'adres',
      'postcode',
      'woonplaats',
      'land',
      'telefoon',
      'mobiel',
      'geslacht',
      'voornamen',
      'echtgenoot',
      'adresseringechtpaar',
      'icq',
      'msn',
      'skype',
      'jid',
      'linkedin',
      'website',
      'beroep',
      'studie',
      'patroon',
      'studienr',
      'studiejaar',
      'lidjaar',
      'lidafdatum',
      'gebdatum',
      'sterfdatum',
      'bankrekening',
      'machtiging',
      'verticaleleider',
      'kringcoach',
      'email',
      'kerk',
      'muziek',
      'status',
      'eetwens',
      'corvee_punten',
      'corvee_punten_bonus',
      'soccieid',
      'createterm',
      'socciesaldo',
      'maalciesaldo',
      'lengte',
      'vrienden',
      'middelbareschool',
      "kring",
      "verticale",
      "commissies",
      "werkgroepen",
      "onderverenigingen",
      "overige_groepen"
    )

class VerticaleLidSerializer(serializers.ModelSerializer):
  user = ShortProfielSerializer()

  class Meta:
    model = VerticaleLid
    fields = ("user",)

class VerticaleDetailSerializer(serializers.ModelSerializer):
  leden = serializers.SerializerMethodField()

  def get_leden(self, verticale):
    # restrict shown members by status
    leden = verticale.leden.filter(user__status=Profiel.STATUS.LID)
    return VerticaleLidSerializer(leden, many=True).data

  class Meta:
    model = Verticale
    fields = ("pk", "naam", "leden")
