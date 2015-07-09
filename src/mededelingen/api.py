from rest_framework import mixins, viewsets
from mededelingen.serializers import MededelingenSerializer
from mededelingen.models import Mededeling
from base.utils import deny_on_fail

class MededelingenViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
  mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

  serializer_class = MededelingenSerializer

  def get_queryset(self):
    return Mededeling.get_viewable_by(self.request.user)

  def destroy(self, request, *args, **kwargs):
    deny_on_fail(request.user.has_perm('mededelingen.destroy', self.get_object()))
    super(request, *args, **kwargs)

  def create(self, request, *args, **kwargs):
    print('-----------get object--------------')
    instance = self.get_object()
    print('-----------entered-----------------')
    deny_on_fail(request.user.has_perm('mededelingen.create', instance))
    print('-----------not failed--------------')
    super()