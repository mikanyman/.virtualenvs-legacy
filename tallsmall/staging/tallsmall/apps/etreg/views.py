from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import *
from django.utils.translation import ugettext_lazy as _

# ---------- email ----------
#from email_from_template import send_mail
#from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect

# ---------- import generic views ----------
from django.views.generic import list_detail, create_update

from django.contrib.auth.decorators import login_required

from tallsmall.apps.etreg.models import Person, PersonForm

from django.http import HttpResponse
import os
import mimetypes


def person_create(request):
    
    # generic views
    response = create_update.create_object(
        request,
        form_class = PersonForm,
        template_name = 'etreg/person_form.html' # default
    )
    return response

def person_update(request, object_id):

    # generic views
    response = create_update.update_object(
        request,
        form_class = PersonForm,
        object_id = object_id,
        template_name = 'etreg/person_form.html' # default
    )
    return response

def person_detail(request, object_id):
    
    # generic views
    response = list_detail.object_detail(
        request,
        queryset = Person.objects.all(),
        object_id = object_id,
        template_name = 'etreg/person_detail.html'
    )
    return response

#@login_required
def person_list(request):
    
    # generic views
    response = list_detail.object_list(
        request, 
        queryset = Person.objects.all().order_by('added'), 
        template_name = 'etreg/person_list.html'
    )
    return response

def person_delete(request, object_id):
    
    # generic views
    response = create_update.delete_object(
        request, 
        model = Person,
        object_id = object_id,
        post_delete_redirect = '/etreg/list/',
        template_name = 'etreg/delete_confirm_rule.html'
    )
    return response

def send_email(request, object_id):
    
    # create email message using generic views
    msg_text = list_detail.object_detail(
        request,
        queryset = Person.objects.all(),
        template_name = "etreg/person_email_text.html",
        object_id = object_id,
        mimetype = None
    )
    
    # create email message using generic views
    msg_html = list_detail.object_detail(
        request,
        queryset = Person.objects.all(),
        template_name = "etreg/person_email_html.html",
        object_id = object_id,
        mimetype = None
    )
    
    message_text = ''
    for line in msg_text:
        if not "Content-Type" in line:
            message_text += line
    
    message_html = ''
    for line in msg_html:
        if not "Content-Type" in line:
            message_html += line
    
    # Remove line "Content-Type: text/html; charset=utf-8"
    # http://stackoverflow.com/questions/1801008/django-html-email-adds-extra-characters-to-the-email-body
    #message_html = str(message_html).replace('Content-Type: text/html; charset=utf-8', '')
    #message_html = message_html.replace('X-Object-Type: etreg.person Content-Type: text/html; charset=utf-8 X-Object-Id: ', '')
    #message_html = message_html.replace('X-Object-Type: etreg.person X-Object-Id: ', '')

    person = Person.objects.filter(id=object_id)
    
    subject = _('Europatreffen Registration')
    from_email = 'europatreffen@gmail.com'
    to_email = person[0].email
        
    msg = EmailMultiAlternatives(subject, message_text, from_email, ['europatreffen@gmail.com', 'webreg@europatreffen.com', to_email])
    msg.attach_alternative(message_html, "text/html")
    msg.send()
    
    redirect_url = '/etreg/detail/%s/?token=sent' % object_id
    return HttpResponseRedirect(redirect_url)


#@login_required
def xsendfile(request, file_name):
    
    # remove a trailing slash if it exists
    if file_name[-1:] == '/':
        file_name = file_name[0:-1]
    
    directory = '/home/mnyman/.virtualenvs/tallsmall/staging/tallsmall/media/xsendfile/'
    path_to_file = os.path.join(directory, file_name)
    
    #return HttpResponse(path_to_file) # debug
    
    # http://codenuts.blogspot.com/2008/10/force-download-django.html
    file = open(path_to_file,"r")
    mimetype = mimetypes.guess_type(path_to_file)[0]
    if not mimetype: mimetype = "application/octet-stream"
    response = HttpResponse(file.read(), mimetype=mimetype)
    response["Content-Disposition"]= "attachment; filename=%s" % os.path.split(path_to_file)[1]
    return response



    # http://discussion.dreamhost.com/thread-127481-post-148059.html#pid148059
    #response = HttpResponse(mimetype='application/force-download')
    #response['X-Sendfile'] = path_to_file
    #response['Content-Length'] = os.path.getsize(path_to_file)
    #response['Content-Disposition'] = 'attachment; filename="%s"' % file_name
    #return response

    #response = HttpResponse(mimetype='application/force-download')
    #response['Content-Disposition'] = 'attachment; filename=%s' % filename
    #response['X-Sendfile'] = path_to_file
    #return response

    #contract = get_object_or_404(Contract, pk=id, owner=request.user)
    #response = HttpResponse(mimetype='application/force-download')
    #response['Content-Disposition'] = 'attachment;filename="%s"' % smart_str(contract.contract_file.name)
    #response["X-Sendfile"] = "%s%s" % (settings.FILE_UPLOAD_DIR, contract.contract_file.name)
    #response['Content-length'] = contract.contract_file.size
    #return response
