from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

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
      "user",
      "kring",
      "verticale",
      "commissies",
      "werkgroepen",
      "onderverenigingen",
      "overige_groepen"
    )
