# encoding:utf-8
import os
import urlparse
import sys
import os.path

SITE_SRC_ROOT = os.path.dirname(__file__)
LOG_FILENAME = 'django.osqa.log'

#for logging
import logging
logging.basicConfig(
    filename=os.path.join(SITE_SRC_ROOT, 'log', LOG_FILENAME),
    level=logging.ERROR,
    format='%(pathname)s TIME: %(asctime)s MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s',
)

#ADMINS and MANAGERS
ADMINS = (
        #('Ntino', 'agbiotec@yahoo.com'),
        )
MANAGERS = ADMINS

DEBUG = False
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': True
}
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

# Register database schemes in URLs.
urlparse.uses_netloc.append('postgres')
urlparse.uses_netloc.append('mysql')

try:
    # Check to make sure DATABASES is set in settings.py file.
    # If not default to {}


    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "osqa_backup_migrated_02052013",
            "USER": "kkrampis",
            "PASSWORD": "",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }

except Exception:
        print 'Unexpected error:', sys.exc_info()


CACHE_BACKEND = 'file://%s' % os.path.join(os.path.dirname(__file__),'cache').replace('\\','/')
#CACHE_BACKEND = 'dummy://'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# This should be equal to your domain name, plus the web application context.
# This shouldn't be followed by a trailing slash.
# I.e., http://www.yoursite.com or http://www.hostedsite.com/yourhostapp
APP_URL = 'http://evening-lowlands-7532.herokuapp.com/'

#LOCALIZATIONS
TIME_ZONE = 'America/New_York'

#OTHER SETTINGS

USE_I18N = True
LANGUAGE_CODE = 'en'

DJANGO_VERSION = 1.1
OSQA_DEFAULT_SKIN = 'default'

DISABLED_MODULES = ['books', 'recaptcha', 'project_badges', 'sphinxfulltext', 'pgfulltext']
