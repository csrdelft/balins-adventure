from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class LichtingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lichting

class KringSerializer(serializers.ModelSerializer):
  class Meta:
    model = Kring

class VerticaleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Verticale

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

  class Meta:
    model = Profiel
    fields = (
      'user',
      'pk',
      'voornaam',
      'achternaam',
      'full_name'
    )
    read_only_fields = ('full_name', )

class ProfielSerializer(serializers.ModelSerializer):
  kring = KringSerializer()
  verticale = VerticaleSerializer()
  commissies = CommissieSerializer(many=True)
  werkgroepen = WerkgroepSerializer(many=True)
  onderverenigingen = OnderverenigingSerializer(many=True)
  overige_groepen = GroepSerializer(many=True)

  class Meta:
    model = Profiel
    fields = (
      'uid',
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
