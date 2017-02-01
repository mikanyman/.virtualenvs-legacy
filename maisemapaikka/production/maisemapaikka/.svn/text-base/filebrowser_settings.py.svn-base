from settings import MEDIA_ROOT

VIRTUALENVS_ROOT = "C:/cygwin/home/mnyman/.virtualenvs"

# C:/cygwin/home/mnyman/.virtualenvs/maisemapaikka/development/maisemapaikka/media/
#FILEBROWSER_MEDIA_ROOT = LOCAL_MEDIA_ROOT
#MEDIA_ROOT = FILEBROWSER_MEDIA_ROOT
FILEBROWSER_MEDIA_ROOT = '%s/maisemapaikka/development/maisemapaikka/media/' % VIRTUALENVS_ROOT
MEDIA_ROOT = getattr(settings, "FILEBROWSER_MEDIA_ROOT", settings.MEDIA_ROOT)

#FILEBROWSER_MEDIA_URL = LOCAL_MEDIA_URL
#MEDIA_URL = FILEBROWSER_MEDIA_URL

MEDIA_URL = getattr(settings, "FILEBROWSER_MEDIA_URL", settings.MEDIA_URL)

# C:/cygwin/home/mnyman/.virtualenvs/maisemapaikka/development/maisemapaikka/media/uploads/
FILEBROWSER_DIRECTORY = LOCAL_MEDIA_ROOT
DIRECTORY = FILEBROWSER_DIRECTORY + '/uploads/'