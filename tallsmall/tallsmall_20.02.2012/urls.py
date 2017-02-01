from django.conf.urls.defaults import patterns, include, url
import os
from tallsmall.local_redirects import REDIRECTS

from django.views.generic.simple import redirect_to

from django.contrib import admin
admin.autodiscover()

urlpatterns = REDIRECTS
urlpatterns += patterns('',

    # Examples:
    # url(r'^$', 'tallsmall.views.home', name='home'),

    # ---------- redirects ----------
    url(r'^$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/en/etreg/create/'}),
    url(r'^etreg/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/en/etreg/create/'}),
    url(r'^en/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/en/etreg/create/'}),
    url(r'^fi/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/fi/etreg/create/'}),
    url(r'^de/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/de/etreg/create/'}),
    url(r'^en/etreg/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/en/etreg/create/'}),
    url(r'^fi/etreg/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/fi/etreg/create/'}),
    url(r'^de/etreg/$', redirect_to, {'url': 'http://europatreffen.tallsmall.fi/de/etreg/create/'}),

    # ---------- site ----------
    url(r'^etreg/', include('tallsmall.apps.etreg.urls')),
    url(r'^accounts/', include('registration.urls'),),
    url(r'^profiles/', include('profiles.urls')),

    # ---------- admin ----------
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if os.name == 'nt':
    from django.conf import settings
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('django.views',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL, 'static.serve', {'document_root': settings.MEDIA_ROOT })
    )
