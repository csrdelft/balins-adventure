from rest_framework import serializers
from .models import *
from base.serializers import ShortProfielSerializer
from base.api import StekPaginator

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

  user = ShortProfielSerializer(read_only=True)

  # permissions
  can_delete = serializers.SerializerMethodField()

  def get_can_delete(self, post):
    return self.context['request'].user.has_perm('forum.delete_forumpost', post)

  class Meta:
    model = ForumPost
    fields = (
      'pk',
      'draad',
      'user',
      'tekst',
      'datum_tijd',
      'can_delete',
      'laatst_gewijzigd'
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

class ListForumDraadSerializer(serializers.ModelSerializer):

  user = ShortProfielSerializer(read_only=True)
  laatste_wijziging_user = ShortProfielSerializer(read_only=True, source="laatste_post.user")
  laatst_gewijzigd = serializers.ReadOnlyField(source="laatste_post.laatst_gewijzigd")

  # permissions
  can_delete = serializers.SerializerMethodField()

  def get_can_delete(self, draad):
    return self.context['request'].user.has_perm('forum.delete_forumdraad', draad)

  class Meta:
    model = ForumDraad
    read_only_fields = ('datum_tijd', "laatst_gewijzigd", "laatste_wijziging_user")
    fields = (
      'pk',
      'user',
      'forum',
      'titel',
      'datum_tijd',
      'gesloten',
      'plakkerig',
      'laatst_gewijzigd',
      'laatste_wijziging_user',
      'can_delete'
    )

class DetailForumDraadSerializer(ListForumDraadSerializer):

  posts = serializers.SerializerMethodField()

  def get_posts(self, draad):
    posts_query = draad.posts.all().order_by("datum_tijd")
    paginator = StekPaginator()

    serializer = ForumPostSerializer(
      paginator.paginate_queryset(posts_query, self.context['request']),
      context=self.context,
      many=True
    )

    return paginator.get_paginated_response(serializer.data).data

  class Meta:
    model = ForumDraad
    read_only_fields = ListForumDraadSerializer.Meta.read_only_fields
    fields = ListForumDraadSerializer.Meta.fields + ('posts',)

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
