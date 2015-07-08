from django.contrib.auth.models import User
from django.views.decorators.http import condition
from .models import *
from .serializers import *
from base.utils import *

from rest_framework import views, response, generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter

from datetime import datetime
import logging
import json

logger = logging.getLogger(__name__)

class ProfielApi(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

  permission_classes = [IsAuthenticated]
  serializer_class = ProfielSerializer

  def get_queryset(self):
    return Profiel.objects\
      .prefetch_related(
        "kring",
        "verticale",
        "commissies",
        "werkgroepen",
        "onderverenigingen",
        "overige_groepen")\
      .all()

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

router = DefaultRouter()
router.register("lichtingen", LichtingApi, base_name="lichtingen")
router.register("profiel", ProfielApi, base_name="profiel")
urls = router.urls
