# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from local_settings import \
    LOCAL_DATABASES, LOCAL_MEDIA_ROOT, LOCAL_MEDIA_URL, LOCAL_STATIC_ROOT, \
    LOCAL_STATIC_URL, LOCAL_ADMIN_MEDIA_PREFIX, LOCAL_STATICFILES_DIRS, \
    LOCAL_TEMPLATE_DIRS, LOCAL_FIXTURE_DIRS, LOCAL_INSTALLED_APPS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Mika Nyman', 'mika.nyman@synapse-computing.com'),
)

MANAGERS = ADMINS

DATABASES = LOCAL_DATABASES

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
LANGUAGES = (
  ('fi', _('Finnish')),
  ('de', _('German')),
  ('en', _('English')),
)
MEDIA_ROOT = LOCAL_MEDIA_ROOT
MEDIA_URL = LOCAL_MEDIA_URL

STATIC_ROOT = LOCAL_STATIC_ROOT
STATIC_URL = LOCAL_STATIC_URL
ADMIN_MEDIA_PREFIX = LOCAL_ADMIN_MEDIA_PREFIX
STATICFILES_DIRS = LOCAL_STATICFILES_DIRS
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'pf4at9z(@vi^#ipk)7u#w(qal41b2a0b7&c1j_so4slrpk&9l&'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    # ---------- django-cms ----------
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'tallsmall.urls'

TEMPLATE_CONTEXT_PROCESSORS = {
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request', # added for grappelli + django-admin-tools
    'django.contrib.messages.context_processors.messages',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'tallsmall.context_processors.gen_view',
}
TEMPLATE_DIRS = LOCAL_TEMPLATE_DIRS
FIXTURE_DIRS = LOCAL_FIXTURE_DIRS
CMS_TEMPLATES = (
    ('etreg/etreg.html', 'ET Registration Form'),
)

# ---------- django-registration ----------
ACCOUNT_ACTIVATION_DAYS = 7

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
