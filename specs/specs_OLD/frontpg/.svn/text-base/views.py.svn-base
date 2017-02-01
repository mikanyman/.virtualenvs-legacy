# -*- coding: UTF-8 -*-
# specs/frontpg/views.py

from django.shortcuts import render_to_response
from django.template import RequestContext
from specs.modules import PortalContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from specs.questionaries.forms import Questionary1Form
from specs.questionaries.models import Questionary1

def index(request, url_lang, url_profile, url_event, url_app, url_pg):
    context = PortalContext.context(request, url_lang, url_profile, url_event, url_app, url_pg)
    template = 'frontpg/'+ str(url_pg) +'.html'
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return response

def index_id(request, url_lang, url_profile, url_event, url_app, url_pg, url_id):
    context = PortalContext.context(request, url_lang, url_profile, url_event, url_app, url_pg, url_id)
    template = 'frontpg/'+ str(url_pg) +'.html'
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return response

def cur_poll(request, url_lang, url_profile, url_event, url_app, url_pg):
    
    """ TO-DO: poimi tietokannasta """
    url_id = 1
    next = '/%s/%s/%s/%s/%s/polls/%i/'  % (url_lang, url_profile, url_event, url_app, url_pg, url_id)
    return HttpResponseRedirect(next)

def poll(request, url_lang, url_profile, url_event, url_app, url_pg, url_id):

    extra_context = {}
    ## send email goes here
    
    if request.POST:
        form = Questionary1Form(request.POST)
        if form.is_valid():
            q1 = Questionary1()

            q1.q1text = form.cleaned_data['q1text']
            q1.q2text = form.cleaned_data['q2text']
            q1.q3text = form.cleaned_data['q3text']
            q1.q4text = form.cleaned_data['q4text']
            q1.q51radio = form.cleaned_data['q51radio']
            q1.q52radio = form.cleaned_data['q52radio']
            q1.q53radio = form.cleaned_data['q53radio']
            q1.q6text = form.cleaned_data['q6text']
            q1.q7text = form.cleaned_data['q7text']
            q1.q8text = form.cleaned_data['q8text']
            q1.q9text = form.cleaned_data['q9text']
            q1.q11text = form.cleaned_data['q11text']
            q1.save()

            extra_context = {'poll_sent': 1}
    else:
        form = Questionary1Form()        
        extra_context = {'form': form}
    
    context = PortalContext.context(request, url_lang, url_profile, url_event, url_app, url_pg, **extra_context)
    template = 'frontpg/'+ str(url_pg) +'.html'
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return response