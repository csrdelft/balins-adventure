from rest_framework import mixins, viewsets
from mededelingen.serializers import MededelingenSerializer
from mededelingen.models import Mededeling
from base.utils import deny_on_fail

class MededelingenViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
  mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

  serializer_class = MededelingenSerializer

  def get_queryset(self):
    return Mededeling\
      .get_viewable_by(self.request.user)\
      .order_by('-datum')

  def destroy(self, request, *args, **kwargs):
    deny_on_fail(request.user.has_perm('mededelingen.delete_mededeling', self.get_object))
    return super().destroy(request, *args, **kwargs)

  def create(self, request, *args, **kwargs):
    deny_on_fail(request.user.has_perm('mededelingen.add_mededeling', self.get_object))
    return super().create(request, *args, **kwargs)

  def update(self, request, *args, **kwargs):
    deny_on_fail(request.user.has_perm('mededelingen.change_mededeling', self.get_object))
    return super().update(request, *args, **kwargs)
