from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
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
      'status': 'OUD'
    }).create(1)

  def test_titel(self):
    alpha = Mededeling.objects.get(pk=1)
    self.assertEqual(alpha.pk, 1)
    self.assertEqual(alpha.titel, 'Nice day today')

  # def test_post_bestuur(self):
  #   factory = APIRequestFactory()
  #   user = Profiel.objects.get(uid='0001')
  #   view = Mededeling.as_view()
  #
  #   request = factory.get('/api/v1/mededelingen/1')
  #   force_authenticate(request,user=user)
  #   response = view(request)
  #   print(response)
