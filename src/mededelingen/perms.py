from base.perms import *
from mededelingen.models import Mededeling
from base.models import Bestuur

##########    WIP

def get_ht_bestuur(): return Bestuur.objects.get(status='ht')

PERMISSION_LOGICS = (
  (Mededeling, DynamicConditionLogic(['mededeling.add_mededeling'], 'rechten_toevoegen')),
  (Mededeling, DynamicConditionLogic(['mededeling.delete_mededeling'], 'rechten_verwijderen')),
  (Mededeling, DynamicConditionLogic(['mededeling.view_mededeling'], 'rechten_lezen')),
  (Mededeling, DynamicConditionLogic(['mededeling.change_mededeling'], 'rechten_veranderen')),
  (Mededeling, InGroupPermissionLogic(['mededelingen.add_mededeling'], get_ht_bestuur)),
  (Mededeling, InGroupPermissionLogic(['mededelingen.change_mededeling'], get_ht_bestuur())),
  (Mededeling, InGroupPermissionLogic(['mededelingen.delete_mededeling'], get_ht_bestuur())),
  (Mededeling, MatchFieldPermissionLogic(
          grants=['mededelingen.view'],
          user_attr='profiel__lidstatus',
          obj_attr='zichtbaarheid',
        )),
)


