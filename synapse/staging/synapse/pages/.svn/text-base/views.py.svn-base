from django.shortcuts import render_to_response
from django.template import RequestContext

#from django.contrib.auth.decorators import login_required

from synapse.pages.models import Entry

#@login_required
def index(request, lang, page):
    
    ### select layout for page
    if page == 'company': layout = 'layout_ms.html'
    elif page == 'standards': layout = 'layout_ms.html'
    elif page == 'technologies': layout = 'layout_ms.html'
    elif page == 'projects': layout = 'layout_ms.html'
    elif page == 'products': layout = 'layout_ms.html'
    elif page == 'services': layout = 'layout_ms.html'
    else: layout = 'layout_ms.html'
    
    entries = Entry.objects.filter(
        lang__label__exact=lang,
        page__name__exact=page
        ).order_by('-updated')
    
    # synchronizes session with url
    request.session['django_language'] = lang
    
    context = {
        'entries': entries,
        'lang': lang,
        'page': page,
        'layout': layout
        }
    
    return render_to_response('index.html', context, 
        context_instance=RequestContext(request))
