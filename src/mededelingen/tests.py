from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase
from base.models import Profiel
from mededelingen.models import Mededeling
from autofixture import AutoFixture

class MededelingTests(APITransactionTestCase):
  def setUp(self):
    print(User.objects.all())
    liduser = User.objects.create_user(username="Lid", password="Lid")
    AutoFixture(Profiel, field_values={
      'naam': 'LID',
      'status': Profiel.STATUS.LID,
      'user_id': liduser.pk
    }).create(1)

    AutoFixture(Mededeling, generate_fk=True, field_values={
      'pk': 1,
      'titel': 'A',
      'audience': Mededeling.AUDIENCE.PUBLIC
    }).create(1)

    AutoFixture(Mededeling, generate_fk=True, field_values={
      'pk': 2,
      'titel': 'B',
      'audience': Mededeling.AUDIENCE.LEDEN
    }).create(1)

  def test_get_public_unauthed(self):
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}), {})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['titel'], 'A')

  def test_get_public_authed(self):
    self.client.login(username="Lid", password="Lid")
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 1}), {})
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_get_lid_unauthed(self):
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}), {})
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  def test_get_lid_authed(self):
    self.client.login(username="Lid", password="Lid")
    response = self.client.get(reverse('mededeling-detail', kwargs={'pk': 2}), {})
    self.assertEqual(response.status_code, status.HTTP_200_OK)

