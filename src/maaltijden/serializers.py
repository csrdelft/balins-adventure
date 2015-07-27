from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class MaaltijdAanmeldingSerializer(serializers.ModelSerializer):

  # make this explicit because the defualt is a primaryKeyRelatedField
  # with required=True, which clashes with the read_only=True
  user = serializers.PrimaryKeyRelatedField(source="user", read_only=True)

  class Meta:
    model = MaaltijdAanmelding
    read_only_fields = ('user',)
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
