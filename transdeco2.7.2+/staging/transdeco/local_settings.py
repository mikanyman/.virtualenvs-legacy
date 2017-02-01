import os

# ---------- stuff to import ----------
"""
    LOCAL_DATABASES, LOCAL_MEDIA_ROOT, LOCAL_MEDIA_URL, LOCAL_STATIC_ROOT, \
    LOCAL_STATIC_URL, LOCAL_ADMIN_MEDIA_PREFIX, LOCAL_STATICFILES_DIRS, \
    LOCAL_TEMPLATE_DIRS, LOCAL_FIXTURE_DIRS, LOCAL_INSTALLED_APPS
"""

# ---------- roots ----------
cur_dir = os.path.dirname(os.path.abspath(__file__)) # staging or production
path_list = cur_dir.split(os.sep)
DEPLOYMENT_DIR = path_list[-2] # staging or production
VIRTUALENVS_ROOT = '/home/mnyman/.virtualenvs'
PROJECT_ROOT = '%s/transdeco2.7.2+/%s/transdeco' % (VIRTUALENVS_ROOT, DEPLOYMENT_DIR)
URL_ROOT = 'http://a199.myrootshell.com:8080/transdeco/' + DEPLOYMENT_DIR

# ---------- debug ----------
LOCAL_DEBUG = False

# ---------- databases ----------
LOCAL_DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'transdeco',
        'USER': 'transdeco',
        'PASSWORD': 'transdeco',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# ---------- media ----------
LOCAL_MEDIA_ROOT = '/home/mnyman/.virtualenvs/transdeco2.7.2+/media/' # staging & production
LOCAL_MEDIA_URL = '%s/media/'  % URL_ROOT
LOCAL_STATIC_ROOT = '%s/sitestatic/' % PROJECT_ROOT
LOCAL_STATIC_URL = '%s/static/' % URL_ROOT
LOCAL_ADMIN_MEDIA_PREFIX = '%s/static/admin/' %  URL_ROOT
LOCAL_STATICFILES_DIRS = (
    PROJECT_ROOT + '/static',
    PROJECT_ROOT + '/media',
    '/home/mnyman/.virtualenvs/transdeco2.7.2+/media'
)

# ---------- templates, fixtures, apps ----------

LOCAL_TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT + '/templates',
)

LOCAL_FIXTURE_DIRS = (
    VIRTUALENVS_ROOT + '/transdeco2.7.2+/' + DEPLOYMENT_DIR + '/transdeco/apps/flatpages/fixtures/',
    VIRTUALENVS_ROOT + '/transdeco2.7.2+/' + DEPLOYMENT_DIR + '/transdeco/apps/galleria/fixtures/',
)

LOCAL_INSTALLED_APPS = (

    # ---------- django-admin-tools ----------
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'south',

    'transdeco.apps.flatpages',
    'transdeco.apps.galleria',
)

