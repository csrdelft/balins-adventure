from django.test import TestCase
from mededelingen.models import Mededeling
from autofixture import AutoFixture
class MededelingTest(TestCase):

  def setUp(self):
    AutoFixture(Mededeling, generate_fk=True, field_values={
      'titel': 'Nice day today'
    }).create(1)

  def test_titel(self):
    alpha = Mededeling.objects.get(pk=1)
    self.assertEqual(alpha.pk, 1)
    self.assertEqual(alpha.titel, 'Nice day today')


