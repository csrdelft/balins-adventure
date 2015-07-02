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
    return Maaltijd.objects\
      .prefetch_related("aanmeldingen")

  def list(self, *args, **kwargs):
    """ Maaltijd upcoming list
        ---
        parameters:
          - name: at
            paramType: query
            description: Give the upcoming list for `at` timestamp
            type: integer
    """
    at = self.request.query_params.get('at')
    if at is not None:
      at = datetime.fromtimestamp(int(at))
    else:
      at = datetime.now()

    mlten = self.get_queryset()\
      .filter(datum__gt=at)\
      .filter(datum__lt=at + timedelta(days=21))

    # only show those that fall within the permissions filter
    mlten = filter(lambda m: self.request.user.has_perm('maaltijden.view_maaltijd', m), mlten)

    serializer = self.get_serializer(mlten, many=True)
    return Response(serializer.data)

  @detail_route(methods=['post'])
  def aanmelden(self, request, pk):
    """ Maaltijd aanmelden
        ---
        parameters_strategy: replace
        parameters:
          - name: aantal_gasten
            required: true
            type: integer
          - name: gasten_eetwens
            required: true
            type: string
        responseMessages:
          - code: 200
            message: Succesfully aangemeld
        serializer: MaaltijdAanmeldingSerializer
    """
    mlt = self.get_object()

    # make sure the maaltijd isn't closed
    if mlt.gesloten:
      return Response({"details": "Maaltijd closed"}, status=status.HTTP_400_BAD_REQUEST)

    # check that the user can sign in on this one
    deny_on_fail(request.user.has_perm('maaltijden.view_maaltijd', mlt))

    request.data['user'] = request.profiel.pk
    request.data['maaltijd'] = pk

    serializer = MaaltijdAanmeldingSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(laatst_gewijzigd=datetime.now())
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  @detail_route(methods=['post'])
  def afmelden(self, request, pk):
    """ Maaltijd afmelden
        ---
        omit_serializer: true
        parameters_strategy: replace
        parameters: []
        responseMessages:
          - code: 200
            message: Succesfully afgemeld
          - code: 400
            message: Maaltijd closed
        type: {}
    """
    # make sure the maaltijd isn't closed
    if self.get_object().gesloten:
      return Response({"message": "Maaltijd closed"}, status=status.HTTP_400_BAD_REQUEST)

    aanmelding = MaaltijdAanmelding.object\
      .get(maaltijd_id=pk, user=request.profiel)

    aanmelding.delete()

    return Response({})
