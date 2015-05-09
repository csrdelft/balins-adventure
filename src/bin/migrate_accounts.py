import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csrdelft.settings")
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from django.conf import settings
from legacy.models import Accounts

print(Accounts.objects.using('legacy').all()[0:10])
