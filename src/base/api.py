from django.conf.urls import url
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from .serializers import *

from rest_framework import mixins, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import list_route, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter
from rest_framework.pagination import PageNumberPagination

import logging
import json

logger = logging.getLogger(__name__)


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

  permission_classes = [IsAuthenticated]
  serializer_class = ProfielSerializer
  filter_backends = (filters.SearchFilter,)
  search_fields = ('pk', 'voornaam', 'achternaam',)

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


router = DefaultRouter()
router.register("lichtingen", LichtingApi, base_name="lichtingen")
router.register("profiel", ProfielApi, base_name="profiel")
urls = [
  url(r'^auth/$', user_get, name="auth-retrieve"),
  url(r'^auth/login$', user_login, name="auth-login"),
] + router.urls
