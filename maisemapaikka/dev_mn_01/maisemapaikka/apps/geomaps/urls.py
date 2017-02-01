# Import django modules
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'maisemapaikka.apps.geomaps.views.index'),
    (r'^save$', 'maisemapaikka.apps.geomaps.views.save'),
    (r'^search$', 'maisemapaikka.apps.geomaps.views.search'),
    (r'^upload$', 'maisemapaikka.apps.geomaps.views.upload'),
    
    #(r'^save$', 'maisemapaikka.apps.wiki.views.save'),
    #(r'^search$', 'maisemapaikka.apps.wiki.views.search'),
    #(r'^upload$', 'maisemapaikka.apps.wiki.views.upload'),
)
