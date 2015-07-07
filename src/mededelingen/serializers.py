from rest_framework import serializers
from mededelingen.models import Mededeling

class MededelingenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mededeling
    fields = (
      'datum',
      'vervaltijd',
      'titel',
      'tekst',
      'prive',
      'prioriteit',
      'user',
      'doelgroep',
      'verborgen',
      'verwijderd',
      'plaatje'
    )