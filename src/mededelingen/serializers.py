from rest_framework import serializers
from mededelingen.models import Mededeling


class MededelingenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mededeling
    fields = (
      'pk',
      'live',
      'datum',
      'vervaltijd',
      'titel',
      'tekst',
      'prioriteit',
      'user',
      'plaatje',
      'audience'
    )
