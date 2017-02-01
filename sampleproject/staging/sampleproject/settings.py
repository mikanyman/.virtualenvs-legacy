# Django settings for project project.

import calloway
import os
import sys

ROOT_URLCONF = 'sampleproject.urls'

# CALLOWAY_ROOT = '/home/mnyman/.virtualenvs/sampleproject/local/lib/python2.7/site-packages/calloway'
CALLOWAY_ROOT = os.path.abspath(os.path.dirname(calloway.__file__))
sys.path.insert(0, os.path.join(CALLOWAY_ROOT, 'apps'))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'lib'))

try:
    from local_settings import DEBUG as LOCAL_DEBUG
    DEBUG = LOCAL_DEBUG
except ImportError:
    DEBUG = False
TEMPLATE_DEBUG = DEBUG

from calloway.settings import *

ADMINS = (
    ('mnyman', 'mika.nyman@synapse-computing.com'),
)
MANAGERS = ADMINS
DEFAULT_FROM_EMAIL='mika.nyman@synapse-computing.com'
SERVER_EMAIL='mika.nyman@synapse-computing.com'

SECRET_KEY = 'zji%0t_=1x#=&7l-y)@5_fo*h2bplrb51&3=k1j4b1@2=bx)jj'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'sampleproject.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Helsinki'
LANGUAGE_CODE = 'en-us'
USE_I18N = True

try:
    from local_settings import MEDIA_URL_PREFIX
except ImportError:
    MEDIA_URL_PREFIX = "/media/"

try:
    from local_settings import MEDIA_ROOT_PREFIX
except ImportError:
    MEDIA_ROOT_PREFIX = os.path.join(PROJECT_ROOT, 'media')

# uploads
try:    
    from local_settings import MEDIA_ROOT
except ImportError:
    MEDIA_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'uploads')

# static
try:
    from local_settings import STATIC_ROOT
except ImportError:
    STATIC_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'static')
    

MEDIA_URL = '%suploads/' % MEDIA_URL_PREFIX
STATIC_URL = "%sstatic/" % MEDIA_URL_PREFIX

ADMIN_TOOLS_MEDIA_URL = '/admin_tools/'

MMEDIA_DEFAULT_STORAGE = 'media_storage.MediaStorage'
MMEDIA_IMAGE_UPLOAD_TO = 'image/%Y/%m/%d'

AUTH_PROFILE_MODULE = ''

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
) + CALLOWAY_TEMPLATE_DIRS

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    # required by django-admin-tools
    'django.core.context_processors.request',
)

#CACHE_BACKEND = 'memcached://localhost:11211/'
CACHE_BACKEND = 'memcached://194.187.212.199:11211/'

INSTALLED_APPS = (
    APPS_DJANGO_BASE + \
    APPS_MESSAGES + \
    APPS_ADMIN + \
    APPS_STAFF + \
    APPS_REVERSION + \
    #APPS_STORIES + \
    APPS_CALLOWAY_DEFAULT + \
    APPS_MPTT + \
    APPS_CATEGORIES + \
    APPS_COMMENT_UTILS + \
    APPS_FRONTEND_ADMIN + \
    APPS_MEDIA + \
    APPS_UTILS + \
    #APPS_REGISTRATION + \
    APPS_TINYMCE + (
        'admin_tools.theming',
        'admin_tools.menu',
        'admin_tools.dashboard',
        'django.contrib.auth',
        'django.contrib.sites',
        'django.contrib.admin',
        #'staticfiles',
        #'calloway',
        #https://bitbucket.org/fivethreeo/django-mptt-comments
        #'django.contrib.comments',
        #'django.contrib.markup',
        #'template_utils',
        #'mptt',
        #'mptt_comments',
        'sampleproject.demo',
    )
)

ADMIN_TOOLS_THEMING_CSS = 'calloway/admin/css/theming.css'
#ADMIN_TOOLS_THEMING_CSS = os.path.join(CALLOWAY_ROOT, 'static/calloway/admin/css/theming.css')
# ADMIN_TOOLS_MENU = 'menu.CustomMenu'

TINYMCE_JS_URL = '%scalloway/js/tiny_mce/tiny_mce.js' % STATIC_URL
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, 'js/tiny_mce')

try:
    from local_settings import *
except ImportError:
    pass
