# specs/tagforum/urls.py

from django.conf.urls.defaults import *

""" generic views """
from tagging.views import tagged_object_list
from django.db.models import Q
from specs.tagforum.models import Entry

#"""
#urlpatterns = patterns('',
#    url(r'(?P<url_pg>tagforum_list)/tag/(?P<tag>[^/]+)/$',
#        tagged_object_list,
#        dict(
#            queryset_or_model = Entry.objects.filter(
#                Q(spam__isnull=True) | Q(spam=False)),
#            tag = '%s',
#            paginate_by=10, 
#            allow_empty=True,
#            template_object_name='entry',
#            extra_context = {
#                'url_lang': '%s', 
#                'url_profile': '%s', 
#                'url_event': '%s', 
#                'url_app': '%s', 
#                'url_pg': '%s'}),
#        name='entry_tag_list'),
#) % tag, url_lang, url_profile, url_event, url_app, url_pg
#"""
urlpatterns = patterns('',
    url(r'(?P<url_pg>tagforum_list)/$', 'specs.tagforum.views.list_entries', name='entry_list'),
    url(r'(?P<url_pg>tagforum_list)/tag/(?P<tag>[^/]+)/$', 'specs.tagforum.views.list_tagged_entries', name='entry_tag_list'),
    url(r'(?P<url_pg>tagforum_create)/$', 'specs.tagforum.views.create_entry'),
)
