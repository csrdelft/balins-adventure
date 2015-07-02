from django.contrib.auth.models import User
from django.conf.urls import url, include
from django.http import *

from rest_framework import views, response, generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from base.http import *

from datetime import datetime, timedelta

class MaaltijdViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

  permission_classes = [IsAuthenticated]
  serializer_class = MaaltijdSerializer

  def get_queryset(self):
    # TODO permissions

    return Maaltijd.objects\
      .prefetch_related("aanmeldingen")

  def list(self, *args, **kwargs):
    at = self.request.query_params.get('at')
    if at is not None:
      at = datetime.fromtimestamp(int(at))
    else:
      at = datetime.now()

    mlten = self.get_queryset()\
      .filter(datum__gt=at)\
      .filter(datum__lt=at + timedelta(days=21))

    serializer = self.get_serializer(mlten, many=True)
    return Response(serializer.data)

  @detail_route(methods=['post'])
  def aanmelden(self, request, pk):
    # make sure the maaltijd isn't closed
    if self.get_object().gesloten:
      return Response({"details": "Maaltijd closed"}, status=status.HTTP_400_BAD_REQUEST)

    request.data['user'] = request.profiel.pk
    request.data['maaltijd'] = pk

    serializer = MaaltijdAanmeldingSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(laatst_gewijzigd=datetime.now())
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  @detail_route(methods=['post'])
  def afmelden(self, request, pk):
    # make sure the maaltijd isn't closed
    if self.get_object().gesloten:
      return Response({"details": "Maaltijd closed"}, status=status.HTTP_400_BAD_REQUEST)

    aanmelding = MaaltijdAanmelding.object\
      .get(maaltijd_id=pk, user=request.profiel)

    aanmelding.delete()

    return Response({'details': 'Succesfully deleted'})
