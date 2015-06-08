import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'nw_-0v1gumzd=w1l+fc8ji)5%7624%!mb0ha9i1i+iwdcrqg#!'

# session settings for php compatibility
# SESSION_ENGINE = 'base.sessions'
# SESSION_COOKIE_NAME = 'PHPSESSID'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'OPTIONS': {
      'context_processors': [
        'django.contrib.auth.context_processors.auth',
        'django.template.context_processors.debug',
        'django.template.context_processors.i18n',
        'django.template.context_processors.media',
        'django.template.context_processors.static',
        'django.template.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.template.context_processors.request',
      ],
      'loaders': [
        ('pyjade.ext.django.Loader', (
          'django.template.loaders.filesystem.Loader',
          'django.template.loaders.app_directories.Loader',
        )),
      ]
    },
  },
]

LEGACY_HOST = 'http://embed.csrdelft.nl'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_tables2',
    'django_extensions',
    'rest_framework',
    'permission',
    'base',
    'forum',
    'maaltijden'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'permission.backends.PermissionBackend',
)

HIJACK_LOGIN_REDIRECT_URL = '/'
REVERSE_HIJACK_LOGIN_REDIRECT_URL = '/'

REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.AllowAny',
  ),
  'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
  ),
  'DEFAULT_FILTER_BACKENDS': (
    'rest_framework.filters.DjangoFilterBackend',
  )
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'base.auth.SSHAPasswordHasher',
)

ROOT_URLCONF = 'csrdelft.urls'

WSGI_APPLICATION = 'csrdelft.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'csrdelft_django',
        'USER': 'csrdelft',
        'PASSWORD': 'bl44t'
    },
    'legacy': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'csrdelft',
        'USER': 'csrdelft',
        'PASSWORD': 'bl44t'
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'assets'),
)

STATIC_URL = '/static/'

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'handlers': {
    'console': {
      'class': 'logging.StreamHandler',
    },
  },
  'loggers': {
    'django': {
      'handlers': ['console'],
      'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
    },
    'root': {
      'handlers': ['console'],
      'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
    },
  },
}
