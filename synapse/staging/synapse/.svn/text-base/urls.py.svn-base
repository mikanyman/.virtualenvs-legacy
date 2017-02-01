# urlconf for synapse

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.views.generic.simple import direct_to_template

import os

from django.contrib import admin
admin.autodiscover()

# STATIC & MEDIA FOR DEVELOPMENT
if os.name == 'nt':
    
    from django.conf import settings
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # serving static files
    urlpatterns = staticfiles_urlpatterns()
    
    # serving uploaded files
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    )

# STATIC & MEDIA FOR STAGING & PRODUCTION
else:
    urlpatterns = patterns('',
        (r'^$', direct_to_template, {'template': 'blank.html'}),
    )

urlpatterns += patterns('',
    (r'^$', redirect_to, {'url': '/en/company'}),
    (r'^en/$', redirect_to, {'url': '/en/company'}),
    #(r'^.{1}$', redirect_to, {'url': 'fi/'}),
    (r'^(?P<lang>\w{2})/', include('synapse.pages.urls')),
    #(r'^.{3,}$', redirect_to, {'url': 'fi/'}),
    (r'^segments/', include('synapse.segments.urls')),

    #(r'^photologue/', include('photologue.urls')),
    #(r'^tinymce/', include('tinymce.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)


### Support for the tinymce-gallery-connection plugin
### http://code.google.com/p/tinymce-gallery-connection/

#from django.conf.urls.defaults import *
from views import *

urlpatterns += patterns('',
    (r'^galleries', galleries),
    (r'^images/(\-?\d+)', images),
    (r'^image/(\d+)', image),
    (r'^image_src/(\d+)/(\w+)', image_src),
)

#if 'rosetta' in settings.INSTALLED_APPS:
#    urlpatterns += patterns('',
#        url(r'^rosetta/', include('rosetta.urls')),
#    )
    
