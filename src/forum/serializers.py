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
  class Meta:
    model = ForumPost
    fields = ('pk', 'draad', 'user', 'tekst', 'datum_tijd', 'laatst_gewijzigd')
    read_only_fields = ('user', 'datum_tijd', 'laatst_gewijzigd')

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
  laatst_gewijzigd = serializers.ReadOnlyField()
  datum_tijd = serializers.ReadOnlyField()

  class Meta:
    model = ForumDraad
    fields = (
      'pk',
      'user',
      'forum',
      'titel',
      'laatst_gewijzigd',
      'datum_tijd',
      'gesloten',
      'plakkerig'
    )

class EntireForumDraadSerializer(serializers.ModelSerializer):
  posts = ForumPostSerializer(many=True)

  class Meta:
    model = ForumDraad
    fields = ForumDraadSerializer.Meta.fields + ('posts',)

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
