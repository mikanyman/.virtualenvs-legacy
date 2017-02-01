# sql/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('specs.sql.views',
    ### list
    (r'^init_create_modify/$',   'init_create_modify'),
)