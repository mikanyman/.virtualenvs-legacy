# -*- coding: UTF-8 -*-
# specs/morepg/views.py

from django.shortcuts import render_to_response
from django.template import RequestContext
from specs.modules import PortalContext

def index_id(request, url_lang, url_profile, url_event, url_app, url_pg, url_id):
    context = PortalContext.context(request, url_lang, url_profile, url_event, url_app, url_pg, url_id)
    template = 'morepg/'+ str(url_pg) +'.html'
    response = render_to_response(template, context, context_instance=RequestContext(request))
    return response