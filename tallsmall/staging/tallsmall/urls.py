from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
import os
from tallsmall.redirects import REDIRECTS

# ---------- django-userena ----------
from account.forms import SignupFormExtra

from django.contrib import admin
admin.autodiscover()

urlpatterns = REDIRECTS
urlpatterns += patterns('',
                        
    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    
    # ---------- Model app ----------
    # http://www.grenadepod.com/2009/11/09/how-to-use-generic-views-in-django/
    url(r'^rules/', include('tallsmall.apps.rules.urls')),
    
    # Examples:
    # url(r'^$', 'tallsmall.views.home', name='home'),
    url(r'^etreg/', include('tallsmall.apps.etreg.urls')),
    #url(r'^accounts/', include('registration.urls'),),
    #url(r'^profiles/', include('profiles.urls')),
    #(r'^accounts/', include('userena.urls')), # userena
    
    # ---------- admin ----------
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # ---------- django-userena ----------
    # Demo Override the signup form with our own, which includes a first and last name.
    #(r'^accounts/signup/$', 'userena.views.signup', {'signup_form': SignupFormExtra}),
    #(r'^accounts/', include('userena.urls')),
    #(r'^messages/', include('userena.contrib.umessages.urls')),
    #url(r'^$', direct_to_template, {'template': 'static/promo.html'}, name='promo'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    
    # ---------- django-cms ----------
    url(r'^', include('cms.urls')),
    
)

if os.name == 'nt':
    from django.conf import settings
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('django.views',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL, 'static.serve', {'document_root': settings.MEDIA_ROOT })
    )
