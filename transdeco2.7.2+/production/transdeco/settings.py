# Django settings for transdeco project.

from local_settings import \
    LOCAL_DEBUG, LOCAL_DATABASES, LOCAL_MEDIA_ROOT, LOCAL_MEDIA_URL, LOCAL_STATIC_ROOT, \
    LOCAL_STATIC_URL, LOCAL_ADMIN_MEDIA_PREFIX, LOCAL_STATICFILES_DIRS, \
    LOCAL_TEMPLATE_DIRS, LOCAL_FIXTURE_DIRS, LOCAL_INSTALLED_APPS

DEBUG = LOCAL_DEBUG
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Mika Nyman', 'mika.nyman@synapse-computing.com'),
)

MANAGERS = ADMINS
DATABASES = LOCAL_DATABASES
TIME_ZONE = 'Europe/Helsinki'
LANGUAGE_CODE = 'fi-fi'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = LOCAL_MEDIA_ROOT
MEDIA_URL = LOCAL_MEDIA_URL
STATIC_ROOT = LOCAL_STATIC_ROOT
STATIC_URL = LOCAL_STATIC_URL
ADMIN_MEDIA_PREFIX = LOCAL_ADMIN_MEDIA_PREFIX

SECRET_KEY = 'vt94+x8wzzbkzhv@9-1+=##steaei6)d5gy+$d2d#skgrhs_$4'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader', 
    #'django.template.loaders.eggs.Loader',
    #'django.template.loaders.cached.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'transdeco.urls'
TEMPLATE_DIRS = LOCAL_TEMPLATE_DIRS


TEMPLATE_CONTEXT_PROCESSORS = (
    # Defaults for Django 1.3
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request', # required by django-admin-tools
)

# Defaults for Django 1.3
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'    
    )

STATICFILES_DIRS = LOCAL_STATICFILES_DIRS
#CACHE_BACKEND = 'dummy:///'
FIXTURE_DIRS = LOCAL_FIXTURE_DIRS
INSTALLED_APPS = LOCAL_INSTALLED_APPS


