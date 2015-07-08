from rest_framework import serializers
from mededelingen.models import Mededeling


class MededelingenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mededeling
    fields = (
      'id',
      'live',
      'datum',
      'vervaltijd',
      'titel',
      'tekst',
      'prive',
      'prioriteit',
      'user',
      'plaatje',
      'audience'
    )
