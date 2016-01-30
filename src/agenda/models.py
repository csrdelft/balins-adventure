from __future__ import unicode_literals
from django.db import models

class Agenda(models.Model):
  id = models.AutoField(primary_key=True, db_column='item_id')
  begin_moment = models.DateTimeField()
  eind_moment = models.DateTimeField()
  beschrijving = models.TextField(blank=True)
  locatie = models.CharField(max_length=255, blank=True)
  titel = models.CharField(max_length=255)
  rechten_bekijken = models.CharField(max_length=255)
  link = models.CharField(max_length=255, blank=True)

  def __str__(self):
    return "%s" % (self.titel)

  class Meta:
    db_table = 'agenda'

class AgendaVerbergen(models.Model):
  uid = models.CharField(max_length=4)
  uuid = models.CharField(max_length=255)

  class Meta:
    db_table = 'agenda_verbergen'
    unique_together = (('uid', 'uuid'),)
