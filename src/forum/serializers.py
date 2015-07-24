from rest_framework import serializers
from .models import *
from base.serializers import ShortProfielSerializer

class ForumCategorieSerializer(serializers.ModelSerializer):
  class Meta:
    model = ForumCategorie
    fields = (
      'pk',
      'titel',
      'volgorde',
    )

class ForumDeelSerializer(serializers.ModelSerializer):
  categorie = ForumCategorieSerializer()

  class Meta:
    model = ForumDeel
    fields = (
      'pk',
      'categorie',
      'titel',
      'omschrijving'
    )

class ForumPostSerializer(serializers.ModelSerializer):

  user = ShortProfielSerializer()

  class Meta:
    model = ForumPost
    fields = (
      'pk',
      'draad',
      'user',
      'tekst',
      'datum_tijd',
    )
    read_only_fields = (
      'user',
      'datum_tijd',
    )

class ShortForumDraadSerializer(serializers.ModelSerializer):

  user = serializers.ReadOnlyField(source="user.pk")

  class Meta:
    model = ForumDraad
    fields = (
      'pk',
      'forum',
      'titel',
      'user'
    )

class ForumDraadSerializer(serializers.ModelSerializer):

  user = ShortProfielSerializer(read_only=True)

  class Meta:
    model = ForumDraad
    read_only_fields = ('datum_tijd', )
    fields = (
      'pk',
      'user',
      'forum',
      'titel',
      'datum_tijd',
      'gesloten',
      'plakkerig'
    )

class EntireForumDeelSerializer(serializers.ModelSerializer):
  draden = ShortForumDraadSerializer(many=True)

  class Meta:
    model = ForumDeel
    fields = (
      'pk',
      'draden',
      'categorie',
      'titel',
      'omschrijving'
    )
