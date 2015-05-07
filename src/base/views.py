from django.shortcuts import render
from django.template import loader, RequestContext

DEFAULT_TITLE = "Civitas Studiosorum Reformatorum"

def render_with_layout(request, template, ctx={}, title=DEFAULT_TITLE):
  """ Renders content in the csr layout
  """
  t = loader.get_template(template)
  r = t.render(ctx, request)

  return render(request, 'index.jade', {"content": r, "title": title})

def index(request):
  return render_with_layout(request, 'main.jade')
