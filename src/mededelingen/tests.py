from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from base.models import Profiel, Bestuur, BestuursLid
from mededelingen.models import Mededeling
from autofixture import AutoFixture

class MededelingTests(APITestCase):

  def fixture(self):
    liduser = User.objects.create_user(username='Lid', password='Lid')
    ouduser = User.objects.create_user(username='OudLid', password='OudLid')
    bestuuruser = User.objects.create_user(username='Bestuur', password='Bestuur')
    superuser = User.objects.create_superuser(username='Superman', email='pubcie@csrdelft.nl', password='Superman')

    AutoFixture(Profiel, field_values={
      'voornaam': 'LID',
      'status': Profiel.STATUS.LID,
      'user': liduser
    }).create(1)

    AutoFixture(Profiel, field_values={
      'voornaam': 'OUDLID',
      'status': Profiel.STATUS.OUDLID,
      'user': ouduser
    }).create(1)

    AutoFixture(Profiel, field_values={
      'voornaam': 'SUPER',
      'status': Profiel.STATUS.LID,
      'user': superuser
    }).create(1)

    AutoFixture(Profiel, field_values={
      'voornaam': 'BESTUURSLID',
      'status': Profiel.STATUS.LID,
      'user': bestuuruser,
      'uid': '1234'
    }).create(1)

    AutoFixture(Bestuur, generate_fk=True, field_values={
      'naam': 'van Heukelum',
      'status': 'ht'
    }).create(1)

    AutoFixture(BestuursLid, field_values={
      'user': Profiel.objects.get(uid='1234'),
      'opmerking': 'Praeses van Heukelum',
      'groep_id': Bestuur.objects.get(status='ht')
    }).create(1)

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


  def test_public_gets_public(self):
    self.fixture()
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('A', response.data['titel'])

  def test_public_gets_lid(self):
    self.fixture()
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

  def test_public_gets_oudlid(self):
    self.fixture()
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 3}))
    self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


  def test_lid_gets_public(self):
    self.fixture()
    self.client.login(username='Lid', password='Lid')
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('A', response.data['titel'])

  def test_lid_gets_lid(self):
    self.fixture()
    self.client.login(username='Lid', password='Lid')
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('B', response.data['titel'])

  def test_lid_gets_oudlid(self):
    self.fixture()
    self.client.login(username='Lid', password='Lid')
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 3}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('C', response.data['titel'])


  def test_oudlid_gets_public(self):
    self.fixture()
    self.client.login(username='OudLid', password='OudLid')
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('A', response.data['titel'])

  def test_oudlid_gets_lid(self):
    self.fixture()
    self.client.login(username='OudLid', password='OudLid')
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

  def test_oudlid_gets_oudlid(self):
    self.fixture()
    self.client.login(username='OudLid', password='OudLid')
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 3}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('C', response.data['titel'])


  def test_superuser_patch(self):
    self.fixture()
    self.client.login(username='Superman', password='Superman')

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('B', response.data['titel'])

    response_2 = self.client.patch(reverse('mededeling-detail', kwargs={'pk': 2}), {'titel':'D'})
    self.assertEqual(status.HTTP_200_OK, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(status.HTTP_200_OK, response_3.status_code)
    self.assertEqual('D', response_3.data['titel'])

  def test_lid_patch(self):
    self.fixture()
    self.client.login(username='Lid', password='Lid')

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('B', response.data['titel'])

    response_2 = self.client.patch(reverse('mededeling-detail', kwargs={'pk': 2}), {'titel':'D'})
    self.assertEqual(status.HTTP_403_FORBIDDEN, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(status.HTTP_200_OK, response_3.status_code)
    self.assertEqual('B', response_3.data['titel'])

  def test_public_patch(self):
    self.fixture()

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('A', response.data['titel'])

    response_2 = self.client.patch(reverse('mededeling-detail', kwargs={'pk': 1}), {'titel':'D'})
    self.assertEqual(status.HTTP_403_FORBIDDEN, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response_3.status_code)
    self.assertEqual('A', response_3.data['titel'])

  def test_bestuur_patch(self):
    self.fixture()
    self.client.login(username='Bestuur', password='Bestuur')

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('B', response.data['titel'])

    response_2 = self.client.patch(reverse('mededeling-detail', kwargs={'pk': 2}), {'titel':'D'})
    self.assertEqual(status.HTTP_200_OK, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}))
    self.assertEqual(status.HTTP_200_OK, response_3.status_code)
    self.assertEqual('D', response_3.data['titel'])

