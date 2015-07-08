from rest_framework import mixins, viewsets
from mededelingen.serializers import MededelingenSerializer
from mededelingen.models import Mededeling

class MededelingenViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
  mixins.DestroyModelMixin, viewsets.GenericViewSet):

  serializer_class = MededelingenSerializer

  def get_queryset(self):
    return Mededeling.get_viewable_by(self.request.user)