# transdeco/urls.py

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os
cur_dir = os.getcwd()

from django.conf.urls.defaults import *

## required in Django 1.x
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/(.*)', admin.site.root),VANHA
    url(r'^admin/', include(admin.site.urls)), 
    #url(r'^rdf',       include('transdeco.rdf.urls')),
    url(r'^',          include('transdeco.galleria.urls')),
    
    #url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': 'C:/"Application Data"/eclipse/workspace/transdeco/site_media'}),

)
if cur_dir.startswith('C:'):
    urlpatterns += staticfiles_urlpatterns()
    #urlpatterns += patterns('',
    #    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    #        {'document_root': 'C:\\"Application Data"\\eclipse\\workspace\\transdeco\\site_media'}),
    #)
