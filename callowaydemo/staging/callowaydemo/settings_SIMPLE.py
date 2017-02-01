# Django settings for project project.

DEBUG = True

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
        'NAME': '/home/mnyman/.virtualenvs/callowaydemo/staging/callowaydemo/callowaydemo.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
ROOT_URLCONF = 'callowaydemo.urls'
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True

CACHE_BACKEND = 'memcached://localhost:11211/'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes'
    )

