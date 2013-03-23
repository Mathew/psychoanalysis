import dj_database_url

from .base import *

DEBUG = TEMPLATE_DEBUG = True

print dj_database_url.config()
DATABASES = {
    'default': dj_database_url.config(),
}
