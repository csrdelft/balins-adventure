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

    AutoFixture(Profiel, field_values={
      'voornaam': 'LID',
      'status': Profiel.STATUS.LID,
      'user': liduser,
      'uid': '0001'
    }).create(1)

    AutoFixture(Profiel, field_values={
      'voornaam': 'OUDLID',
      'status': Profiel.STATUS.OUDLID,
      'user': ouduser,
      'uid': '0002'
    }).create(1)

    AutoFixture(Profiel, field_values={
      'voornaam': 'BESTUURSLID',
      'status': Profiel.STATUS.LID,
      'user': bestuuruser,
      'uid': '0003'
    }).create(1)

    AutoFixture(Bestuur, field_values={
      'naam': 'van Heukelum',
      'status': 'ht'
    }).create(1)

    AutoFixture(BestuursLid, field_values={
      'user': Profiel.objects.get(uid='0003'),
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

    self.data = {
      'titel': 'E',
      'tekst': 'Newly posted Announcement',
      'prioriteit': '0',
      'user': '0003',
      'plaatje': 'NULL',
    }

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


  def test_lid_patch(self):
    self.fixture()
    self.client.login(username='Lid', password='Lid')

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('A', response.data['titel'])

    response_2 = self.client.patch(reverse('mededeling-detail', kwargs={'pk': 1}), {'titel':'D'})
    self.assertEqual(status.HTTP_403_FORBIDDEN, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response_3.status_code)
    self.assertEqual('A', response_3.data['titel'])

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

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('A', response.data['titel'])

    response_2 = self.client.patch(reverse('mededeling-detail', kwargs={'pk': 1}), {'titel':'D'})
    self.assertEqual(status.HTTP_200_OK, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response_3.status_code)
    self.assertEqual('D', response_3.data['titel'])


  def test_bestuur_delete(self):
    self.fixture()
    self.client.login(username='Bestuur', password='Bestuur')

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('A', response.data['titel'])

    response_2 = self.client.delete(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_204_NO_CONTENT, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_404_NOT_FOUND, response_3.status_code)

  def test_lid_delete(self):
    self.fixture()
    self.client.login(username='Lid', password='Lid')

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('A', response.data['titel'])

    response_2 = self.client.delete(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_403_FORBIDDEN, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response_3.status_code)
    self.assertEqual('A', response_3.data['titel'])

  def test_public_delete(self):
    self.fixture()

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response.status_code)
    self.assertEqual('A', response.data['titel'])

    response_2 = self.client.delete(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_403_FORBIDDEN, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}))
    self.assertEqual(status.HTTP_200_OK, response_3.status_code)
    self.assertEqual('A', response_3.data['titel'])


  def test_bestuur_post(self):
    self.fixture()
    self.client.login(username='Bestuur', password='Bestuur')

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 4}))
    self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    response_2 = self.client.post(reverse('mededeling-list'), self.data, format='json')
    self.assertEqual(status.HTTP_201_CREATED, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 4}))
    self.assertEqual(status.HTTP_200_OK, response_3.status_code)
    self.assertEqual('E', response_3.data['titel'])

  def test_lid_post(self):
    self.fixture()
    self.client.login(username='Lid', password='Lid')

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 4}))
    self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    response_2 = self.client.post(reverse('mededeling-list'), self.data, format='json')
    self.assertEqual(status.HTTP_403_FORBIDDEN, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 4}))
    self.assertEqual(status.HTTP_404_NOT_FOUND, response_3.status_code)

  def test_public_post(self):
    self.fixture()

    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 4}))
    self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    response_2 = self.client.post(reverse('mededeling-list'), self.data, format='json')
    self.assertEqual(status.HTTP_403_FORBIDDEN, response_2.status_code)

    response_3 = self.client.get(reverse('mededeling-detail', kwargs={'pk': 4}))
    self.assertEqual(status.HTTP_404_NOT_FOUND, response_3.status_code)
