from django.conf.urls.defaults import *

urlpatterns = patterns('rockart.geo.views',
                       url(r'^$', 'index', name='waypoints-index'),
                       url(r'^search/', 'search', name='waypoints-search'),
                       url(r'^save/', 'save', name='waypoints-save'),
)
