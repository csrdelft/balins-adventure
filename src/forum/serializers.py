from rest_framework import serializers
from .models import *

class ForumCategorieSerializer(serializers.ModelSerializer):
  class Meta:
    model = ForumCategorie
    fields = (
      'categorie_id',
      'titel',
      'volgorde',
    )

class ForumDeelSerializer(serializers.ModelSerializer):
  categorie = ForumCategorieSerializer()

  class Meta:
    model = ForumDeel
    fields = (
      'forum_id',
      'categorie',
      'titel',
      'omschrijving'
    )

class ForumPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = ForumPost
    fields = ('post_id', 'draad', 'user', 'tekst', 'datum_tijd', 'laatst_gewijzigd')
    read_only_fields = ('post_id', 'user', 'datum_tijd', 'laatst_gewijzigd')

class ShortForumDraadSerializer(serializers.ModelSerializer):

  user = serializers.ReadOnlyField(source="user.pk")

  class Meta:
    model = ForumDraad
    fields = (
      'draad_id',
      'forum',
      'titel',
      'user'
    )

class ForumDraadSerializer(serializers.ModelSerializer):

  user = serializers.ReadOnlyField(source="user.pk")
  laatst_gewijzigd = serializers.ReadOnlyField()
  datum_tijd = serializers.ReadOnlyField()

  class Meta:
    model = ForumDraad
    fields = (
      'draad_id',
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
      'forum_id',
      'draden',
      'categorie',
      'titel',
      'omschrijving'
    )
