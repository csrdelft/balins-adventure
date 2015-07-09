from base.perms import *
from mededelingen.models import Mededeling
from base.models import Bestuur

##########    WIP

def get_ht_bestuur(): return Bestuur.objects.get(status='ht')

PERMISSION_LOGICS = [(
  (Mededeling, InGroupPermissionLogic(['mededelingen.create', 'mededelingen.destroy'],get_ht_bestuur))
)]
