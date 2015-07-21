from rest_framework import mixins, viewsets, status
from mededelingen.serializers import MededelingenSerializer
from mededelingen.models import Mededeling
from base.utils import deny_on_fail

class MededelingenViewSet(
  mixins.RetrieveModelMixin,
  mixins.ListModelMixin,
  mixins.CreateModelMixin,
  mixins.DestroyModelMixin,
  mixins.UpdateModelMixin,
  viewsets.GenericViewSet
):

  serializer_class = MededelingenSerializer

  def get_queryset(self):
    return Mededeling\
      .get_viewable_by(self.request.user)\
      .order_by('-datum')

  def destroy(self, request, *args, **kwargs):
    deny_on_fail(request.user.has_perm('mededelingen.delete_mededeling', self.get_object))
    return super().destroy(request, *args, **kwargs)

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    deny_on_fail(request.user.has_perm('mededelingen.add_mededeling'))

    serializer.save(user=request.user)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

  def update(self, request, pk, *args, **kwargs):
    mededeling = self.get_object()

    # initializing the serializer with both an instance and new data
    # will cause the instance to update when we call .save() later on the serializer
    serializer = self.get_serializer(mededeling, data=request.data)
    serializer.is_valid(raise_exception=True)

    deny_on_fail(request.user.has_perm('mededelingen.change_mededeling', self.get_object()))

    # the owner is unchanged
    # update the existing mededeling
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)
