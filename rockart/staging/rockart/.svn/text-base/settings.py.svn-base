# Django settings for rockart project.
import os
import getpass

PWD = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'rockart',
        'USER': 'rockart',
        'PASSWORD': 'rockart',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MEDIA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'site_media')

MEDIA_URL = '/site_media/'

#ADMIN_MEDIA_PREFIX = 'http://a199.myrootshell.com:8080/rockart/admin/admin_media/'
      
# Kommentti otettu pois, serveri kaynnisty jos STATIC_ROOT ei asetettu.
# Python ei paase if os.name == 'posix' lausekkeesta eteenpain
#STATIC_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'site_media')

#STATIC_URL = '/site_media/'

STATIC_URL = 'http://a199.myrootshell.com:8080/rockart/staging/site_media/'

# Additional locations of static files
#STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#)

# List of finder classes that know how to find static files in
# various locations.
# Defaults for Django 1.3
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
#    'django.contrib.staticfiles.finders.DefaultStorageFinder', 
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

if os.name == 'nt':
    MEDIA_ROOT = '/cygwin/home/mnyman/.virtualenvs/rockart/staging/rockart/site_media/' # ROOT for uploads
    ADMIN_MEDIA_PREFIX = '/admin_media/'
    STATICFILES_DIRS = (
        'C:/cygwin/home/mnyman/.virtualenvs/rockart/staging/rockart/site_media/', # pakollinen...
    )
    STATIC_URL = '/site_media/'
elif os.name == 'posix':
    #if PWD.endswith('staging/rockart'):
        #MEDIA_ROOT = '/home/mnyman/.virtualenvs/rockart/staging/rockart/site_media/' #% (getpass.getuser(),) # ROOT for uploads
        # Sama kuin ylempi, mutta huomattavasti portattavampi (toimisi myos nt)
    MEDIA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'site_media')
    MEDIA_URL = '/site_media/'
    ADMIN_MEDIA_PREFIX = 'http://a199.myrootshell.com:8080/rockart/admin/admin_media/'     
    STATIC_URL = 'http://a199.myrootshell.com:8080/rockart/staging/site_media/'
        #STATIC_URL = '/site_media/'
    #pass
    #elif PWD.endswith('production/rockart'):
    #    MEDIA_ROOT = '/home/mnyman/.virtualenvs/rockart/production/rockart/site_media/' #% (getpass.getuser(),) # ROOT for uploads
    #    ADMIN_MEDIA_PREFIX = 'http://a199.myrootshell.com:8080/rockart/admin/admin_media/'   
    #    STATIC_URL = 'http://a199.myrootshell.com:8080/rockart/production/site_media/'
    #    pass
    #else:
    #    # TO-DO: some error handling here...
    #    pass

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xxe+9m*k$s8jahph3$!m91!p52ut$_vjjmfyus((w9nes1#w@j'

# List of callables that know how to import templates from various sources.
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
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'rockart.urls'

TEMPLATE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.gis',
    'rockart.geo',
)

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
