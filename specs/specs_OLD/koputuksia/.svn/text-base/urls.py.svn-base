from django.conf.urls.defaults import *
from models import Juttu # relative import

info_dict = {
    'queryset': Juttu.objects.all(),
}

edit_dict = {
    'model': Juttu,
    'post_save_redirect': '/sites/specs/koputuksia/'
}

del_dict = {
    'model': Juttu,
    'post_delete_redirect': '/sites/specs/koputuksia/',
}

urlpatterns = patterns('',
    ### common to slug-based and id-based:
    #(r'^$',                          'django.views.generic.list_detail.object_list', info_dict),
    (r'^$',                           'specs.koputuksia.views.root_view'),

    ### slug-based:
    #(r'^(?P<slug>[\w_]+)/$',         'django.views.generic.list_detail.object_detail', dict(info_dict, slug_field='slug')),
    #(r'^add/$',                      'django.views.generic.create_update.create_object', edit_dict),
    #(r'^edit/(?P<slug>[\w_]+)/$',    'django.views.generic.create_update.update_object', dict(edit_dict, slug_field='slug')),
    #(r'^delete/(?P<slug>[\w_]+)/$',  'django.views.generic.create_update.delete_object', dict(del_dict, slug_field='slug')),

    ### id-based:
    #(r'^(?P<object_id>\d+)/$',       'django.views.generic.list_detail.object_detail', info_dict),
    (r'^(?P<issue_num>\d{1,2}-\d{4})/(?P<object_id>\d+)/$', 'specs.koputuksia.views.id_view'),
    (r'^add/$',                       'django.views.generic.create_update.create_object', dict(edit_dict, post_save_redirect='/sites/specs/koputuksia/')),
    #(r'^edit/(?P<object_id>\d+)/$',   'django.views.generic.create_update.update_object', dict(edit_dict, post_save_redirect='/sites/specs/koputuksia/%(id)s/')),
    #(r'^delete/(?P<object_id>\d+)/$', 'django.views.generic.create_update.delete_object', del_dict),
    (r'^(?P<issue_num>\d{1,2}-\d{4})/edit/(?P<object_id>\d+)/$', 'specs.koputuksia.views.edit_view'),
    (r'^(?P<issue_num>\d{1,2}-\d{4})/delete/(?P<object_id>\d+)/$', 'specs.koputuksia.views.del_view'),

    # Listaus julkaisunumeroittain (esim. '1-2006'):
    (r'^(?P<issue_num>\d{1,2}-\d{4})/$', 'specs.koputuksia.views.issue_view'),

    # Listaus julkaisunumeroittain ja osastoittain (esim. '1-2006/uutiset'):
    (r'^(?P<issue_num>\d{1,2}-\d{4})/(?P<category_name>[\w_]+)/$', 'specs.koputuksia.views.issue_category_view'),
    
    #(r'^(?P<slug>[\w\/]+)/$',        'django.views.generic.list_detail.object_detail', dict(info_dict, slug_field='slug')),
    #(r'^edit/(?P<slug>\w+)/$',       'django.views.generic.create_update.update_object', dict(edit_dict, slug_field='slug')),
    #(r'^edit/(?P<object_id>\d+)/$',  'django.views.generic.create_update.update_object', edit_dict),
)
