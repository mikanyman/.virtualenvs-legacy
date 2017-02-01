#from django.conf.urls.defaults import *
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import os
from django.conf import settings

admin.autodiscover()

handler500 = 'django_ext.views.custom_server_error'

sitemaps = {
}

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^demo/', include('sampleproject.demo.urls')),
    (r'^admin_tools/', include('admin_tools.urls')),
)
from calloway.urls import urlpatterns as calloway_patterns

urlpatterns += calloway_patterns

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/mnyman/.virtualenvs/sampleproject/lib/python2.7/site-packages/calloway/static/calloway'}),
        url(r'^admin_tools/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/mnyman/.virtualenvs/sampleproject/lib/python2.7/site-packages/admin_tools/media/admin_tools'}),
    )

# STATIC_ROOT
#if settings.DEBUG:
#    urlpatterns += patterns('django.views.static',
#        (r'^media/static/(?P<path>.*)$', 'serve',
#            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
#    )

# MEDIA_ROOT
#if settings.DEBUG:
#    urlpatterns += patterns('',
#        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#            'document_root': settings.MEDIA_ROOT,
#        }),
#   )
