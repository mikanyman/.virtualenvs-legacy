# Django settings for project project.

import calloway
import os
import sys

# /home/mnyman/.virtualenvs/callowaydemo/local/lib/python2.7/site-packages/calloway
CALLOWAY_ROOT = os.path.abspath(os.path.dirname(calloway.__file__))
sys.path.insert(0, os.path.join(CALLOWAY_ROOT, 'apps'))
# /home/mnyman/.virtualenvs/callowaydemo/staging/callowaydemo
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

SECRET_KEY = 'es^aje_(=9&z(^$i=+3dpk!i(_gog7c2zmno@(%*&&8$0vz06$'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'callowaydemo.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/New_York'
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

# Uploads
# /home/mnyman/.virtualenvs/callowaydemo/staging/callowaydemo/media/uploads
try:    
    from local_settings import MEDIA_ROOT
except ImportError:
    MEDIA_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'uploads')

# Static
# /home/mnyman/.virtualenvs/callowaydemo/staging/callowaydemo/media/static
try:
    from local_settings import STATIC_ROOT
except ImportError:
    STATIC_ROOT = os.path.join(MEDIA_ROOT_PREFIX, 'static')

# /media/uploads/
MEDIA_URL = '%suploads/' % MEDIA_URL_PREFIX
# /media/static/
STATIC_URL = "%sstatic/" % MEDIA_URL_PREFIX

MMEDIA_DEFAULT_STORAGE = 'media_storage.MediaStorage'
MMEDIA_IMAGE_UPLOAD_TO = 'image/%Y/%m/%d'

AUTH_PROFILE_MODULE = ''

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
) + CALLOWAY_TEMPLATE_DIRS

CACHE_BACKEND = 'memcached://localhost:11211/'

INSTALLED_APPS = APPS_DJANGO_BASE + \
    APPS_MESSAGES + \
    APPS_ADMIN + \
    APPS_STAFF + \
    APPS_REVERSION + \
    APPS_STORIES + \
    APPS_CALLOWAY_DEFAULT + \
    APPS_MPTT + \
    APPS_CATEGORIES + \
    APPS_COMMENT_UTILS + \
    APPS_FRONTEND_ADMIN + \
    APPS_MEDIA + \
    APPS_UTILS + \
    APPS_REGISTRATION + \
    APPS_TINYMCE + (
        'django.contrib.staticfiles',
        'django.contrib.redirects',
        'calloway',
        # requirements for mptt-comments
        'django.contrib.comments',
        'django.contrib.markup',
        'template_utils',
        #'mptt', # tullut callowayn mukana
        #'mptt_comments', # tullut callowayn mukana
    )

ADMIN_TOOLS_THEMING_CSS = 'calloway/admin/css/theming.css'
# ADMIN_TOOLS_MENU = 'menu.CustomMenu'

TINYMCE_JS_URL = '%scalloway/js/tiny_mce/tiny_mce.js' % STATIC_URL
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, 'js/tiny_mce')

try:
    from local_settings import *
except ImportError:
    pass
