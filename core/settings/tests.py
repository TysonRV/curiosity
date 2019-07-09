from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test',
        'PORT': '',
        'TEST': {'NAME': ':memory:'}
    }
}
