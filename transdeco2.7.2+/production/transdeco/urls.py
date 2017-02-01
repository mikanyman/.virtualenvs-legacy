# transdeco/urls.py

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os
cur_dir = os.getcwd()

from django.conf.urls.defaults import *

## required in Django 1.x
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #(r'^rdf',   include('transdeco.rdf.urls')),

    (r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    (r'^', include('transdeco.apps.galleria.urls')),
)

if os.name == 'nt':       
    from django.conf import settings
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('django.views',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL, 'static.serve', {'document_root': settings.MEDIA_ROOT })
    #(r'^admin_media/(.*)$', 'django.views.static.serve',
    #    {'document_root': 'C:/cygwin/home/mnyman/.virtualenvs/transdeco/Lib/site-packages/django-1.3-py2.7.egg/django/contrib/admin/media'}),
    )
