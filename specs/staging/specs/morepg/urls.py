## morepg/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('specs.morepg.views',
    url(r'^(?P<url_pg>\w*)/(?P<url_id>\d+)/$', 'index_id'),
)