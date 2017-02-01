# members/urls.py

from django.conf.urls.defaults import *

""" preview """
from specs.members.preview import JasenhakemusFormPreview
from specs.members.forms import JasenhakemusForm
from django import forms

urlpatterns = patterns('',
    url(r'^(?P<url_pg>application)/post/$', JasenhakemusFormPreview(JasenhakemusForm)),
    url(r'^(?P<url_pg>application)/create/$', 'specs.members.views.application_create'),
    url(r'^(?P<url_pg>application)/update/(?P<object_id>\d+)/$', 'specs.members.views.application_update'),                   
)

urlpatterns += patterns('',
    #url(r'^(?P<url_pg>application)/$', 'specs.members.views.application'),                        # application form                
    url(r'^(?P<url_pg>members_list)/$', 'specs.members.views.members_list'),
    url(r'^(?P<url_pg>members_list)/pass/$', 'specs.members.views.members_pass'),                 # update to passive
    url(r'^(?P<url_pg>member)/(?P<object_id>\d+)/$', 'specs.members.views.members_detail'),       # view, update, delete
    url(r'^(?P<url_pg>member)/latest_id/$', 'specs.members.views.members_latest_id'),             # redirect from create
    url(r'^(?P<url_pg>member)/$', 'specs.members.views.members_detail'),                          # create, search
    url(r'^(?P<url_pg>member_events)/(?P<object_id>\d+)/$', 'specs.members.views.member_events'), # events
)