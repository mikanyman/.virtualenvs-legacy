# Django settings for transdeco project.

import os
cur_dir = os.getcwd()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

#if cur_dir.startswith('C:\\'):
#    DATABASE_ENGINE = 'sqlite3' # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
#    DATABASE_NAME = 'C:\Application Data\sqlite3\sqlite3_transdeco.db'             # Or path to database file if using sqlite3.    
#else:
#    DATABASE_USER = 'transdeco'             # Not used with sqlite3.
#    DATABASE_PASSWORD = 'transdeco'         # Not used with sqlite3.
#    DATABASE_HOST = '127.0.0.1'             # Set to empty string for localhost. Not used with sqlite3.
#    DATABASE_PORT = '5432'                  # Set to empty string for default. Not used with sqlite3.

db_path = cur_dir + '/sqlite/transdeco.sqlite'

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'transdeco',
    #    'USER': 'transdeco',
    #    'PASSWORD': 'transdeco',
    #    'HOST': '127.0.0.1',
    #    'PORT': '5432'
    #}
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/mnyman/.virtualenvs/transdeco/staging/transdeco/sqlite/transdeco.sqlite',
        #'NAME': db_path,
    }
}


# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Helsinki'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'fi-fi'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = '/var/cherokee/transdeco/'
#if cur_dir == '/var/django/transdeco':
#    MEDIA_ROOT = '/var/cherokee/transdeco/site_media/'
#elif cur_dir.startswith('C:\\'):
#    MEDIA_ROOT = 'C:/eclipse/workspace/a29.myrootshell.com/transdeco/site_media/'

#if cur_dir == '/home/mnyman/.virtualenvs/transdeco/staging/transdeco/':
#MEDIA_ROOT = '/var/cherokee/transdeco/staging/site_media/'
#MEDIA_URL = 'http://a29.myrootshell.com:8080/site_media/transdeco/staging/site_media/'
#else:
#MEDIA_ROOT = '/var/cherokee/transdeco/production/site_media'
#MEDIA_URL = 'http://www.transdeco.fi:8080/transdeco/staging/site_media/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
#MEDIA_URL = 'http://a29.myrootshell.com:8080/site_media/'
#if cur_dir == '/var/django/transdeco':
#     MEDIA_URL = 'http://a29.myrootshell.com:8080/site_media/'
#elif cur_dir.startswith('C:\\'):
#     MEDIA_URL = 'http://127.0.0.1:8000/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'vt94+x8wzzbkzhv@9-1+=##steaei6)d5gy+$d2d#skgrhs_$4'

# List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.load_template_source',
#    'django.template.loaders.app_directories.load_template_source',
#    'django.template.loaders.eggs.load_template_source',
#)

# Django 1.3 default
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'transdeco.middleware.ViewCountMiddleware',
)

ROOT_URLCONF = 'transdeco.urls'

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
if cur_dir.startswith('C:'):
    TEMPLATE_DIRS = (
        'C:/cygwin/home/mnyman/.virtualenvs/transdeco/staging/transdeco/templates',
    )
else:
    TEMPLATE_DIRS = (
        '/home/mnyman/.virtualenvs/transdeco/staging/transdeco/templates',
    )

# Defaults for Django 1.3
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)
TEMPLATE_CONTEXT_PROCESSORS += (
    'transdeco.context_processors.deployment_mode',
)

# Defaults for Django 1.3
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'    
    )
STATIC_ROOT = '/cygwin/home/mnyman/.virtualenvs/transdeco/staging/static/'

STATICFILES_DIRS = (
    '/cygwin/home/mnyman/.virtualenvs/transdeco/staging/transdeco/site_media/',
    )

STATIC_URL = '/site_media/'
#STATIC_URL = 'http://a29.myrootshell.com:8080/transdeco/staging/site_media/' # staging, production

CACHE_BACKEND = 'dummy:///'

FIXTURE_DIRS = (
    '/home/mnyman/.virtualenvs/transdeco/staging/transdeco/counter/fixtures/',
    '/home/mnyman/.virtualenvs/transdeco/staging/transdeco/flatpages/fixtures/',
    '/home/mnyman/.virtualenvs/transdeco/staging/transdeco/galleria/fixtures/',
)

#if cur_dir == '/var/django/transdeco':
#    FIXTURE_DIRS = (
#        '/var/django/transdeco/counter/fixtures',
#        '/var/django/transdeco/galleria/fixtures'
#    )
#elif cur_dir.startswith('C:\\'):
#    FIXTURE_DIRS = (
#        'C:/eclipse/workspace/a29.myrootshell.com/transdeco/counter/fixtures', 
#        'C:/eclipse/workspace/a29.myrootshell.com/transdeco/galleria/fixtures'
#    )

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'transdeco.counter',
    'transdeco.flatpages',
    'transdeco.galleria',
    #'transdeco.rdf',
    'transdeco.taglibrary',
)
