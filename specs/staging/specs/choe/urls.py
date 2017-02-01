# specs/choe/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    ### list
    (r'^$',        'specs.choe.views.list_entries'),
    (r'^create/$', 'specs.choe.views.create_entry'),
)
