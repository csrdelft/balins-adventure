from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from mededelingen.serializers import MededelingenSerializer

class MededelingenViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
  mixins.DestroyModelMixin, viewsets.GenericViewSet):

  permission_classes = [IsAuthenticated]
  serializer_class = MededelingenSerializer

  queryset = Mededeling.objects.all()
