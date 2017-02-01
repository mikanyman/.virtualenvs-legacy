from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os
#cur_dir = os.getcwd()

from django.conf.urls.defaults import *
from django.conf import settings

## required in Django 1.x
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)), 
)

#urlpatterns += patterns('',
#        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#)

if os.name == 'nt':
    urlpatterns += patterns('',
        (r'^admin_media/(.*)$', 'django.views.static.serve',
            {'document_root': 'C:/cygwin/home/mnyman/.virtualenvs/rockart/Lib/site-packages/django/contrib/admin/media'}),
        (r'^', include('rockart.geo.urls')),
)
else:
    urlpatterns += patterns('',
        (r'^', include('rockart.geo.urls')),
)
