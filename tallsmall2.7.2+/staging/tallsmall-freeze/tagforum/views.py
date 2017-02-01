# specs/tagforum/views.py

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from specs.tagforum.models import Entry, EntryForm
from specs.modules import PortalContext

""" generic views """
from django.views.generic.list_detail import object_list
from django.views.generic.create_update import create_object

""" tagging """
from tagging.views import tagged_object_list


def list_entries(request, url_lang, url_profile, url_event, url_app, url_pg):

    context = PortalContext.context(request, url_lang, url_profile, url_event, url_app, url_pg)    
    ## GENERIC VIEWS
    ## generic views use RequestContext by default
    ## TO-DO: generic views voitaisiin siirtaa PortalContext.py moduliin
    return object_list(request,
        queryset = Entry.objects.filter(
            Q(spam__isnull=True) | Q(spam=False)
        ),
        paginate_by = 20,
        template_name = 'tagforum/entry_list.html',
        extra_context = context  
    )
    
def list_tagged_entries(request, url_lang, url_profile, url_event, url_app, url_pg, **kwargs):

    context = PortalContext.context(request, url_lang, url_profile, url_event, url_app, url_pg, **kwargs)

    return tagged_object_list(request,
        queryset_or_model = Entry.objects.filter(
            Q(spam__isnull=True) | Q(spam=False)
        ),
        #queryset_or_model = Entry,
        tag = kwargs['tag'],
        paginate_by = 20,
        allow_empty=True,
        template_name = 'tagforum/entry_list.html',
        extra_context = context  
    )
        
def create_entry(request, url_lang, url_profile, url_event, url_app, url_pg):
      
    if request.method == 'POST':
        form = EntryForm(request.POST)
        entry = Entry()

        if form.is_valid():
            
            ## Ingest content
            entry.username = form.cleaned_data['username']
            entry.email = form.cleaned_data['email']
            entry.content = form.cleaned_data['content']
            entry.tag_list = form.cleaned_data['tag_list']
            entry.ip_address = request.META['REMOTE_ADDR']
            
            # Save if prohibited strings not found
            s = entry.content           
            items = ['href'] # kiellettyjen lista 
            
            x = -1 # no prohibited content
            for item in items:
                x = s.find(item)
                if x > -1: break
                
            if x == -1: # no prohibited content
                entry.save()
            
            redirect_url = '/%s/%s/%s/%s/tagforum_list/' % (url_lang, url_profile, url_event, url_app)
            return HttpResponseRedirect(redirect_url)
        
        else:
            
            ## Empty form
            ## TO-DO: use RequestContext; This part is redundant...
            context = {
                'entry_form': form,
                #'lang': url_lang,
                #'profile': url_profile,
                #'event': url_event,
                #'app': url_app,
                #'pg': url_pg,
            }
            return render_to_response('tagforum/entry_form.html', context)
        
    else:

        redirect_url = '/%s/%s/%s/%s/tagforum_list/' % (url_lang, url_profile, url_event, url_app)

        ## Empty form
        form = EntryForm()
        context = {
            'entry_form': form,
        }
    
        ### GENERIC VIEWS
        return create_object(request, Entry, template_name='tagforum/entry_form.html', extra_context = context)

        #post_save_redirect = "/specs/guestbook/?page=%(id)s/"
        