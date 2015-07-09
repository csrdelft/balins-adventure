from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from mededelingen.models import Mededeling
from autofixture import AutoFixture
from datetime import datetime

class MededelingTest(TestCase):

  def setUp(self):
    mededelingen = AutoFixture(Mededeling, generate_fk=True, field_values={
      'titel': 'Nice day today'
    }).create(1)

  def titelTest(self):
    alpha = Mededeling.objects.get(pk=1)
    self.assertEqual(alpha.pk, 1)
    self.assertEqual(alpha.titel, 'Nice day today')

