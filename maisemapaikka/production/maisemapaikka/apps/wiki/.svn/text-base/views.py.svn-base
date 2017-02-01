# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf

from maisemapaikka.apps.wiki.models import Page
from maisemapaikka.apps.wiki.forms import PageForm

from unidecode import unidecode
from django.template import defaultfilters
import uuid

import datetime
#from django.utils.timezone import utc
#import pytz

def preview_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        content = page.content
        d = {'page_name': page_name, 'content': content}
        return render_to_response('wiki/preview.html', d,
                                  context_instance=RequestContext(request))
    except Page.DoesNotExist:
        d = {'page_name': page_name}
        return render_to_response('wiki/create.html', d,
                                   context_instance=RequestContext(request))

def create_page(request, page_name):
    content = ''
    page = Page(name=page_name, content=content)
    page.save()
    
    return render_to_response('wiki/edit.html',
                              context_instance=RequestContext(request))

def edit_page(request, slug):
    if request.method == 'POST':
        
        #page = Page()
        form = PageForm(request.POST)
        if form.is_valid():
            
            link_header = form.cleaned_data['link_header']
            header = form.cleaned_data['header']
            content = form.cleaned_data['content']

            return HttpResponse("OK")
            
            #slug = defaultfilters.slugify(unidecode(link_header))
            #uid = uuid.uuid1()
            #now = datetime.datetime.now()
            
            #page = Page.objects.get(pk=slug)
            #link_header = page.link_header
            #content = page.content
            

            


            #if 'update' in request.POST:
            #    # do subscribe
            #    a = 'a'
            #elif 'version' in request.POST:
            #    # do unsubscribe
            #    b = 'b'
    
            ##d = dict(post=post, comments=comments, form=CommentForm(), user=request.user)
            #d = {'page_name': page_name, 'content': content}
            #d.update(csrf(request))
    
            #return render_to_response('wiki/edit.html', d,
            #                          context_instance=RequestContext(request))
            
            #return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = PageForm()
        
        slug_input = u'Tämä on slugitesti'
        slug = defaultfilters.slugify(unidecode(slug_input))
        uid = uuid.uuid1()
        now = datetime.datetime.now()
        
        d = {
            'form': form,
            'crud_role': 'create',
            'slug': slug,
            'uuid': uid,
            'now': now,
            }
        return render_to_response('wiki/edit.html', d,
                                      context_instance=RequestContext(request))

    #page = Page.objects.get(pk=page_name)
    #content = page.content
    
    #d = dict(post=post, comments=comments, form=CommentForm(), user=request.user)
    #d = {'page_name': page_name, 'content': content}
    #d.update(csrf(request))
    
    #return render_to_response('wiki/edit.html', d,
    #                          context_instance=RequestContext(request))

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })


def save_page(request, page_name):
    content = request.POST['content']
    try:
        page = Page.objects.get(pk=page_name)
        page.content = content
    except Page.DoesNotExist:
        page = Page(name=page_name, content=content)
    page.save()
    return HttpResponseRedirect('/maisemapaikka/wiki/' + page_name + '/edit/')
         
         
         