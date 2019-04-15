"""
Local Django settings.
"""

from settings.common import *

SECRET_KEY = 'SECRET_KEY'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DATABASE_NAME',
        'USER': 'DATABASE_USER',
        'PASSWORD': 'DATABASE_PASSWORD',
        'HOST': 'DATABASE_HOST',
        'PORT': 'DATABASE_PORT',
    }
}
