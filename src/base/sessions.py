""" Initially taken from https://github.com/winhamwr/django-php-bridge
"""
import phpserialize

from django.contrib.sessions.backends.db import SessionStore as DbStore

class SessionStore(DbStore):
    def __init__(self, session_key=None):
        super(SessionStore, self).__init__(session_key)

    def decode(self, session_data):
        return phpserialize.loads(session_data)

    def encode(self, session_dict):
        return phpserialize.dumps(session_dict)
