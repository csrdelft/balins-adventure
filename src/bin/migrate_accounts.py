import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csrdelft.settings")
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from django.conf import settings
from django.contrib.auth.models import User
from base.models import Profiel
from legacy.models import Accounts

accounts = dict(map(lambda a: (a.uid, a), Accounts.objects.using('legacy').all()))
profielen = dict(map(lambda a: (a.uid, a), Profiel.objects.using('default').all()))

for uid, account in accounts.items():
  profiel = profielen.get(uid)

  # create the user that belongs with it
  user = User.objects.create(
    username = uid,
    email = account.email,
    password = "SSHA$" + account.pass_hash[6:], # strip off the hash alg and add it back properly
    first_name = profiel.voornaam,
    last_name = profiel.achternaam
  )
  user.save()
  profiel.user = user
  profiel.save(using='default')
