from datetime import datetime
from django.test import TestCase
import null
from rest_framework.test import APIRequestFactory
from mededelingen.models import Mededeling

# Create your tests here.
class MededelingTest(TestCase):

  def setUp(self):
    Mededeling.objects.create(
      id='1',
      live=True,
      datum=datetime.now,
      vervaltijd=null,
      titel='Test',
      tekst='Test text',
      prioriteit='1',
      user='1414',
      plaatje='groen',
      audience='LID'
    )

  def titelTest(self):
    alpha = Mededeling.objects.get(id='1')
    self.assertEqual(alpha.id,'1')


