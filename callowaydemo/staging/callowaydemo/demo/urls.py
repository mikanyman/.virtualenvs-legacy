# callowaydemo/demo/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$',        'callowaydemo.demo.views.index'),
)
