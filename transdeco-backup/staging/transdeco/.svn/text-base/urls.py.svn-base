# transdeco/urls.py

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os
cur_dir = os.getcwd()

from django.conf.urls.defaults import *

## required in Django 1.x
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)), 
)
if cur_dir.startswith('C:'):
    #urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        (r'^admin_media/(.*)$', 'django.views.static.serve',
            {'document_root': 'C:/cygwin/home/mnyman/.virtualenvs/transdeco/Lib/site-packages/django/contrib/admin/media'}),
        (r'^', include('transdeco.galleria.urls')),
        #(r'^rdf',   include('transdeco.rdf.urls')),
)
else:
    urlpatterns += patterns('',
        (r'^', include('transdeco.galleria.urls')),
        #(r'^rdf',   include('transdeco.rdf.urls')),
)
