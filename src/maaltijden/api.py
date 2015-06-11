from django.contrib.auth.models import User
from django.conf.urls import url, include

from rest_framework import routers, viewsets, views, response, permissions

from .models import *
from .serializers import *

class MaaltijdAanmeldingViewSet(viewsets.ModelViewSet):
  queryset = MaaltijdAanmelding.objects.all()

  serializer_class = MaaltijdAanmeldingSerializer

router = routers.DefaultRouter()
router.register(r'aanmeldingen', MaaltijdAanmeldingViewSet)

urls = [
  url(r'^', include(router.urls)),
]
