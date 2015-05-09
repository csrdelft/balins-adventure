from permission.utils.field_lookup import field_lookup

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
