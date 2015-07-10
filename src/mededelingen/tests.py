from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from base.models import Profiel
from mededelingen.models import Mededeling
from autofixture import AutoFixture

class MededelingTests(APITestCase):

  def fixture(self):
    liduser = User.objects.create_user(username="Lid", password="Lid")
    ouduser = User.objects.create_user(username='OudLid', password='OudLid')

    AutoFixture(Profiel, field_values={
      'voornaam': 'LID',
      'status': Profiel.STATUS.LID,
      'user': liduser,
    }).create(1)

    AutoFixture(Profiel, field_values={
      'voornaam': 'OUDLID',
      'status': Profiel.STATUS.OUDLID,
      'user': ouduser
    }).create(1)
    print(Profiel.objects.all().values('pk', 'user_id', 'status'))

    AutoFixture(Mededeling, generate_fk=True, field_values={
      'pk': 1,
      'titel': 'A',
      'audience': Mededeling.AUDIENCE.PUBLIC,
      'live': True
    }).create(1)

    AutoFixture(Mededeling, generate_fk=True, field_values={
      'pk': 2,
      'titel': 'B',
      'audience': Mededeling.AUDIENCE.LEDEN,
      'live': True
    }).create(1)

    AutoFixture(Mededeling, generate_fk=True, field_values={
      'pk': 3,
      'titel': 'C',
      'audience': Mededeling.AUDIENCE.OUDLEDEN,
      'live': True
    }).create(1)

    print(Mededeling.objects.all().values('pk', 'live', 'audience'))

  def test_public_gets_public(self):
    self.fixture()
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['titel'], 'A')

  def test_public_gets_lid(self):
    self.fixture()
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_public_gets_oudlid(self):
    self.fixture()
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 3}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


  def test_lid_gets_public(self):
    self.fixture()
    self.client.login(username="Lid", password="Lid")
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['titel'], 'A')

  def test_lid_gets_lid(self):
    self.fixture()
    self.client.login(username="Lid", password="Lid")
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['titel'], 'B')

  def test_lid_gets_oudlid(self):
    self.fixture()
    self.client.login(username="Lid", password="Lid")
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 3}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['titel'], 'C')


  def test_oudlid_gets_public(self):
    self.fixture()
    self.client.login(username="OudLid", password="OudLid")
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['titel'], 'A')

  def test_oudlid_gets_lid(self):
    self.fixture()
    self.client.login(username="OudLid", password="OudLid")
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_oudlid_gets_oudlid(self):
    self.fixture()
    self.client.login(username="OudLid", password="OudLid")
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 3}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['titel'], 'C')

