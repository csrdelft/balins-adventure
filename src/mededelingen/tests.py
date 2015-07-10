from django.test import TestCase
from django.test.client import ClientHandler
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase, APIClient
from base.middleware import ProfielMiddleware
from base.models import Profiel
from mededelingen.api import MededelingenViewSet
from mededelingen.models import Mededeling
from autofixture import AutoFixture
from mock import Mock

class MededelingTest(APITestCase, TestCase):

  def setUp(self):
    AutoFixture(Mededeling, generate_fk=True, field_values={
      'titel': 'A',
      'audience': 'PUB'
    }).create(1)

    AutoFixture(Mededeling, generate_fk=True, field_values={
      'titel': 'B',
      'audience': 'LID'
    }).create(1)

    AutoFixture(Profiel, generate_fk=True, field_values={
      'uid': '0001',
      'status': 'LID'
    }).create(1)

    AutoFixture(Profiel, generate_fk=True, field_values={
      'uid': 'x999',
      'status': 'NOB'
    }).create(1)

    self.factory = APIRequestFactory()
    self.client = APIClient(self.factory)
    self.user = Profiel.objects.get(uid='0001')

  def test_public_get_public(self):
    requestPUB = self.client.get('/api/v1/mededelingen/1/')
    self.assertEqual(requestPUB.status_code, status.HTTP_200_OK)

  def test_public_get_lid(self):
    requestLID = self.client.get('/api/v1/mededelingen/2/')
    self.assertEqual(requestLID.status_code, status.HTTP_404_NOT_FOUND)

  def test_lid_get_lid(self):
    self.client.force_authenticate(user=self.user)
    requestLID = self.client.get('/api/v1/mededelingen/2/')
    self.assertEqual(requestLID.status_code, status.HTTP_200_OK)

  def test_lid_get_public(self):
    self.client.force_authenticate(user=self.user)
    requestPUB = self.client.get('/api/v1/mededelingen/1/')
    self.assertEqual(requestPUB.status_code, status.HTTP_200_OK)
