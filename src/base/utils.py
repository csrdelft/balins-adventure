from permission.utils.field_lookup import field_lookup
from django.core.exceptions import PermissionDenied
from django.conf import settings
import redis

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
