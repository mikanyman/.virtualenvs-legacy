# specs/blog/urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'(?P<url_pg>blog_list)/$', 'specs.blog.views.list_entries'),
    url(r'(?P<url_pg>blog_list)/(?P<url_id>\d+)/$', 'specs.blog.views.detail'),
    #url(r'(?P<url_pg>blog_list)/(?P<url_blog>\w+)/$', 'specs.blog.views.list_entries'),
)
