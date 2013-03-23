from .base import *

DEBUG = TEMPLATE_DEBUG = True

INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
    'south',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'psychoanalysis',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'psychoanalysis',
        'PASSWORD': 'psychoanalysis',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Debug Toolbar IPs.
INTERNAL_IPS = (
    '33.33.33.1',
    '33.33.33.10',
    '127.0.0.1',
)
