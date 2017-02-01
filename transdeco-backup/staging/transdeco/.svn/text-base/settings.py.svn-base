# Django settings for transdeco project.

import os
import getpass

PWD = os.path.dirname(__file__)

if PWD.endswith('production/transdeco'):
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
else:
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG    

ADMINS = (
    ('Mika Nyman', 'mika.nyman@synapse-computing.com'),
)

MANAGERS = ADMINS

# http://djangosnippets.org/snippets/831/
ROOT = lambda suffix: os.path.join(os.path.dirname(__file__), suffix).replace('\\','/')

if os.name == 'nt':
    db_path = 'C:/cygwin/home/mnyman/.virtualenvs/transdeco/staging/sqlite/transdeco.sqlite'
elif os.name == 'posix':
    #% (getpass.getuser(),) # perustuu olettamukseen, etta tiedetaan mina kayttajana apache ajetaan
    if PWD.endswith('staging/transdeco'):
        db_path = '/home/%s/.virtualenvs/transdeco/staging/sqlite/transdeco.sqlite' % (getpass.getuser(),)
    elif PWD.endswith('production/transdeco'):
        db_path = '/home/%s/.virtualenvs/transdeco/production/sqlite/transdeco.sqlite' % (getpass.getuser(),)
    else:
        pass
        # manage.py edellyttaa manuaalisen ohjauksen fixturien paivityksessa
        #db_path = '/home/mnyman/.virtualenvs/transdeco/staging/sqlite/transdeco.sqlite'
        #db_path = '/home/mnyman/.virtualenvs/transdeco/production/sqlite/transdeco.sqlite'
    
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
        'NAME': db_path,
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

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
#MEDIA_URL = 'http://a29.myrootshell.com:8080/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'vt94+x8wzzbkzhv@9-1+=##steaei6)d5gy+$d2d#skgrhs_$4'

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
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'transdeco.urls'

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (
    ROOT('templates'),
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

# Defaults for Django 1.3
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'    
    )

#if PWD.startswith('C:'):
if os.name == 'nt':
    MEDIA_ROOT = '/cygwin/home/mnyman/.virtualenvs/transdeco/staging/transdeco/site_media/' # ROOT for uploads
    ADMIN_MEDIA_PREFIX = '/admin_media/'
    STATICFILES_DIRS = (
        'C:/cygwin/home/mnyman/.virtualenvs/transdeco/staging/transdeco/site_media/', # pakollinen...
    )
    #STATIC_ROOT = 'C:/cygwin/home/mnyman/.virtualenvs/transdeco/staging/static/'
    STATIC_URL = '/site_media/'
elif os.name == 'posix':
    if PWD.endswith('staging/transdeco'):
        MEDIA_ROOT = '/home/%s/.virtualenvs/transdeco/staging/transdeco/site_media/' % (getpass.getuser(),) # ROOT for uploads
        ADMIN_MEDIA_PREFIX = 'http://a29.myrootshell.com:8080/transdeco/admin/admin_media/'
        #STATICFILES_DIRS = (
        #    '/home/%s/.virtualenvs/transdeco/staging/transdeco/staging/transdeco/site_media/' % (getpass.getuser(),)
        #)       
        STATIC_URL = 'http://a29.myrootshell.com:8080/transdeco/staging/site_media/'
    elif PWD.endswith('production/transdeco'):
        MEDIA_ROOT = '/home/%s/.virtualenvs/transdeco/production/transdeco/site_media/' % (getpass.getuser(),) # ROOT for uploads
        ADMIN_MEDIA_PREFIX = 'http://a29.myrootshell.com:8080/transdeco/admin/admin_media/'
        #STATICFILES_DIRS = (
        #    '/home/%s/.virtualenvs/transdeco/staging/transdeco/staging/transdeco/site_media/' % (getpass.getuser(),)
        #)       
        STATIC_URL = 'http://a29.myrootshell.com:8080/transdeco/production/site_media/'
    else:
        # TO-DO: some error handling here...
        pass

#CACHE_BACKEND = 'dummy:///'

FIXTURE_DIRS = (
    ROOT('flatpages/fixtures/'),
    ROOT('galleria/fixtures/'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'transdeco.flatpages',
    'transdeco.galleria',
)
