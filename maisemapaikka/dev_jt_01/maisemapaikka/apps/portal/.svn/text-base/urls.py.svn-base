#from django.conf.urls.defaults import *
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

import os

urlpatterns = patterns('',
                          
    # MAISEMAT
    (r'landscapes/frontpg/$', 'maisemapaikka.apps.portal.views.landscapes_frontpg'),
    (r'landscapes/time/$', 'maisemapaikka.apps.portal.views.landscapes_time'),
    (r'landscapes/photo/$', 'maisemapaikka.apps.portal.views.landscapes_photo'),
    (r'landscapes/research/$', 'maisemapaikka.apps.portal.views.landscapes_research'),
    (r'landscapes/research/rhtml/$', 'maisemapaikka.apps.portal.views.landscapes_rhtml'),
    (r'landscapes/story/$', 'maisemapaikka.apps.portal.views.landscapes_story'),
        
    # TEST  
    (r'landscapes/rmedia/(?P<rhtml_file>.*)$', 'maisemapaikka.apps.portal.views.landscapes_rmedia'),
    (r'landscapes/lmedia/(?P<lmedia_file>.*)$', direct_to_template, {'template': 'lmedia.html'}),
    
    # KIRKOT
    (r'churches/frontpg/$', 'maisemapaikka.apps.portal.views.churches_frontpg'),
    (r'churches/time/$', 'maisemapaikka.apps.portal.views.churches_time'),
    (r'churches/photo/$', 'maisemapaikka.apps.portal.views.churches_photo'),
    (r'churches/research/$', 'maisemapaikka.apps.portal.views.churches_research'),
    (r'churches/research/rhtml/$', 'maisemapaikka.apps.portal.views.churches_rhtml'),
    (r'churches/story/$', 'maisemapaikka.apps.portal.views.churches_story'),
    
    # KALLIOMAALAUKSET
    (r'rockart/frontpg/$', 'maisemapaikka.apps.portal.views.rockart_frontpg'),
    (r'rockart/time/$', 'maisemapaikka.apps.portal.views.rockart_time'),
    (r'rockart/photo/$', 'maisemapaikka.apps.portal.views.rockart_photo'),
    (r'rockart/research/$', 'maisemapaikka.apps.portal.views.rockart_research'),
    (r'rockart/research/rhtml/$', 'maisemapaikka.apps.portal.views.rockart_rhtml'),
    (r'rockart/story/$', 'maisemapaikka.apps.portal.views.rockart_story'),
)

if os.name == 'posix':
    urlpatterns += patterns('',
                            
        # malli...
        #url(r'^$', 'index', name='waypoints-index'),
        #url(r'^search$', 'search', name='waypoints-search'),

        (r'landscapes/map/', 'maisemapaikka.apps.geomaps.views.index'),
        #(r'landscapes/map/(?P<map>\d+)/$', 'maisemapaikka.apps.geomaps.views.index'),
        #(r'landscapes/map/$', 'maisemapaikka.apps.portal.views.landscapes_map'),
        #url(r'landscapes/map/$', 'maisemapaikka.apps.geomaps.views.index', name='waypoints-index'),
        #url(r'landscapes/map/search$', 'maisemapaikka.apps.geomaps.search.index', name='waypoints-search'),
        
        (r'churches/map/', 'maisemapaikka.apps.geomaps.views.index'),
        #(r'churches/map/(?P<map>\d+)/$', 'maisemapaikka.apps.geomaps.views.index'),
        #(r'churches/map/$', 'maisemapaikka.apps.portal.views.churches_map'),
        #url(r'churches/map/$', 'maisemapaikka.apps.geomaps.views.index', name='waypoints-index'),
        #url(r'churches/map/search$', 'maisemapaikka.apps.geomaps.search.index', name='waypoints-search'),
    
        (r'rockart/map/', 'maisemapaikka.apps.geomaps.views.index'),
        #(r'rockart/map/(?P<map>\d+)/$', 'maisemapaikka.apps.geomaps.views.index'),
        #(r'rockart/map/$', 'maisemapaikka.apps.portal.views.rockart_map'),
        #(r'^rockart/map/$', 'maisemapaikka.apps.portal.views.index'),
        #url(r'rockart/map/$', 'maisemapaikka.apps.geomaps.views.index', name='waypoints-index'),
        #url(r'rockart/map/search$', 'maisemapaikka.apps.geomaps.search.index', name='waypoints-search'),
    )
