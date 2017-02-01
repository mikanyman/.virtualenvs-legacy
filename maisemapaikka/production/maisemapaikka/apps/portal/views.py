# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import *
from django.http import HttpResponse

import os
if os.name == 'posix':
    from maisemapaikka.apps.geomaps.models import *

from maisemapaikka.apps.wiki.models import RemoteHtml
from django.http import Http404

import chardet
import urllib
import urllib2

from django.http import HttpResponse

#from maisemapaikka import settings

def landscapes_lmedia(request, lmedia_file):
   
    # remote file: http://art.jyu.fi/rmedia/test.html
    l = 'http://art.jyu.fi/rmedia/%s' % lmedia_file
    response = urllib2.urlopen(r)
    rhtml = response.read()

    dict = {
        'page_name': 'landscapes',
        'aspect': 'research',
        'page_name_display': 'Maisemat',
        'rhtml': rhtml,
        }
    return render_to_response('portal/landscapes_rhtml.html', 
        dict,
        context_instance=RequestContext(request))
    
def landscapes_rmedia(request, rhtml_file):

    # TEST
    # http://a199.myrootshell.com/maisemapaikka/landscapes/rmedia/test.html
    # http://a199.myrootshell.com/maisemapaikka/landscapes/rmedia/reippailija.jpg
    # reippailija.jpg --> http://a199.myrootshell.com/maisemapaikka/landscapes/media/reippailija.jpg
    
    # remote file: http://art.jyu.fi/rmedia/test.html
    r = 'http://art.jyu.fi/rmedia/%s' % rhtml_file
    response = urllib2.urlopen(r)
    rhtml = response.read()

    dict = {
        'page_name': 'landscapes',
        'aspect': 'research',
        'page_name_display': 'Maisemat',
        'rhtml': rhtml,
        }
    return render_to_response('portal/landscapes_rhtml.html', 
        dict,
        context_instance=RequestContext(request))

# HOME
def home_frontpg(request):
    dict = {
        'page_name': 'home',
        'aspect': 'frontpg',
        'page_name_display': 'Maisemat',
        }
    return render_to_response('portal/home_frontpg.html', 
        dict,
        context_instance=RequestContext(request))

# LANDSCAPES
def landscapes_frontpg(request):
    dict = {
        'page_name': 'landscapes',
        'aspect': 'frontpg',
        'page_name_display': 'Maisemat',
        }
    return render_to_response('portal/landscapes_frontpg.html', 
        dict,
        context_instance=RequestContext(request))
    
def landscapes_time(request):
    dict = {
        'page_name': 'landscapes',
        'aspect': 'time',
        'page_name_display': 'Maisemat',
        }
    return render_to_response('portal/landscapes_time.html', 
        dict,
        context_instance=RequestContext(request))

def landscapes_photo(request):
    dict = {
        'page_name': 'landscapes',
        'aspect': 'photo',
        'page_name_display': 'Maisemat',
        }
    return render_to_response('portal/landscapes_photo.html', 
        dict,
        context_instance=RequestContext(request))

def landscapes_research(request):
    try:
        rhtml_list = RemoteHtml.objects.filter(tab__tabname='landscapes')
    except RemoteHtml.DoesNotExist:
        raise Http404
    dict = {
        'page_name': 'landscapes',
        'aspect': 'research',
        'page_name_display': 'Maisemat',
        'rhtml_list': rhtml_list,
        }
    
    return render_to_response('portal/landscapes_research.html', 
        dict,
        context_instance=RequestContext(request))
    
def landscapes_rhtml(request):
    
    urlencoded = request.GET.get('url')
    
    response = urllib2.urlopen(urlencoded)
    rhtml = response.read()
    
    dict = {
        'page_name': 'landscapes',
        'aspect': 'research',
        'page_name_display': 'Maisemat',
        'rhtml': rhtml,
        }
    
    return render_to_response('portal/landscapes_rhtml.html', 
        dict,
        context_instance=RequestContext(request))

