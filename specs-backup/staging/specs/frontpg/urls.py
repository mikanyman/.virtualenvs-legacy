## frontpg/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('specs.frontpg.views',
    url(r'^(?P<url_pg>\w*)/$', 'index'),
    url(r'^(?P<url_pg>\w*)/(?P<url_id>\d+)/$', 'index_id'),                       
                    
    #url(r'^(?P<url_pg>vaikuta)/poll/(?P<poll_id>\d+)/kiitos/$', 'poll'),
    url(r'^(?P<url_pg>vaikuta)/$', 'cur_poll'),
    url(r'^(?P<url_pg>vaikuta)/\d+/$', 'cur_poll'),
    url(r'^(?P<url_pg>vaikuta)/polls/(?P<url_id>\d+)/$', 'poll'),
)
