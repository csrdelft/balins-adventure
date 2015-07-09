from base.perms import *
from mededelingen.models import Mededeling
from base.models import Bestuur

def get_ht_bestuur(): return Bestuur.objects.get(status='ht')

PERMISSION_LOGICS = [
  (Mededeling, InGroupPermissionLogic(
    [ 'mededelingen.add_mededeling',
      'mededelingen.delete_mededeling',
      'mededelingen.change_mededeling' ]
    , get_ht_bestuur)
  )
]
