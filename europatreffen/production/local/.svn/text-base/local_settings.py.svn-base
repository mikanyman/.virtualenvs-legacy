# ---------- stuff to import ----------
"""
    LOCAL_DATABASES, LOCAL_MEDIA_ROOT, LOCAL_MEDIA_URL, LOCAL_STATIC_ROOT, \
    LOCAL_STATIC_URL, LOCAL_ADMIN_MEDIA_PREFIX, LOCAL_STATICFILES_DIRS, \
    LOCAL_TEMPLATE_DIRS, LOCAL_FIXTURE_DIRS, LOCAL_INSTALLED_APPS, LOCAL_DEPLOYMENT
"""

# ---------- for apache/django.wsgi ----------
LOCAL_DEPLOYMENT = 'production'

# ---------- roots ----------
VIRTUALENVS_ROOT = '/home/mnyman/.virtualenvs'
PROJECT_ROOT = '/home/mnyman/.virtualenvs/tallsmall/%s/tallsmall' % LOCAL_DEPLOYMENT
URL_ROOT = 'http://a199.myrootshell.com:8080/tallsmall/%s' %  LOCAL_DEPLOYMENT


# ---------- debug ----------
LOCAL_DEBUG = True


# ---------- databases ----------
#LOCAL_DATABASE_ROUTERS = ['tallsmall.routers.DatabaseAppsRouter']
LOCAL_DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tallsmall',
        'USER': 'tallsmall',
        'PASSWORD': 'tallsmall',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# ---------- media ----------
LOCAL_MEDIA_ROOT = '%s/media/' % PROJECT_ROOT
LOCAL_MEDIA_URL = '%s/media/' % URL_ROOT
LOCAL_STATIC_ROOT = '%s/sitestatic/' % PROJECT_ROOT
LOCAL_STATIC_URL = '%s/static/' % URL_ROOT
LOCAL_ADMIN_MEDIA_PREFIX = '%s/static/admin/' % URL_ROOT
LOCAL_STATICFILES_DIRS = (
    PROJECT_ROOT + '/static',
)

# ---------- templates, fixtures, apps ----------

LOCAL_TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT + '/templates',
)

LOCAL_FIXTURE_DIRS = (
   VIRTUALENVS_ROOT + "/tallsmall/production/tallsmall/apps/etreg/fixtures/",
)

LOCAL_INSTALLED_APPS = (

    # ---------- django-admin-tools ----------
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    #'accounts', # for django-profiles
    'registration',
    'profiles',
    'tagging',

    # ---------- apps ----------
    'tallsmall.account',
    'apps.etreg',
    'apps.rules',

    # ---------- django-userena / django-guardian ----------
    #'userena',
    'guardian',
    #'easy_thumbnails',

    # ---------- django-cms ----------
    'cms',
    'cms_redirects',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'smartsnippets',

    # ---------- django-cms plugins ----------
    #'cms.plugins.file', # use django-filer instead
    #'cms.plugins.flash',
    #'cms.plugins.googlemap',
    #'cms.plugins.link',
    #'cms.plugins.picture',
    #'cms.plugins.snippet',
    #'cms.plugins.teaser',
    'cms.plugins.text',
    #'cms.plugins.video',
    #'cms.plugins.twitter',

    # ---------- django-filer ----------
    #'easy_thumbnails',
    #'polymorphic',
    #'filer',
    #'reversion',
    #'cmsplugin_filer_file',
    #'cmsplugin_filer_folder',
    #'cmsplugin_filer_image',
    #'cmsplugin_filer_teaser',
    #'cmsplugin_filer_video',
)

