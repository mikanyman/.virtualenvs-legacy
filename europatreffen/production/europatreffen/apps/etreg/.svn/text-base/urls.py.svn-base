from django.conf.urls.defaults import patterns, include, url
from django.views.generic import list_detail, create_update
from europatreffen.apps.etreg.models import Person, PersonForm


# ---------- generic views dictionaries ----------

# create, update
#person_form = {
#    'form_class': PersonForm,
#    'template_name': 'etreg/person_form.html', # default
#}
# detail
#person_detail = {
#    'queryset' : Person.objects.all(),
#    'template_name': 'etreg/person_detail.html',
#}
# email
#person_email = {
#    'queryset' : Person.objects.all(),
#    'template_name': 'etreg/person_email.html',
#}
# list
#person_list = {
#    'queryset' : Person.objects.all(),
#    'template_name': 'etreg/person_list.html', # default
#}
# delete
#person_delete = {
#  'model': Person,
#  'post_delete_redirect': '/etreg/list/',
#  'template_name': 'etreg/delete_confirm_rule.html',
#}

urlpatterns = patterns('',

    # ---------- generic views ----------
    #url(r'^create/$', create_update.create_object, person_form, name="person-create"),
    #url(r'^update/(?P<object_id>\d+)/$', create_update.update_object, person_form, name="person-update"),
    #url(r'^detail/(?P<object_id>\d+)/$', list_detail.object_detail,   person_detail, name="person-detail"),
    #url(r'^list/$', list_detail.object_list, person_list, name="person-list"),
    #url(r'^delete/(?P<object_id>\d+)/$', create_update.delete_object, person_delete, name="person-delete"),

    # ---------- extensible generic views ----------
    url(r'^create/$', 'europatreffen.apps.etreg.views.person_create', name='person-create'),
    url(r'^update/(?P<object_id>\d+)/$', 'europatreffen.apps.etreg.views.person_update', name='person-update'),
    url(r'^detail/(?P<object_id>\d+)/$', 'europatreffen.apps.etreg.views.person_detail', name='person-detail'),
    url(r'^list/$', 'europatreffen.apps.etreg.views.person_list', name="person-list"),
    url(r'^delete/(?P<object_id>\d+)/$', 'europatreffen.apps.etreg.views.person_delete', name='person-delete'),

    #url(r'^email/(?P<object_id>\d+)/$', list_detail.object_detail, person_email, name="person-email"),
    url(r'^email/(?P<object_id>\d+)/$', 'europatreffen.apps.etreg.views.send_email', name="person-email"),
    
    (r'^xsendfile/(?P<file_name>(.+?)(\.[^.]*$|$))$', 'europatreffen.apps.etreg.views.xsendfile'),
    #url(r'^xsendfile/.*$', 'europatreffen.utils.xsend.send', {'from_media': True, 'file': 'ET2012FI_Registration_form_PDF_auf_Deutsch.pdf'})

)




    
