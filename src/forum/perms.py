from base.perms import *
from .models import *

PERMISSION_LOGICS = (
  (ForumDeel, DynamicConditionLogic(['forum.view_forumdeel'], 'rechten_lezen')),
  (ForumDeel, DynamicConditionLogic(['forum.moderate_forumdeel'], 'rechten_modereren')),
  (ForumDeel, DynamicConditionLogic(['forum.post_in_forumdeel'], 'rechten_posten')),
  (ForumPost, MatchFieldPermissionLogic(['forum.delete_forumpost'], 'profiel__uid', 'user_id')),
)
