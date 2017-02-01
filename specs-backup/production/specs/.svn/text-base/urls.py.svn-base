from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

profile_string_1 = '(?P<url_lang>\w{2})/(?P<url_profile>\w+)/(?P<url_event>\w+)/'
urlpatterns = patterns('',
    (r'^' + profile_string_1 + '(?P<url_app>blog)/',          include('specs.blog.urls')),
    (r'^' + profile_string_1 + '(?P<url_app>frontpg)/',       include('specs.frontpg.urls')),
    (r'^' + profile_string_1 + '(?P<url_app>morepg)/',        include('specs.morepg.urls')),
    (r'^' + profile_string_1 + '(?P<url_app>members)/',       include('specs.members.urls')),
    (r'^' + profile_string_1 + '(?P<url_app>questionaries)/', include('specs.questionaries.urls')),
    (r'^' + profile_string_1 + '(?P<url_app>tagforum)/',      include('specs.tagforum.urls')),
)

urlpatterns += patterns('',
    (r'^\w{2}/\w+/\w+/tagforum/',      include('specs.tagforum.urls')),
    (r'^\w{2}/\w+/\w+/lehtiarkisto/',  include('specs.lehtiarkisto.urls')),
    (r'^\w{2}/\w*/\w*/html/(?P<html_dir>[\w_-]*)/(?P<html_page>[\w\._-]*\.htm(l)?)$', 'specs.html.views.show_html_page'),
)

urlpatterns += patterns('',

    (r'^test/$', 'specs.test.views.index'),
    
    (r'^choe/',              include('specs.choe.urls')),                     

    # HUOM alusta puuttuu hatttu /fi/tall/e0 etuliitteen mahdollistamiseksi
    (r'accounts/',              include('registration.urls')),
    (r'^profiles/',             include('profiles.urls')),
    (r'^i18n/',                 include('django.conf.urls.i18n')),
    (r'^admin/filebrowser/',    include('filebrowser.urls')),
    #(r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
    (r'^admin/doc/',            include('django.contrib.admindocs.urls')),
    (r'^admin/',                include(admin.site.urls)),
    #(r'^cal/',                  include('specs.eventcal.urls')),
)


