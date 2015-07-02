from permission.logics import PermissionLogic
from permission.utils.field_lookup import field_lookup
from base.utils import accessor
from django.core.exceptions import PermissionDenied

import logging
logger = logging.getLogger(__name__)

class MatchFieldPermissionLogic(PermissionLogic):
  """ Permission logic focussed around granting view-, change- and/or delete permissions.
      Based on a user attribute that should match an object attribute

      example (match verticales to grant view rights on somemodel):
        MatchAttributePermissionLogic(
          grants=['somemodel.view'],
          user_attr='verticale',
          obj_attr='verticale',
        )
  """

  def __init__(self, grants, user_attr, obj_attr):
    self.grants = grants
    self.user_attr = user_attr
    self.obj_attr = obj_attr

  def has_perm(self, user, perm, obj=None):
    if not user.is_authenticated() or perm not in grants:
      return False

    if obj is None:
      return True
    elif user.is_active and lookup_field(user, self.user_attr) == lookup_field(obj, self.obj_attr):
      return True

    return False

class DynamicConditionLogic(PermissionLogic):

  def __init__(self, grants, condition_field):
    self.grants = grants
    self.condition_field = condition_field

  def has_perm(self, user, perm, obj):
    if not user.is_authenticated() or perm not in self.grants:
      return False

    if obj is None:
      return True
    else:
      return self.check_dynamic_condition(user, field_lookup(obj, self.condition_field))

    return False

  def check_dynamic_condition(self, user, condition):
    # empty conditions are easy
    if condition == "":
      return True

    try:
      cond, value = condition.split(':', 1)

      if cond == 'lidjaar':
        return user.profiel.lidjaar == int(value)
      elif cond == 'verticale':
        return user.profiel.verticale().naam.upper() == value.upper()

      return False
    except Exception as e:
      return False
