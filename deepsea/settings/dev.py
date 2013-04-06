"""Settings for Development Server"""
from deepsea.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

VAR_ROOT = '/var/www/deepsea'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'deepsea',                      # Or path to database file if using sqlite3.
        'USER': 'root',
        # Not used with sqlite3.
        'PASSWORD': '',
        # Set to empty string for localhost. Not used with sqlite3.
        # 'HOST': '10.232.38.186',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# WSGI_APPLICATION = 'deepsea.wsgi.dev.application'
