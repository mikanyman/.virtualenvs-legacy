import os

from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # url(r'^$', 'churches.views.home', name='home'),
    # url(r'^churches/', include('churches.foo.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    
    # ---------- django-userena ----------
    (r'^accounts/', include('userena.urls')),

    # ---------- redirects ----------
    ('^$', redirect_to, {'url': '/churches/list/'}),

    # ---------- robots ----------
    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),

    # ---------- Model app ----------
    # http://www.grenadepod.com/2009/11/09/how-to-use-generic-views-in-django/
    url(r'^', include('churches.apps.rules.urls')),

    # ---------- admin ----------
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
if os.name == 'nt':
    from django.conf import settings
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('django.views',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL, 'static.serve', {'document_root': settings.MEDIA_ROOT })
    )