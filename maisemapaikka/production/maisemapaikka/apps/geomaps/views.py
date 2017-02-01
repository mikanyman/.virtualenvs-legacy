# Import django modules
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.contrib.gis.geos import Point
#from django.contrib.gis.gdal import DataSource
# Import system modules
import simplejson
import itertools
import tempfile
import os
# Import custom modules
from maisemapaikka.apps.geomaps.models import Waypoint
from maisemapaikka.apps.geomaps.forms import WaypointForm
from maisemapaikka import settings
#from maisemapaikka.apss.geomaps.waypoints.coordinates import *
from django.forms.models import model_to_dict

def index(request, map=None):
    map = request.GET.get('map')
  
    if map is None:
        waypoints = []
        page_name = 'null'
        aspect = 'map'
        page_name_display = 'All'
        site_string = 'portal/landscapes_map.html'
    else:
        if map == '1':
            waypoints = Waypoint.objects.filter(Q(map_id=1))
            page_name = 'landscapes'
            aspect = 'map'
            page_name_display = 'Maisemat'
            site_string = 'portal/landscapes_map.html'
        elif map == '2':
            waypoints = Waypoint.objects.filter(Q(map_id=2))
            page_name = 'churches'
            aspect = 'map'
            page_name_display = 'Kirkot'
            site_string = 'portal/churches_map.html'
        elif map == '3':
            waypoints = Waypoint.objects.filter(Q(map_id=3))
            page_name = 'rockart'
            aspect = 'map'
            page_name_display = 'Kalliomaalaukset'
            site_string = 'portal/rockart_map.html'
        elif map == '4':
            waypoints = Waypoint.objects.filter(Q(map_id=4))
            page_name = 'mylocation'
            aspect = 'map'
            page_name_display = 'My location'
            site_string = 'portal/mylocation_map.html'
        else:
            waypoints = Waypoint.objects.order_by('name')
            page_name = 'null'
            aspect = 'map'
            page_name_display = 'All'
            site_string = 'portal/landscapes_map.html'
    
    #'Display map'
    ##waypoints = Waypoint.objects.order_by('name')
    #return render_to_response('waypoints/index.html', {
    #    'waypoints': waypoints,
    #    'content': render_to_string('waypoints/waypoints.html', {'waypoints': waypoints}),
    #}, context_instance=RequestContext(request))
    
    # Mikan kokeilu
    'Display map'
    #waypoints = Waypoint.objects.order_by('name')
    return render_to_response(site_string, {
        'page_name': page_name,
        'aspect' : aspect,
        'page_name_display' : page_name_display,
        'waypoints': waypoints,
        'content': render_to_string('includes/waypoints.html', {'waypoints': waypoints}),
    }, context_instance=RequestContext(request))

#def waypointSave(request, object_id=None):
#   if object_id == None:
#       objectsubmission = Waypoint()
#   else:
#       objectsubmission = Waypoints.objects.get(id = object_id)
#       objectsubmission = 
#
#   if request.method == 'POST': # Onko formi lahetetty
#        form = WaypointForm(request.POST, object_id)
#       if form.is_valid(): 
#            #id = form.cleaned_data['id']
#            name = form.cleaned_data['name']
#            lon = form.cleaned_data['lon']
#            lat = form.cleaned_data['lat']
#            form.save()
#            return HttpResponse('<h1>Paikka lisatty onnistuneesti</h1>')
#        else:
#            return HttpResponseNotFound('<h1>Virhe tallennettaessa paikkaa</h1>')

def edit(request):
    if request.method == 'POST':
        form = WaypointForm(request.POST)
        
        if form.is_valid():
            id = form.cleaned_data.get('id', '')
            if not id:
                form.save()
            else:
                form.save(id)
            return HttpResponseRedirect('/mylocation/map/?map=4')
    else:
        form = WaypointForm()
        object = request.GET.get('object_id')
        site_string = 'portal/mylocation_frontpg.html'
        page_name = 'mylocation'
        aspect = 'map'
        page_name_display = 'My location'
        waypoints = Waypoint.objects.filter(Q(id=object))
        return render_to_response(site_string, {
           'waypoints': waypoints,
            'content': render_to_string('includes/waypoints.html', {'waypoints': waypoints}),
        }, context_instance=RequestContext(request))

def save(request):
    'Save waypoints'
    for waypointString in request.POST.get('waypointsPayload', '').splitlines():
        waypointID, waypointX, waypointY = waypointString.split()
        waypoint = Waypoint.objects.get(id=int(waypointID))
        waypoint.geometry.set_x(float(waypointX))
        waypoint.geometry.set_y(float(waypointY))
        waypoint.save()
    return HttpResponse(simplejson.dumps(dict(isOk=1)), mimetype='application/json')

def search(request):
    'Search waypoints'
    # Build searchPoint
    try:
        searchPoint = Point(float(request.GET.get('lng')), float(request.GET.get('lat')))
    except:
        return HttpResponse(simplejson.dumps(dict(isOk=0, message='Could not parse search point')))
    # Search database
    waypoints = Waypoint.objects.distance(searchPoint).order_by('distance')
    # Return
    return HttpResponse(simplejson.dumps(dict(
        isOk=1,
        content=render_to_string('waypoints/waypoints.html', {
            'waypoints': waypoints
        }),
        waypointByID=dict((x.id, {
            'name': x.name,
            'lat': x.geometry.y,
            'lng': x.geometry.x,
        }) for x in waypoints),
    )), mimetype='application/json')

def upload(request):
    'Upload waypoints'
    # If the form contains an upload,
    if 'gpx' in request.FILES:
        # Get
        gpxFile = request.FILES['gpx']
        # Save
        targetPath = tempfile.mkstemp()[1]
        destination = open(targetPath, 'wt')
        for chunk in gpxFile.chunks():
            destination.write(chunk)
        destination.close()
        # Parse
        dataSource = DataSource(targetPath)
        layer = dataSource[0]
        waypointNames = layer.get_fields('name')
        waypointGeometries = layer.get_geoms()
        for waypointName, waypointGeometry in itertools.izip(waypointNames, waypointGeometries):
            waypoint = Waypoint(name=waypointName, geometry=waypointGeometry.wkt)
            waypoint.save()
        # Clean up
        os.remove(targetPath)
    # Redirect
    return HttpResponseRedirect(reverse('waypoints-index'))
