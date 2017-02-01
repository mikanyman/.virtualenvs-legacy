from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.formtools.preview import FormPreview
from specs.members.models import Applicant

class JasenhakemusFormPreview(FormPreview):
    
    preview_template = 'members/jasenhakemus_preview.html'
    form_template = 'members/jasenhakemus_form.html'
    
    def done(self, request, cleaned_data):
        applicant = Applicant(**cleaned_data)
        applicant.save()
        
        context = {
            #'form_completed': form_completed,
            #'applicant_id': applicant_id
            }
        
        return render_to_response('members/add_family_members.html', context, context_instance=RequestContext(request))