def landscapes_map(request):
    waypoints = Waypoint.objects.filter(Q(map_id=1))
    waypoints.order_by("name")
    dict = {
        'page_name': 'landscapes',
        'aspect': 'map',
        'page_name_display': 'Maisemat',
        'waypoints' : waypoints,
        }
    return render_to_response('portal/landscapes_map.html', 
        dict,
        context_instance=RequestContext(request))
    
def landscapes_story(request):
    dict = {
        'page_name': 'landscapes',
        'aspect': 'story',
        'page_name_display': 'Maisemat',
        }
    return render_to_response('portal/landscapes_story.html', 
        dict,
        context_instance=RequestContext(request))


# CHURCHES
def churches_frontpg(request):
    dict = {
        'page_name': 'churches',
        'aspect': 'frontpg',
        'page_name_display': 'Kirkot',
        }
    return render_to_response('portal/churches_frontpg.html', 
        dict,
        context_instance=RequestContext(request))
    
def churches_time(request):
    dict = {
        'page_name': 'churches',
        'aspect': 'time',
        'page_name_display': 'Kirkot',
        }
    return render_to_response('portal/churches_time.html', 
        dict,
        context_instance=RequestContext(request))

def churches_photo(request):
    dict = {
        'page_name': 'churches',
        'aspect': 'photo',
        'page_name_display': 'Kirkot',
        }
    return render_to_response('portal/churches_photo.html', 
        dict,
        context_instance=RequestContext(request))

def churches_research(request):
    try:
        rhtml_list = RemoteHtml.objects.filter(tab__tabname='churches')
    except RemoteHtml.DoesNotExist:
        raise Http404
    dict = {
        'page_name': 'churches',
        'aspect': 'research',
        'page_name_display': 'Kirkot',
        'rhtml_list': rhtml_list,
        }
    return render_to_response('portal/churches_research.html', 
        dict,
        context_instance=RequestContext(request))
    
def churches_rhtml(request):
    
    urlencoded = request.GET.get('url')
    
    response = urllib2.urlopen(urlencoded)
    rhtml = response.read()
    
    dict = {
        'page_name': 'churches',
        'aspect': 'research',
        'page_name_display': 'Kirkot',
        'rhtml': rhtml,
        }
    
    return render_to_response('portal/churches_rhtml.html', 
        dict,
        context_instance=RequestContext(request))
    
def churches_map(request):
    waypoints = Waypoint.objects.filter(Q(map_id=2))
    waypoints.order_by("name")
    dict = {
        'page_name': 'churches',
        'aspect': 'map',
        'page_name_display': 'Kirkot',
        'waypoints' : waypoints,
        }
    return render_to_response('portal/churches_map.html', 
        dict,
        context_instance=RequestContext(request))

def churches_story(request):
    dict = {
        'page_name': 'churches',
        'aspect': 'story',
        'page_name_display': 'Kirkot',
        }
    return render_to_response('portal/churches_story.html', 
        dict,
        context_instance=RequestContext(request))

# ROCKART
def rockart_frontpg(request):
    dict = {
        'page_name': 'rockart',
        'aspect': 'frontpg',
        'page_name_display': 'Kalliomaalaukset',
        }
    return render_to_response('portal/rockart_frontpg.html', 
        dict,
        context_instance=RequestContext(request))
    
def rockart_time(request):
    dict = {
        'page_name': 'rockart',
        'aspect': 'time',
        'page_name_display': 'Kalliomaalaukset',
        }
    return render_to_response('portal/rockart_time.html', 
        dict,
        context_instance=RequestContext(request))
    
def rockart_photo(request):
    dict = {
        'page_name': 'rockart',
        'aspect': 'photo',
        'page_name_display': 'Kalliomaalaukset',
        }
    return render_to_response('portal/rockart_photo.html', 
        dict,
        context_instance=RequestContext(request))

