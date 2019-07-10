from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'test',
        'PORT': '',
        'TEST': {'NAME': ':memory:'}
    }
}
