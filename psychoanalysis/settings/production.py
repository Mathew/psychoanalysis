import dj_database_url

from .base import *

DEBUG = TEMPLATE_DEBUG = True

DATABASES = {
    'default': dj_database_url.config(),
}
