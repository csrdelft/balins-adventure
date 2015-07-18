from rest_framework import serializers
from base.serializers import ShortProfielSerializer
from mededelingen.models import Mededeling

class MededelingenSerializer(serializers.ModelSerializer):

  user = ShortProfielSerializer(read_only=True)

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
