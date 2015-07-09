from permission.utils.field_lookup import field_lookup
from django.core.exceptions import PermissionDenied
from django.conf import settings
import redis

class Choices(object):

  def __init__(self, **choices):
    # verify that all keys and values only appear once
    assert(len(set(choices.keys())) == len(choices), "Provided non-unique choice names")
    assert(len(set(choices.values())) == len(choices), "Provided non-unique choice names")

    self._choices = choices
    for k, v in choices.items():
      assert(k not in self.__dict__.keys(), "Invalid choice name: %s" % k)
      self.__dict__[k] = v

  def choices(self):
    """ Get list of database choices to be used on a database field
    """
    return ((v, k) for k, v in self._choices.items())

def accessor(fieldname):
  """ returns an accessor function for fieldname
      where fieldname can be a '_' seperated django field name
  """
  return lambda x: field_lookup(x, fieldname)

def grouped_dict(iterable):
  result = dict()

  for k, v in iterable:
    if k not in result:
      result[k] = [v]
    else:
      result[k].append(v)

  return result

def deny_on_fail(test):
  if(not test):
    raise PermissionDenied()

def notification_client():
  return redis.StrictRedis(
    host=settings.NOTIFICATION_REDIS_HOST,
    port=settings.NOTIFICATION_REDIS_PORT,
    db=settings.NOTIFICATION_REDIS_DB)
