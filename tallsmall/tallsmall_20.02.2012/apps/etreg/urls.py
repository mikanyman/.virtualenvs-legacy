from django.conf.urls.defaults import patterns, include, url
from django.views.generic import list_detail, create_update
from tallsmall.apps.etreg.models import Person, PersonForm


# ---------- generic views dictionaries ----------
person_info = {
    "queryset" : Person.objects.all(),
    'template_name': 'etreg/admin_person.html',
}
person_form = {
    'form_class': PersonForm,
    'template_name': 'etreg/person_form.html', # default
}
person_detail = {
    'queryset' : Person.objects.all(),
    'template_name': 'etreg/person_form.html',
}
person_list = {
    'queryset' : Person.objects.all(),
    'template_name': 'etreg/person_list.html', # default
}


urlpatterns = patterns('',

    # ---------- generic views ----------
    url(r'^create/$', create_update.create_object, person_form, name="person-create"),
    #url(r'^update/(?P<object_id>\d+)/$', create_update.update_object, person_form, name="person-update"),
    #url(r'^detail/(?P<object_id>\d+)/$', create_update.update_object, person_form, name="person-detail"),
    #url(r'^list/$', list_detail.object_list, person_list, name="person-list"),
    #url(r'^delete/$', create_update.delete_object, person_info, name="person-delete"),
    
<<<<<<< .mine
    #(r'$', 'tallsmall.apps.etreg.views.index'),
=======
    (r'^xsendfile/(?P<file_name>(.+?)(\.[^.]*$|$))$', 'tallsmall.apps.etreg.views.xsendfile'),
    #url(r'^xsendfile/.*$', 'tallsmall.utils.xsend.send', {'from_media': True, 'file': 'ET2012FI_Registration_form_PDF_auf_Deutsch.pdf'})

>>>>>>> .r212
    #(r'$', 'tallsmall.apps.etreg.views.index'),

)




    