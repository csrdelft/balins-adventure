from django.http import *

import json

def json_response(data):
  return HttpResponse(json.dumps(data, indent=2), content_type="application/json")
