from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class ForumPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = ForumPost

class ShortForumDraadSerializer(serializers.ModelSerializer):

  class Meta:
    model = ForumDraad
    fields = (
      'draad_id',
      'forum',
      'titel')

class ForumDraadSerializer(serializers.ModelSerializer):
  class Meta:
    model = ForumDraad
    fields = (
      'draad_id',
      'forum',
      'user',
      'titel',
      'laatst_gewijzigd',
      'datum_tijd',
      'gesloten',
      'plakkerig',
      'eerste_post_plakkerig')

class EntireForumDraadSerializer(serializers.ModelSerializer):
  posts = ForumPostSerializer(many=True)

  class Meta:
    model = ForumDraad
    fields = ForumDraadSerializer.Meta.fields + ('posts',)
