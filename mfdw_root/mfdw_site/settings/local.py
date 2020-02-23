from .base import *

DEBUG = True
ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('PGSQL_DB_NAME'),
        'USER': os.environ.get('PGSQL_DB_USER'),
        'PASSWORD': os.environ.get('PGSQL_DB_PASW'),
        'HOST': os.environ.get('PGSQL_DB_HOST'),
        'PORT': os.environ.get('PGSQL_DB_PORT')
    }
}