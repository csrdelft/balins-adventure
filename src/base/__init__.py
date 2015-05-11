from django.db.models.signals import post_migrate
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

import logging
logger = logging.getLogger(__name__)

DEFAULT_PERMISSIONS = (
  'change',
  'delete',
  'add',
  'view'
)

def add_view_permissions(sender, **kwargs):
  """
  This syncdb hooks takes care of adding a view permission too all our
  content types.
  """

  # for each of our content types
  for content_type in ContentType.objects.all():
    for perm in DEFAULT_PERMISSIONS:
      # build our permission slug
      codename = "%s_%s" % (perm, content_type.model)

      # if it doesn't exist..
      if not Permission.objects.filter(content_type=content_type, codename=codename):
        # add it
        Permission.objects.create(content_type=content_type,
          codename=codename,
          name="Can view %s" % content_type.name)

        logger.info("Added %s permission for %s" % (perm, content_type.name))

# check for all our view permissions after a syncdb
post_migrate.connect(add_view_permissions)
