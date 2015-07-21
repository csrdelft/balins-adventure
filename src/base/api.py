from django.conf.urls import url
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from .serializers import *

from rest_framework import mixins, viewsets
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
    return Response(data)

class ProfielApi(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

  permission_classes = [IsAuthenticated]
  serializer_class = ProfielSerializer

  def get_queryset(self):
    return Profiel.objects.all()

class LichtingApi(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

  permission_classes = [IsAuthenticated]
  serializer_class = LichtingSerializer

  def get_queryset(self):
    return Lichting.objects.all();

  @list_route(methods=["get"])
  def demooiste(self, request):
    """ Returns de unaniem besloten mooiste lichting
        ---
        omit_serializer: true
    """
    # throws mooiste lichting not found when 2013 is missing
    return Response(self.get_serializer(Lichting.objects.get(lidjaar=2013)).data)

@api_view(["POST"])
def user_login(request):
  username = request.data['username']
  password = request.data['password']

  user = authenticate(username=username, password=password)
  if user is not None:
    if user.is_active:
      login(request, user)
      Response(ShortProfielSerializer(user.profiel).data)
    else:
      raise PermissionDenied(detail="Inactieve gebruiker")
  else:
    raise AuthenticationFailed()

router = DefaultRouter()
router.register("lichtingen", LichtingApi, base_name="lichtingen")
router.register("profiel", ProfielApi, base_name="profiel")
urls = [
  url(r'^login$', user_login, name="login"),
] + router.urls
