from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class LichtingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lichting
    fields = (
      "pk", "naam", "status", "familie", "samenvatting",
      "begin_moment", "eind_moment", "maker_user"
    )

class KringListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Kring
    fields = (
      "pk", "naam", "status", "familie", "samenvatting",
      "begin_moment", "eind_moment", "maker_user"
    )

class VerticaleListSerializer(serializers.ModelSerializer):
  aantal_leden = serializers.SerializerMethodField()

  def get_aantal_leden(self, verticale):
    return verticale.leden.count()

  class Meta:
    model = Verticale
    fields = (
      "pk", "naam", "status", "familie", "samenvatting",
      "begin_moment", "eind_moment", "maker_user",
      "aantal_leden"
    )

class CommissieListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Commissie
    fields = (
      "pk", "naam", "status", "familie", "samenvatting",
      "begin_moment", "eind_moment", "maker_user"
    )

class WerkgroepSerializer(serializers.ModelSerializer):
  class Meta:
    model = Werkgroep
    fields = (
      "pk", "naam", "status", "familie", "samenvatting",
      "begin_moment", "eind_moment", "maker_user"
    )

class OnderverenigingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ondervereniging
    fields = (
      "pk", "naam", "status", "familie", "samenvatting",
      "begin_moment", "eind_moment", "maker_user"
    )

class GroepSerializer(serializers.ModelSerializer):
  class Meta:
    model = Groep
    fields = (
      "pk", "naam", "status", "familie", "samenvatting",
      "begin_moment", "eind_moment", "maker_user"
    )

class ShortProfielSerializer(serializers.ModelSerializer):

  lidjaar = serializers.ReadOnlyField()

  class Meta:
    model = Profiel
    fields = (
      'pk',
      'user',
      'voornaam',
      'achternaam',
      'full_name',
      'lidjaar',
      'email'
    )
    read_only_fields = ('full_name', 'lidjaar')

class ProfielSerializer(serializers.ModelSerializer):
  kring = KringListSerializer()
  verticale = VerticaleListSerializer()
  commissies = CommissieListSerializer(many=True)
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

class CommissieLidSerializer(serializers.ModelSerializer):
  user = ShortProfielSerializer()

  class Meta:
    model = VerticaleLid
    fields = ("user",)

class CommissieDetailSerializer(serializers.ModelSerializer):
  leden = serializers.SerializerMethodField()

  def get_leden(self, verticale):
    # restrict shown members by status
    leden = verticale.leden.filter(user__status=Profiel.STATUS.LID)
    return CommissieLidSerializer(leden, many=True).data

  class Meta:
    model = Commissie
    fields = (
      "pk", "naam", "status", "familie", "samenvatting",
      "begin_moment", "eind_moment", "maker_user",
      "leden"
    )

class KringLidSerializer(serializers.ModelSerializer):
  user = ShortProfielSerializer()

  class Meta:
    model = KringLid
    fields = ("user",)

class KringDetailSerializer(serializers.ModelSerializer):
  leden = serializers.SerializerMethodField()
  verticale = VerticaleListSerializer()

  def get_leden(self, kring):
    # restrict shown members by status
    leden = kring.leden.filter(user__status=Profiel.STATUS.LID)
    return KringLidSerializer(leden, many=True).data

  class Meta:
    model = Kring
    fields = (
      "pk", "naam", "status", "familie", "samenvatting",
      "begin_moment", "eind_moment", "maker_user",
      "leden"
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
    fields = (
      "pk", "naam", "samenvatting", "leden"
    )
