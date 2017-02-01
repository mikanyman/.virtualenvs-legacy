from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

admin.autodiscover()

urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'talls.views.home', name='home'),
    # url(r'^talls/', include('talls.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^news/', include('cmsplugin_news.urls')),

    url(r'^', include('cms.urls')), # always last
)
