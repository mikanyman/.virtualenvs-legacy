from django.conf.urls.defaults import *

urlpatterns = patterns('rockart.geo.views',
                       url(r'^$', 'index', name='waypoints-index'),
                       url(r'^search/$', 'search', name='waypoints-search'),
                       url(r'^show-all/', 'search_all', name='waypoints-search-all'),
                       url(r'^save/', 'save', name='waypoints-save'),
                       #
                       url(r'^kartat/', 'map_index', name='map-index'),
                       url(r'^kartat/map/$', 'show_map', name='map-show-map'),
                       url(r'^kartat/waypoint/$', 'show_waypoint', name='map-show-waypoint'),
                       )
