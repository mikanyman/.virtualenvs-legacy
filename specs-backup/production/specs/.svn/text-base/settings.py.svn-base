# specs@a29.myrootshell.com
# settings.py

#import os, posix
import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'specs',
        'USER': 'specs',
        'PASSWORD': 'specs',
        'HOST': '127.0.0.1',
        'PORT': '5432'
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
LANGUAGE_CODE = 'fi'

# Itse lisatty
DATE_FORMAT = 'd.m.Y'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/var/cherokee/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = 'http://www.tallsmall.fi:8080/site_media'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://www.tallsmall.fi:8080/specs/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'u%+14oj^+3^np^74fp5+65=&+#+bee@2hvtu_pjb+yx3m+wnp1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
##    'specs.template.loaders.database.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'specs.middleware.SetUserSession',
    'specs.middleware.UrlRedirectMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "specs.context_processors.url_vars",
    "specs.context_processors.topmenu_items",
)

ROOT_URLCONF = 'specs.urls'

# Ks. http://risottoinc.blogspot.com/2007/06/django-deployment-recipe.html
# PROJECT_ROOT maaritelty /etc/apache2/sites-available/default
# HUOM! loppuviiva poistettu alta! %s/templates

#PROJECT_ROOT = posix.environ.get('PROJECT_ROOT') or os.getcwd()
#dynamic_template_dir = '%s/templates' % PROJECT_ROOT

TEMPLATE_DIRS = (
    #os.path.join(os.path.dirname(__file__), 'templates')
    #dynamic_template_dir,
    '/var/django/specs/templates',
)

#ALLOWED_INCLUDE_ROOTS = ('/var/django/specs/templates/ssi', '/var/www')
ALLOWED_INCLUDE_ROOTS = (
    '/var/django/specs/templates/include',
    '/var/django/specs/templates/html/koputuksia/',
    '/var/django/specs/templates/cells/common',
)

ACCOUNT_ACTIVATION_DAYS = 7 #Liittyy pakettiin django-registration
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'toimisto@tallsmall.fi'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # True = browser-length cookies
LOGIN_REDIRECT_URL = '/accounts/profiles/'

""" ---------- django-registration ---------- """
ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_HOST='localhost'
DEFAULT_FROM_EMAIL = 'info@synapse-computing.com'
LOGIN_REDIRECT_URL = '/'


URL_REDIRECTS = (
    (r'www\.tallsmall\.fi/$', 'http://www.tallsmall.fi/fi/all/e0/frontpg/etusivu/'),
)

# MEMO: /etc/init.d/memcached {start|stop|restart|force-reload}
CACHE_BACKEND = 'memcached://194.187.213.71:11211/'

#FIXTURE_DIRS = (
#   'D:/Python26/Lib/site-packages/django/contrib/auth/fixtures',
#   'D:/eclipse/workspace/b71.myrootshell.com/specs/portal/.fixtures',
#)

# django-tagging
FORCE_LOWERCASE_TAGS = True
MAX_TAG_LENGTH = 50
TAGGING_AUTOCOMPLETE_JS_BASE_URL = '/var/cherokee/site_media/js/jquery/jquery-autocomplete'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.formtools',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
    'profiles',
    'registration',
    'tagging',
    #'tagging_autocomplete',
    'specs.apps.eventcal',
    'specs.choe',
    'specs.html',
    'specs.lehtiarkisto',
    'specs.taglibrary',
    'specs.frontpg',
    'specs.members',
    'specs.portal',
    'specs.questionaries',
    'specs.rdf',
    'specs.sql',
    'specs.tagforum',
    'specs.test',
)
