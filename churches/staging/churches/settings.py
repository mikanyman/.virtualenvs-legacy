import os
from django.utils.translation import ugettext_lazy as _

# ---------- roots ----------
if os.name == 'nt':
    VIRTUALENVS_ROOT = 'C:/cygwin/home/mnyman/.virtualenvs'
    PROJECT_ROOT = 'C:/cygwin/home/mnyman/.virtualenvs/churches/development/churches'
    URL_ROOT = ''
if os.name == 'posix':
    VIRTUALENVS_ROOT = '/home/mnyman/.virtualenvs'
    PROJECT_ROOT = '/home/mnyman/.virtualenvs/churches/staging/churches'
    URL_ROOT = 'http://a199.myrootshell.com:8080/churches/staging'


# ---------- site ----------
SITE_ID = 1
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    # ('Mika Nyman', 'info@synapse-computing.com'),
)
MANAGERS = ADMINS

# ---------- databases ----------
if os.name == 'nt':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'C:/cygwin/home/mnyman/.virtualenvs/churches/development/sqlite/churches.sqlite',
        }
    }
if os.name == 'posix':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'churches',
            'USER': 'churches',
            'PASSWORD': 'churches',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

# ---------- locale ----------
TIME_ZONE = 'Europe/Helsinki'
LANGUAGE_CODE = 'en-us'
LANGUAGES = [
  ('en', _('English')),
  ('fi', _('Finnish')),
  ('sv', _('Swedish')),
]
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ---------- media ----------
MEDIA_ROOT = '%s/media/' % PROJECT_ROOT
MEDIA_URL = '/media/'
if os.name == 'nt':
    STATIC_ROOT = '%s/sitestatic/' % PROJECT_ROOT
    STATIC_URL = '/static/'
if os.name == 'posix':
    STATIC_ROOT = '%s/sitestatic/' % PROJECT_ROOT
    STATIC_URL = '%s/static/' % URL_ROOT


STATICFILES_DIRS = (
    PROJECT_ROOT + '/static',
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = '8#&amp;@9y$#&amp;8=tq$jyf*cc%av3i$ngbg#*l3w(-5nq9ml^um46dq'

# List of callables that know how to import templates from various sources.
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
    'django.middleware.locale.LocaleMiddleware', # one of the first, after session & cache
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'userena.middleware.UserenaLocaleMiddleware', # django-userena, at the end
)

ROOT_URLCONF = 'churches.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'churches.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'churches.context_processors.gen_view',
)

if os.name == 'nt':
    TEMPLATE_DIRS = (
        'C:/cygwin/home/mnyman/.virtualenvs/churches/development/churches/templates'
    )
if os.name == 'posix':
    TEMPLATE_DIRS = (
        '/home/mnyman/.virtualenvs/churches/staging/churches/templates'
    )

# ---------- django-userena ----------
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PROFILE_MODULE = 'profiles.Profile'

LOGIN_REDIRECT_URL = '/en/list/' #'/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

ANONYMOUS_USER_ID = -1
USERENA_DISABLE_PROFILE_LIST = True
USERENA_MUGSHOT_SIZE = 140


# ---------- email ----------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # default
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'maisemapaikka@gmail.com'
EMAIL_HOST_PASSWORD = 'maisema2012paikka'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    
    # ---------- django-userena ----------
    'easy_thumbnails',
    'guardian',
    'userena',
    'userena.contrib.umessages',
    'churches.profiles',
    
    # ---------- apps ----------
    'churches.apps.rules',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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
