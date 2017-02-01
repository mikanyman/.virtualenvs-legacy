#from filebrowser.sites import site
#from django.conf.urls.defaults import *
#import registration
#import profiles
#from django.views.generic.simple import redirect_to
#from django.views.generic.simple import direct_to_template

import os

# ---------- django-userena ----------
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from profiles.forms import SignupFormExtra

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # ---------- django-userena ----------
    # Demo Override the signup form with our own, which includes a first and last name.
    # (r'^accounts/signup/$', 'userena.views.signup', {'signup_form': SignupFormExtra}),
    (r'^accounts/', include('userena.urls')),
    (r'^messages/', include('userena.contrib.umessages.urls')),
    #url(r'^$', direct_to_template, {'template': 'static/promo.html'}, name='promo'),
    url(r'^promo/$', direct_to_template, {'template': 'static/promo.html'}, name='promo'),
    (r'^i18n/', include('django.conf.urls.i18n')),
                       
    url(r'^', include('maisemapaikka.apps.portal.urls')),
    url(r'^geo/', include('maisemapaikka.apps.geomaps.urls')),
    
    # ---------- django-haystack ----------
    (r'^search/', include('haystack.urls')),
        
    # ---------- django-cms ----------
    #url(r'^', include('filer.server.urls')),
    url(r'^', include('cms.urls')), # DEBUG jata vain juuri
)

#if settings.DEBUG:
if os.name == 'nt':
    #from django.conf import settings # already imported at top
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('django.views',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL, 'static.serve', {'document_root': settings.MEDIA_ROOT })
        # django-userena demo_project
        #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,
        #    'show_indexes': True, }),
    )


#if os.name == 'nt':
#    from django.conf import settings
#    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#    urlpatterns = staticfiles_urlpatterns()
#    urlpatterns += patterns('django.views',
#        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL, 'static.serve', {'document_root': settings.MEDIA_ROOT })
#    )
#    urlpatterns += patterns('',
                            
        #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        #url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.JS_ROOT}),
        
        # Testing
        #url(r'^maisemapaikka/cms/$', direct_to_template, {'template': 'template_1.html'}),

        #(r'^maisemapaikka/\w*/accounts/', include('registration.urls')),
        #(r'^maisemapaikka/\w*/accounts/profiles/', include('profiles.urls')),
        
        #url(r'^maisemapaikka/admin_tools/', include('admin_tools.urls')),        
        #(r'^maisemapaikka/rosetta/', include('rosetta.urls')),
        #(r'^maisemapaikka/map/$', include('maisemapaikka.apps.geomaps.urls')),
        #(r'^maisemapaikka/i18n/', include('django.conf.urls.i18n')),
        #(r'^maisemapaikka/\w*/wiki/', include('maisemapaikka.apps.wiki.urls')),
        #(r'^maisemapaikka/\w*/map/', include('maisemapaikka.apps.geodemo.urls')),
        
        # ---------- with/without django-cms ----------
        #(r'^maisemapaikka/', include('maisemapaikka.apps.portal.urls')), # with
        #(r'^maisemapaikka/\w*/', include('maisemapaikka.apps.portal.urls')), # without
        
        # Redirects
        #(r'^maisemapaikka/(?P<lang>\w+)/landscapes/$', redirect_to, {'url': '/maisemapaikka/%(lang)s/landscapes/frontpg/'}),
        #(r'^maisemapaikka/(?P<lang>\w+)/churches/$', redirect_to, {'url': '/maisemapaikka/%(lang)s/churches/frontpg/'}),
        #(r'^maisemapaikka/(?P<lang>\w+)/rockart/$', redirect_to, {'url': '/maisemapaikka/%(lang)s/rockart/frontpg/'}),
        #(r'^maisemapaikka/fi/$', redirect_to, {'url': '/maisemapaikka/fi/landscapes/frontpg/'}),
        #(r'^maisemapaikka/se/$', redirect_to, {'url': '/maisemapaikka/se/landscapes/frontpg/'}),
        #(r'^maisemapaikka/en/$', redirect_to, {'url': '/maisemapaikka/en/landscapes/frontpg/'}),
        #(r'^maisemapaikka/$', redirect_to, {'url': '/maisemapaikka/fi/landscapes/frontpg/'}),
        
        # ---------- admin ----------
        #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        #(r'^admin/', include(admin.site.urls)),
        
        # ---------- django-cms ----------
        #url(r'^maisemapaikka/', include('filer.server.urls')), # filer
        #url(r'^maisemapaikka/', include('cms.urls')),
#    )
#else:
#    urlpatterns = patterns('',                   
        
        #url(r'^fi/accounts/', include('registration.urls')),
        #url(r'^sv/accounts/', include('registration.urls')),
        #url(r'^en/accounts/', include('registration.urls')),
        
        #url(r'^fi/accounts/\w+/profiles/', include('profiles.urls')),
        #url(r'^sv/accounts/\w+/profiles/', include('profiles.urls')),
        #url(r'^en/accounts/\w+/profiles/', include('profiles.urls')),

        #url(r'^admin_tools/', include('admin_tools.urls')),
        #(r'^rosetta/', include('rosetta.urls')),
        #(r'^i18n/', include('django.conf.urls.i18n')),
        #(r'^wiki/\w+/', include('maisemapaikka.apps.wiki.urls')),
        #(r'^map/$', include('maisemapaikka.apps.geomaps.urls')),
        
        # ---------- Maisemapaikka ----------
        #(r'^', include('maisemapaikka.apps.portal.urls')),

        #(r'^fi/', include('maisemapaikka.apps.portal.urls')),
        #(r'^sv/', include('maisemapaikka.apps.portal.urls')),
        #(r'^en/', include('maisemapaikka.apps.portal.urls')),
        
        # Redirects
        #(r'^[fi,sv,en]/\w+/$', redirect_to, {'url': '/fi/landscapes/frontpg/'}),
        #(r'^[fi,sv,en]/$', redirect_to, {'url': '/fi/landscapes/frontpg/'}),
        
        #(r'^(?P<lang>\w+)/landscapes/$', redirect_to, {'url': '/%(lang)s/landscapes/frontpg/'}),
        #(r'^(?P<lang>\w+)/churches/$', redirect_to, {'url': '/%(lang)s/churches/frontpg/'}),
        #(r'^(?P<lang>\w+)/rockart/$', redirect_to, {'url': '/%(lang)s/rockart/frontpg/'}),
        #(r'^fi/$', redirect_to, {'url': '/fi/landscapes/frontpg/'}),
        #(r'^se/$', redirect_to, {'url': '/se/landscapes/frontpg/'}),
        #(r'^en/$', redirect_to, {'url': '/en/landscapes/frontpg/'}),
        #(r'^$', redirect_to, {'url': '/fi/landscapes/frontpg/'}),

        # ---------- admin ----------
        #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        #(r'^admin/', include(admin.site.urls)),

        # ---------- django-cms ----------
        #url(r'^', include('filer.server.urls')),
        #url(r'^', include('cms.urls')),
#    )
#urlpatterns += patterns('',
    #(r'^grappelli/', include('grappelli.urls')),
    #(r'^tinymce/', include('tinymce.urls')),
    #(r'^i18n/', include('django.conf.urls.i18n')),
    #(r'^admin/filebrowser/', include(site.urls)), # v. 3.4 # before admin-urls!
    #(r'^admin/filebrowser/', include('filebrowser.urls')), # v. 3.3  # before admin-urls!
    #(r'^photologue/', include('photologue.urls')),
#)