def rockart_research(request):
    try:
        rhtml_list = RemoteHtml.objects.filter(tab__tabname='rockart')
    except RemoteHtml.DoesNotExist:
        raise Http404
    dict = {
        'page_name': 'rockart',
        'aspect': 'research',
        'page_name_display': 'Kalliomaalaukset',
        'rhtml_list': rhtml_list,
        }
    return render_to_response('portal/rockart_research.html', 
        dict,
        context_instance=RequestContext(request))
    
def rockart_rhtml(request):
    
    urlencoded = request.GET.get('url')
    
    response = urllib2.urlopen(urlencoded)
    rhtml = response.read()
    
    dict = {
        'page_name': 'rockart',
        'aspect': 'research',
        'page_name_display': 'Kalliomaalaukset',
        'rhtml': rhtml,
        }
    
    return render_to_response('portal/rockart_rhtml.html', 
        dict,
        context_instance=RequestContext(request))
    
def rockart_lhtml(request, lhtml_dir, lhtml_file):
    
    #url = 'http://maisemapaikka.synapse-computing.com/fi/rockart/research/ihtml/%s/%s' % (lhtml_dir, lhtml_file)
    url = 'http://a199.myrootshell.com:8080/maisemapaikka/filestore/media/uploads/%s/%s' % (lhtml_dir, lhtml_file)
    
    # USE THIS
    #response = urllib2.urlopen(url)
    #ihtml_1 = response.read()
    
    response = urllib2.urlopen(url).read()

    # for cp1252
    #ihtml = response.decode('cp1252').encode('utf-8')
    # for ascii
    #ihtml = response.decode('ascii').encode('utf-8')
    # for latin-1
    ihtml = response.decode('latin-1').encode('utf-8')

    # http://www.minvolai.com/blog/2009/11/chardet-detecting-unknown-string-encodings/
    #mysterystring = urllib2.urlopen(url).read()
    #e = chardet.detect(mysterystring)
    #return HttpResponse(e)
        
    #urlencoded = urllib.urlencode(url)
    #response = urllib2.urlopen(urlencoded)
    #ihtml = response.read()

    ####################
    ##    METADATA    ##
    ####################
    
    from apps.notes.models import Note
    note = Note.objects.get(title='Saraakallio I')
    test = 'abc'
    
    dict = {
        'page_name': 'rockart',
        'aspect': 'research',
        'page_name_display': 'Kalliomaalaukset',
        'ihtml': ihtml,
        'note': note,
        'test': url,
        }
    
    return render_to_response('portal/rockart_lhtml.html', 
        dict,
        context_instance=RequestContext(request))
    
def rockart_map(request):
    waypoints = Waypoint.objects.filter(Q(map_id=3))
    waypoints.order_by("name")
    dict = {
        'page_name': 'rockart',
        'aspect': 'map',
        'page_name_display': 'Kalliotaide',
        'waypoints' : waypoints,
        }
    return render_to_response('portal/rockart_map.html', 
        dict,
        context_instance=RequestContext(request))
    
def rockart_story(request):
    dict = {
        'page_name': 'rockart',
        'aspect': 'story',
        'page_name_display': 'Kalliomaalaukset',
        }
    return render_to_response('portal/rockart_story.html', 
        dict,
        context_instance=RequestContext(request))

# MYLOCATION
def mylocation_frontpg(request):
    dict = {
        'page_name': 'mylocation',
        'aspect': 'frontpg',
        'page_name_display': 'Minun paikkani',
        }
    return render_to_response('portal/mylocation_frontpg.html', 
        dict,
        context_instance=RequestContext(request))
    
def mylocation_map(request):
    waypoints = Waypoint.objects.filter(Q(map_id=4))
    waypoints.order_by("name")
    dict = {
        'page_name': 'mylocation',
        'aspect': 'map',
        'page_name_display': 'Minun paikkani',
        'waypoints' : waypoints,
        }
    return render_to_response('portal/mylocation_map.html', 
        dict,
        context_instance=RequestContext(request))