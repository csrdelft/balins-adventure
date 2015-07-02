from base.perms import *
from .models import *

PERMISSION_LOGICS = (
  (Maaltijd, DynamicConditionLogic(['maaltijden.view_maaltijd'], 'aanmeld_filter')),
)
