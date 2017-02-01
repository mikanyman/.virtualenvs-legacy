# members/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       
    # members_list_all
    # members_list_corp
    # members_list_person
    # members_list_hon
    # members_list_mail
    
    (r'^(?P<url_pg>members_\w+)/$',                    'specs.members.views.members_list'),
    (r'^(?P<url_pg>members_\w+)/(?P<object_id>\d+)/$', 'specs.members.views.members_detail'),
)