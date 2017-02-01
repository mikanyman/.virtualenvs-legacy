# synapse/local_settings.py

VIRTUALENVS_ROOT = '/home/mnyman/.virtualenvs'
#PROJECT_ROOT = '/home/mnyman/.virtualenvs/synapse/staging/synapse'

LOCAL_DEBUG = True

LOCAL_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': VIRTUALENVS_ROOT + '/synapse/staging/sqlite/synapse.sqlite',
    }
}

LOCAL_MEDIA_ROOT = "%s/synapse/staging/synapse/media/" % VIRTUALENVS_ROOT

LOCAL_MEDIA_URL = "/media/"

# Use for python manage.py collectstatic
LOCAL_STATIC_ROOT = '%s/synapse/staging/synapse/sitestatic' % VIRTUALENVS_ROOT

LOCAL_STATIC_URL = '/static/'

LOCAL_ADMIN_MEDIA_PREFIX = '/static/admin/'
#LOCAL_ADMIN_MEDIA_PREFIX = LOCAL_STATIC_URL + "grappelli/"

LOCAL_STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    VIRTUALENVS_ROOT + "/synapse/staging/synapse/static",
)

LOCAL_TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    VIRTUALENVS_ROOT + "/synapse/staging/synapse/templates",
)

#LOCAL_TINYMCE_JS_URL = os.path.join(MEDIA_ROOT, 'tiny_mce/tiny_mce.js')
#LOCAL_TINYMCE_JS_URL = '/static/tiny_mce/tiny_mce_src.js'
