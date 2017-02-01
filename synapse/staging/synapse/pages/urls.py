from django.conf.urls.defaults import *

urlpatterns = patterns('synapse.pages.views',
    (r'(?P<page>\w+)/$', 'index'),
)