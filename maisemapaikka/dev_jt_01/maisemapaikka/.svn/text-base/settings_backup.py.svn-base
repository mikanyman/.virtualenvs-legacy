# -*- coding: utf-8 -*-

import os
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

from local_settings import LOCAL_DEBUG, LOCAL_MEDIA_ROOT, LOCAL_MEDIA_URL, \
                           LOCAL_STATICFILES_DIRS, LOCAL_TEMPLATE_DIRS, \
                           LOCAL_DATABASES, LOCAL_STATIC_ROOT, LOCAL_STATIC_URL, \
                           LOCAL_INSTALLED_APPS, LOCAL_ADMIN_MEDIA_PREFIX
                           # LOCAL_TINYMCE_JS_URL, LOCAL_DATABASE_APPS_MAPPING,
                           # LOCAL_DATABASE_ROUTERS
                           
from django.utils.translation import ugettext_lazy as _

DEBUG = LOCAL_DEBUG
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

#DATABASE_ROUTERS = LOCAL_DATABASE_ROUTERS

#DATABASE_APPS_MAPPING = LOCAL_DATABASE_APPS_MAPPING

DATABASES = LOCAL_DATABASES

# Recommended: pip install pytz
#USE_TZ = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Helsinki'

DEFAULT_CHARSET = 'utf-8'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'


# django-cms
#LANGUAGES = (
#  ('fi', _('Finnish')),
#  ('sv', _('Swedish')),
#  ('en', _('English')),
#)
# changed to list form django-cms
LANGUAGES = [
  ('en', _('English')),
]

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = '/media/'
MEDIA_ROOT = LOCAL_MEDIA_ROOT
FILEBROWSER_MEDIA_ROOT = LOCAL_MEDIA_ROOT
#FILEBROWSER_MEDIA_ROOT = LOCAL_STATIC_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = LOCAL_MEDIA_URL
FILEBROWSER_MEDIA_URL = LOCAL_MEDIA_URL
#FILEBROWSER_MEDIA_URL = LOCAL_STATIC_URL

#DIRECTORY = FILEBROWSER_MEDIA_ROOT + 'uploads/'
#FILEBROWSER_DIRECTORY = 'C:/cygwin/home/mnyman/.virtualenvs/maisemapaikka/development/maisemapaikka/media/uploads/'
#FILEBROWSER_DIRECTORY = 'uploads/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = ''
STATIC_ROOT = LOCAL_STATIC_ROOT

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#STATIC_URL = '/static/'
STATIC_URL = LOCAL_STATIC_URL

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'
ADMIN_MEDIA_PREFIX = LOCAL_ADMIN_MEDIA_PREFIX

# Additional locations of static files
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
STATICFILES_DIRS = LOCAL_STATICFILES_DIRS

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# /static/filebrowser/
#FILEBROWSER_URL_FILEBROWSER_MEDIA = LOCAL_STATIC_URL + 'filebrowser/'
#URL_FILEBROWSER_MEDIA = FILEBROWSER_URL_FILEBROWSER_MEDIA

# C:/cygwin/home/mnyman/.virtualenvs/maisemapaikka/development/maisemapaikka/sitestatic/filebrowser/
#FILEBROWSER_PATH_FILEBROWSER_MEDIA = LOCAL_STATIC_ROOT + '/filebrowser/'
#PATH_FILEBROWSER_MEDIA = FILEBROWSER_PATH_FILEBROWSER_MEDIA

#URL_TINYMCE = getattr(settings, "FILEBROWSER_URL_TINYMCE", ADMIN_MEDIA_PREFIX + "tinymce/jscripts/tiny_mce/")
#PATH_TINYMCE = getattr(settings, "FILEBROWSER_PATH_TINYMCE", ADMIN_MEDIA_PREFIX + "tinymce/jscripts/tiny_mce/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'm7l=qcag4_diadki(@0)l505$iuobiq-*uxo36^@#ylvqt==lo'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
    #'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # one of the first, after session & cache
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'cms.middleware.multilingual.MultilingualURLMiddleware', # replaces LocaleMiddleware
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'maisemapaikka.urls'

TEMPLATE_CONTEXT_PROCESSORS = {
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request', # added for grappelli
    'django.contrib.messages.context_processors.messages',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'maisemapaikka.context_processors.cur_page',
}

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = LOCAL_TEMPLATE_DIRS

CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('portal/churches_frontpg.html', 'Churches Home'),
    ('portal/landscapes_frontpg.html', 'Landscapes Home'),
    ('portal/rockart_frontpg.html', 'Rockart Home'),
    #('template_2.html', 'Template Two'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

ROSETTA_MESSAGES_PER_PAGE = 30
ROSETTA_WSGI_AUTO_RELOAD = True
ROSETTA_EXCLUDED_APPLICATIONS = ()

#TINYMCE_JS_URL = LOCAL_TINYMCE_JS_URL
#TINYMCE_DEFAULT_CONFIG = {
#    'plugins': "table,spellchecker,paste,searchreplace",
#    'theme': "advanced",
#    'cleanup_on_startup': True,
#    'custom_undo_redo_levels': 10,
#}
#TINYMCE_SPELLCHECKER = True
#TINYMCE_COMPRESSOR = True

# for urls.py
#JS_ROOT = MEDIA_ROOT + 'js'

TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = STATIC_ROOT + '/tiny_mce'
TINYMCE_DEFAULT_CONFIG = {
    #'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'relative_urls': False
    #'cleanup_on_startup': True,
    #'custom_undo_redo_levels': 10,
    }
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = True
TINYMCE_FILEBROWSER = False

# django-registration
ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'info@synapse-computing.com'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # True = browser-length cookies
LOGIN_REDIRECT_URL = '/maisemapaikka/accounts/profiles/'

# django-profiles
#AUTH_PROFILE_MODULE = 'accounts.UserProfile'
AUTH_PROFILE_MODULE = 'profiles.UserProfile'

# filer
FILER_ENABLE_PERMISSIONS = True
    
INSTALLED_APPS = LOCAL_INSTALLED_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
