from django.db import models
from base.models import Profiel

class Accounts(models.Model):
  uid = models.ForeignKey(Profiel, db_column='uid', primary_key=True)
  username = models.CharField(unique=True, max_length=255)
  email = models.CharField(max_length=255)
  pass_hash = models.CharField(max_length=255)
  pass_since = models.DateTimeField()
  last_login_success = models.DateTimeField(blank=True, null=True)
  last_login_attempt = models.DateTimeField(blank=True, null=True)
  failed_login_attempts = models.IntegerField()
  blocked_reason = models.TextField(blank=True)
  perm_role = models.CharField(max_length=9)
  private_token = models.CharField(max_length=255, blank=True)
  private_token_since = models.DateTimeField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'accounts'

