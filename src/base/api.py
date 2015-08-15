from django.conf.urls import url
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from .serializers import *

from rest_framework import mixins, viewsets, filters, metadata
from rest_framework.response import Response
from rest_framework.decorators import list_route, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter
from rest_framework.pagination import PageNumberPagination

import django_filters
import logging
import json

logger = logging.getLogger(__name__)

class MinimalMetadata(metadata.BaseMetadata):

  def determine_metadata(self, request, view):
    return dict(
      name=view.get_view_name(),
      description=view.get_view_description()
    )

class StekPaginator(PageNumberPagination):
  page_size = 100
  page_size_query_param = 'page_size'
  max_page_size = 1000

  def get_paginated_response(self, data):
    resp = super().get_paginated_response(data)

    # include the current page number
    resp.data['pageno'] = self.page.number

    return resp

class StekViewSet(viewsets.GenericViewSet):

  pagination_class = StekPaginator
  metadata_class = MinimalMetadata

  def get_serializer(self, *args, **kwargs):
    """ Improved get_serializer that will look for list_/detail_serializer_class properties
    """
    if self.__class__.serializer_class is not None:
      cls = self.__class__.serializer_class
    else:
      if self.action == 'list' and hasattr(self.__class__,
                           'list_serializer_class'):
        cls = self.__class__.list_serializer_class
      elif hasattr(self.__class__, 'detail_serializer_class'):
        cls = self.__class__.detail_serializer_class
      else:
        # error handling
        return super().get_serializer(*args, **kwargs)

    # default the context
    kwargs['context'] = self.get_serializer_context()

    return cls(*args, **kwargs)


class ProfielApi(mixins.ListModelMixin, mixins.RetrieveModelMixin, StekViewSet):

  class ProfielFilter(django_filters.FilterSet):
    lichting = django_filters.CharFilter(name="lichtinglid__groep__lidjaar")

    class Meta:
      model = Profiel
      fields = ['lichting']

  permission_classes = [IsAuthenticated]
  list_serializer_class = ShortProfielSerializer
  detail_serializer_class = ProfielSerializer
  filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
  filter_class = ProfielFilter
  search_fields = ('pk', 'voornaam', 'achternaam','email')

  def get_queryset(self):
    return Profiel.objects.all()

class LichtingApi(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

  permission_classes = [IsAuthenticated]
  serializer_class = LichtingSerializer

  def get_queryset(self):
    return Lichting.objects.all()

  @list_route(methods=["get"])
  def demooiste(self, request):
    """ Returns de unaniem besloten mooiste lichting
        ---
        omit_serializer: true
    """
    # throws mooiste lichting not found when 2013 is missing
    return Response(self.get_serializer(Lichting.objects.get(
      lidjaar=2013)).data)


@api_view(["GET"])
def user_get(request):
  if request.user.is_authenticated():
    return Response(ShortProfielSerializer(request.profiel).data)
  else:
    return Response({})


@api_view(["POST"])
def user_login(request):
  username = request.data['username']
  password = request.data['password']

  user = authenticate(username=username, password=password)
  if user is not None:
    if user.is_active:
      login(request, user)
      return Response(ShortProfielSerializer(user.profiel).data)
    else:
      raise PermissionDenied(detail="Inactieve gebruiker")
  else:
    raise AuthenticationFailed()

class VerticaleApi(mixins.ListModelMixin, mixins.RetrieveModelMixin, StekViewSet):

  permission_classes = [IsAuthenticated]
  serializer_class = VerticaleDetailSerializer
  pagination_class = None

  def get_queryset(self):
    return Verticale.objects.all().exclude(naam="Geen")

class KringApi(mixins.ListModelMixin, mixins.RetrieveModelMixin, StekViewSet):

  permission_classes = [IsAuthenticated]
  serializer_class = KringDetailSerializer
  pagination_class = None

  def get_queryset(self):
    return Kring.objects.all().order_by("naam")

class CommissieApi(mixins.ListModelMixin, mixins.RetrieveModelMixin, StekViewSet):

  class CommissieMetadata(MinimalMetadata):
    def determine_metadata(self, request, view):
      metadict = super().determine_metadata(request,view)

      if request.user.is_authenticated():
        metadict['families'] = [
          o['familie'] for o in Commissie.objects.order_by('familie').values('familie').distinct()
        ]

      return metadict

  permission_classes = [IsAuthenticated]
  serializer_class = CommissieDetailSerializer
  pagination_class = None
  filter_fields = ('status','familie')
  metadata_class = CommissieMetadata

  def get_queryset(self):
    return Commissie.objects.all()

router = DefaultRouter()
router.register("lichtingen", LichtingApi, base_name="lichtingen")
router.register("verticalen", VerticaleApi, base_name="verticalen")
router.register("commissies", CommissieApi, base_name="commissies")
router.register("kringen", KringApi, base_name="kringen")
router.register("profiel", ProfielApi, base_name="profiel")
urls = [
  url(r'^auth/$', user_get, name="auth-retrieve"),
  url(r'^auth/login$', user_login, name="auth-login"),
] + router.urls
