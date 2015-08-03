from permission.logics import PermissionLogic
from permission.utils.field_lookup import field_lookup
from base.models import GROUP_STATUS_CHOICES, Lichting, LichtingLid, Bestuur, Commissie

import logging
logger = logging.getLogger(__name__)

class InGroupPermissionLogic(PermissionLogic):
  """ Non-object specific permission that grants permission if the user
      is in a given stek group (Bestuur/Kring/...) regardless of the object passed.
      So ONLY apply this logic to a model if the logic applies to every instance of this model.

      `get_group` should be a getter for said group that returns None on error.
      If the group is None, no permission is granted.
  """

  def __init__(self, grants, get_group):
    self.get_group = get_group
    self.grants = grants

  def has_perm(self, user, perm, obj=None):
    group = self.get_group()

    if not user.is_authenticated() or perm not in self.grants or group is None:
      return False

    # check if lid in group
    # if user is in group this logic grants permission for any passed object
    return group.leden.filter(user__user__pk=user.pk).exists()

    return False

class MatchFieldPermissionLogic(PermissionLogic):
  """ Permission logic focussed around granting view-, change- and/or delete permissions.
      Based on a user attribute that should match an object attribute

      example (match verticales to grant view rights on somemodel):
        MatchFieldPermissionLogic(
          grants=['somemodel.view'],
          user_attr='verticale',
          obj_attr='verticale',
        )

      IMPORTANT NOTE: this logic can easily be replaced by a (much more efficient) query that
      filters based on the field match, e.g:
      This is preferable and can e.g. be implemented on the model as:

      def get_viewable_by(self, user):
        return SomeModel.objects.filter(verticale=request.user.profiel.verticale)
  """

  def __init__(self, grants, user_attr, obj_attr):
    self.grants = grants
    self.user_attr = user_attr
    self.obj_attr = obj_attr

  def has_perm(self, user, perm, obj=None):
    if not user.is_authenticated() or perm not in self.grants:
      return False

    if obj is None:
      return True
    elif user.is_active and field_lookup(user, self.user_attr) == field_lookup(obj, self.obj_attr):
      return True

    return False

class DynamicConditionLogic(PermissionLogic):

  def __init__(self, grants, condition_field):
    self.grants = grants
    self.condition_field = condition_field

  def has_perm(self, user, perm, obj):
    # non authenticated users cannot gain access through dynamic conditions
    if not user.is_authenticated() or perm not in self.grants:
      return False

    if obj is None:
      return True
    else:
      conditions = field_lookup(obj, self.condition_field).split(',')

      # any of the following conditions can be true
      for cond in conditions:
        if self.check_dynamic_condition(user, field_lookup(obj, self.condition_field)):
          return True

    return False

  def check_dynamic_condition(self, user, condition):
    # empty conditions are easy
    if condition == "":
      return True

    try:
      parts = condition.split(':')

      # parse
      cond = parts[0].lower()
      if len(parts) > 1: value = parts[1]
      else: value = None
      if len(parts) > 2: role = parts[2].lower()
      else: role = None

      if cond == 'lidjaar' or cond == 'lichting':
        return user.profiel.lidjaar == int(value)
      elif cond == 'verticale':
        return user.profiel.verticale().naam.lower() == value.lower()
      elif cond == 'geslacht':
        return user.profiel.geslacht.lower() == value.lower()
      elif cond == 'eerstejaars':
        return LichtingLid.objects\
          .filter(user__user__pk=user.pk, lidjaar=Lichting.get_max_lidjaar()).exists()
      elif cond == 'ouderejaars':
        return not LichtingLid.objects\
          .filter(user__user__pk=user.pk, groep__lidjaar=Lichting.get_max_lidjaar())\
          .exists()
      elif cond == 'bestuur':
        if role is None: role = GROUP_STATUS_CHOICES.HT
        if role is not None and role in GROUP_STATUS_CHOICES:
          bestuur = Bestuur.objects.filter(status=role)
          return bestuur.leden.filter(user__user__pk=user.pk).exists()
      elif cond == 'commissie':
        if role is None: role = GROUP_STATUS_CHOICES.HT
        if role in GROUP_STATUS_CHOICES:
          com = Commissie.objects.filter(status=role, familie=value)
          return com.leden.filter(user__user__pk=user.pk).exists()

      # emulation of old mandatory access control permissions
      elif condition == 'P_LOGGED_IN':
        # non-authenticated users cannot gain dynamic access at all
        return True

      return False

    except Exception as e:
      return False
