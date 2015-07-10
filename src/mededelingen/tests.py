from django.conf import urls
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate, APIClient
from base.models import Profiel
from mededelingen.models import Mededeling
from autofixture import AutoFixture

class MededelingTest(APITestCase, TestCase):

  def setUp(self):
    AutoFixture(Mededeling, generate_fk=True, field_values={
      'titel': 'Nice day today',
      'audience': 'LID'
    }).create(1)

    AutoFixture(Profiel, generate_fk=True, field_values={
      'uid': '0001',
      'status': 'LID'
    }).create(1)

  def test_titel(self):
    alpha = Mededeling.objects.get(pk=1)
    self.assertEqual(alpha.pk, 1)
    self.assertEqual(alpha.titel, 'Nice day today')

  def test_get_lid(self):
    # view = Mededeling.as_view()
    #
    # request = factory.get('/api/v1/mededelingen/1')
    # client = APIClient()
    # response = view(request)
    # print(response)

    factory = APIRequestFactory()
    client = APIClient(factory)
    user = Profiel.objects.get(uid='0001')
    client.force_authenticate(user=user)
    response = client.get('/api/v1/mededelingen')
    # print(response)
    # print(response.status_code)
    # self.assertEqual(response.titel, 'Nice day today')
    self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

