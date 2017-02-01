# specs/guestbook/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list
from django.views.generic.create_update import create_object
from specs.guestbook.models import Entry, EntryForm

def list_entries(request):

    ### GENERIC VIEWS
    queryset = Entry.objects.all()
    
    return object_list(request, queryset, paginate_by = 20,)
    
    #obj_list = Entry.objects.all()
    #response = render_to_response('guestbook/entry_list.html', {
    #    'object_list': queryset                    
    #}, context_instance=RequestContext(request))
    #return response
    
def create_entry(request):
   
    if request.method == 'POST':
        form = EntryForm(request.POST)
        entry = Entry()

        if form.is_valid():
            entry.username = form.cleaned_data['username']
            entry.email = form.cleaned_data['email']
            entry.content = form.cleaned_data['content']
            entry.ip_address = request.META['REMOTE_ADDR']
            entry.save()
            return HttpResponseRedirect('/wrk/specs/guestbook/')
        
        else:
            context = {
                'entry_form': form,
            }
            return render_to_response('guestbook/entry_form.html', context)
        
    else:

        form = EntryForm()
        context = {
            'entry_form': form,
        }
    
        ### GENERIC VIEWS
        return create_object(request, Entry, extra_context = context)
        #post_save_redirect = "/" + url_status + "/specs/guestbook/?page=%(id)s/", 