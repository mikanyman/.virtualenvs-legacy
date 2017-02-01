from django.conf.urls.defaults import *
from django.contrib import admin
import os
from django.conf import settings
import settings
from django.views.generic.simple import direct_to_template

admin.autodiscover()

handler500 = 'django_ext.views.custom_server_error'

sitemaps = {
}

urlpatterns = patterns('',
    (r'^$',             direct_to_template, {'template': 'demo/index.html'}),
    (r'^demo/', include('callowaydemo.demo.urls')),
    (r'^comments/', include('mptt_comments.urls')),
    (r'^admin/', include(admin.site.urls)),
)
from calloway.urls import urlpatterns as calloway_patterns

urlpatterns += calloway_patterns

if settings.DEBUG:
    urlpatterns += patterns('',
        #(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        #    {'document_root': os.path.join(os.path.dirname(__file__), 'media2')}),
        (r'^admin-media/(?P<path>.*)$', 'django.views.static.serve',
            #{'document_root': 'settings.ADMIN_MEDIA_ROOT'}),
            {'document_root': '/home/mnyman/.virtualenvs/callowaydemo/lib/python2.7/site-packages/django/contrib/admin/media'}),
    )
