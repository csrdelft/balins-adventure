from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class MaaltijdAanmeldingSerializer(serializers.ModelSerializer):
  class Meta:
    model = MaaltijdAanmelding
    fields = ('user', 'aantal_gasten', 'gasten_eetwens', 'maaltijd')

class MaaltijdSerializer(serializers.ModelSerializer):

  aanmeldingen = MaaltijdAanmeldingSerializer(many=True)

  class Meta:
    model = Maaltijd
    fields = (
      'id',
      'titel',
      'datum',
      'tijd',
      'prijs',
      'omschrijving',
      'gesloten',
      'aanmeld_limiet',
      'aanmeldingen'
    )
