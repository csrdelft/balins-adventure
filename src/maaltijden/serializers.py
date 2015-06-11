from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class MaaltijdAanmeldingSerializer(serializers.ModelSerializer):
  class Meta:
    model = MaaltijdAanmelding
    fields = (
      'maaltijd',
      'user',
      'aantal_gasten',
      'gasten_eetwens')
