from base.perms import *
from .models import *

PERMISSION_LOGICS = (
  (ForumDeel, DynamicConditionLogic(['forum.view_forumdeel'], 'rechten_lezen')),
  (ForumDeel, DynamicConditionLogic(['forum.moderate_forumdeel'], 'rechten_modereren')),
)
