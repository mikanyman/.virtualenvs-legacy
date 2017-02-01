# synapse/settings.py

from local_settings import LOCAL_DEBUG, LOCAL_DATABASES, \
        LOCAL_MEDIA_ROOT, LOCAL_MEDIA_URL, LOCAL_STATIC_ROOT, LOCAL_STATIC_URL, LOCAL_STATICFILES_DIRS, \
        LOCAL_ADMIN_MEDIA_PREFIX, LOCAL_TEMPLATE_DIRS

import os
from django.utils.translation import gettext_lazy as _

cur_dir = os.getcwd()

DEBUG = LOCAL_DEBUG
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Mika Nyman', 'mika.nyman@synapse-computing.com'),
)

MANAGERS = ADMINS

DATABASES = LOCAL_DATABASES

#DATABASE_ENGINE = 'postgresql_psycopg2' # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = 'synapse'               # Or path to database file if using sqlite3.
#DATABASE_USER = 'synapse'               # Not used with sqlite3.
#DATABASE_PASSWORD = 'synapse'           # Not used with sqlite3.
#DATABASE_HOST = '127.0.0.1'             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = '5432'                  # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Helsinki'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en' # en-gb en-GB en

# default site
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#if cur_dir == '/':
#    MEDIA_ROOT = '/var/django/synapse/site_media/'
#elif cur_dir.startswith('C:\\'):
#    MEDIA_ROOT = 'C:/eclipse/workspace/a46.myrootshell.com/synapse/site_media/'
MEDIA_ROOT = LOCAL_MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#if cur_dir == '/':
#     MEDIA_URL = 'http://synapse.coreference.org/site_media/'
#elif cur_dir.startswith('C:\\'):
#     MEDIA_URL = 'http://127.0.0.1:8000/site_media/'
MEDIA_URL = LOCAL_MEDIA_URL

STATIC_ROOT = LOCAL_STATIC_ROOT
STATIC_URL = LOCAL_STATIC_URL
STATICFILES_DIRS = LOCAL_STATICFILES_DIRS

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/admin_media/'
ADMIN_MEDIA_PREFIX = LOCAL_ADMIN_MEDIA_PREFIX

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i6^h0j4-c#2!$m8#og$yd)8g)n*t_w*x2q!r^rgo-7%&g9#&f*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.core.context_processors.auth',
#    'django.core.context_processors.request',
#)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

LANGUAGE_COOKIE_NAME = 'django_language'

LANGUAGES = (
    ('en', _('English')),
    ('fi', _('Finnish')),
    ('sv', _('Swedish')),
)

ROOT_URLCONF = 'synapse.urls'

#if cur_dir == '/':
#    TEMPLATE_DIRS = (
#        '/var/django/synapse/templates',
#        '/usr/lib/python2.5/site-packages/photologue/templates/photologue'
#    )
#elif cur_dir.startswith('C:\\'):
#    TEMPLATE_DIRS = (
#        'C:/eclipse/workspace/a46.myrootshell.com/synapse/templates',
#        'C:/Python25/Lib/site-packages/photologue/templates/photologue'
#    )
    
TEMPLATE_DIRS = LOCAL_TEMPLATE_DIRS


TINYMCE_JS_URL = 'http://synapse.coreference.org/js/tiny_mce/tiny_mce.js'
if cur_dir == '/':
    TINYMCE_JS_ROOT = '/var/www/js/tiny_mce'
    #PHOTOLOGUE_ROOT = '/usr/lib/python2.5/site-packages/photologue'
elif cur_dir.startswith('C:\\'):
    TINYMCE_JS_ROOT = 'C:/www/js/tiny_mce' # 'C:/www/js/tiny_mce'
    #PHOTOLOGUE_ROOT = 'C:/Python25/Lib/site-packages/photologue'
    
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = True
TINYMCE_FILEBROWSER = False    
#TINYMCE_DEFAULT_CONFIG = {'theme': "simple", 'relative_urls': False}

if cur_dir == '/':
    FIXTURE_DIRS = (
        '/var/django/synapse/pages/fixtures'
    )
elif cur_dir.startswith('C:\\'):
    FIXTURE_DIRS = (
        'C:/eclipse/workspace/a46.myrootshell.com/synapse/pages/fixtures'
    )
    
AUTH_PROFILE_MODULE = "accounts.UserProfile"
    
INSTALLED_APPS = (
    #'grappelli.dashboard',
    #'grappelli', # before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.webdesign',
    #'filebrowser',
    #'tabs',
    #'photologue',
    #'rosetta',
    #'tagging',
    #'tinymce',
    #'synapse.accounts',
    #'synapse.pages',
    #'synapse.listbase',
    #'synapse.modules',
    #'synapse.segments'
)

