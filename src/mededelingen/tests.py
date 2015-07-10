from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, APIClient
from base.models import Profiel
from mededelingen.models import Mededeling
from autofixture import AutoFixture

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

  def test_public_get_public(self):
    factory = APIRequestFactory()
    client = APIClient(factory)
    client.force_authenticate(user=None)
    response = client.get('http://testserver/api/v1/mededelingen/1/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_public_get_lid(self):
    factory = APIRequestFactory()
    client = APIClient(factory)
    client.force_authenticate(user=None)
    response = client.get('http://testserver/api/v1/mededelingen/2/')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_lid_get_lid(self):
    factory = APIRequestFactory()
    client = APIClient(factory)
    user = Profiel.objects.get(uid='0001')
    client.force_authenticate(user=user)
    response = client.get('http://testserver/api/v1/mededelingen/2/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_lid_get_public(self):
    factory = APIRequestFactory()
    client = APIClient(factory)
    user = Profiel.objects.get(uid='0001')
    client.force_authenticate(user=user)
    response = client.get('http://testserver/api/v1/mededelingen/1/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
