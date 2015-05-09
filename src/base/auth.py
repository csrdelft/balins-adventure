import hashlib
import base64
from django.contrib.auth.hashers import BasePasswordHasher, mask_hash
from collections import OrderedDict
from django.utils.translation import ugettext_noop as _

class SSHAPasswordHasher(BasePasswordHasher):
  """
  Stek legacy password hasher
  """
  algorithm = 'SSHA'

  def encode(self, password, salt, iterations=None):
    """
    Encodes the given password as a base64 SSHA hash+salt buffer
    as generously open sourced at https://gist.github.com/rca/7217540

    salt is overridden
    """
    assert password is not None
    assert salt and '$' not in salt

    salt = os.urandom(4)

    # hash the password and append the salt
    sha = hashlib.sha1(password)
    sha.update(salt)

    # create a base64 encoded string of the concatenated digest + salt
    digest_salt_b64 = base64.b64encode(sha.digest() + salt)

    # now tag the digest above with the SSHA tag
    tagged_digest_salt = 'SSHA${}'.format(digest_salt_b64)

    return tagged_digest_salt


  def verify(self, password, encoded):
    """
    Checks the OpenLDAP tagged digest against the given password
    as generously open sourced at https://gist.github.com/rca/7217540
    """
    # the entire payload is base64-encoded
    assert encoded.startswith('SSHA')

    # strip off the hash label
    digest_salt_b64 = encoded[5:]

    # the password+salt buffer is also base64-encoded.  decode and split the
    # digest and salt
    digest_salt = base64.b64decode(digest_salt_b64)
    digest = digest_salt[:20]
    salt = digest_salt[20:]

    sha = hashlib.sha1(password.encode('utf-8'))
    sha.update(salt)

    return digest == sha.digest()

  def safe_summary(self, encoded):
    # the entire payload is base64-encoded
    assert encoded.startswith('SSHA')

    # strip off the hash label
    digest_salt_b64 = encoded[5:]

    # the password+salt buffer is also base64-encoded.  decode and split the
    # digest and salt
    digest_salt = base64.b64decode(digest_salt_b64)
    digest = digest_salt[:20]
    salt = digest_salt[20:]

    return OrderedDict([
      (_('algorithm'), 'SSHA'),
      (_('iterations'), 0),
      (_('salt'), mask_hash(str(salt))),
      (_('hash'), mask_hash(str(digest))),
    ])
