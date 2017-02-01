from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.views.generic.list_detail import object_list, object_detail
from django.db.models import *

from rockart.geo.models import *
from rockart import settings

# Rockart
def index(request):
    waypoints = Waypoint.objects.filter(
        Q(map_id=3))
    waypoints.order_by("name")
    template = "waypoints.html"
    return render_to_response(template,
                              { "waypoints": waypoints, "page_name": "index" },
                              context_instance=RequestContext(request))

def search(request, query=None):
    if request.POST:
        query = request.POST.get('nimi', '')

        if query:
            qset = (
                Q(name__icontains=query,
                  map_id=3)
                )
            results = Waypoint.objects.filter(qset).distinct()
        else:
            query = request.POST.get('paikkakunta', '')

            if query:
                qset = (
                    Q(place__icontains=query,
                      map_id=3)
                    )
                results = Waypoint.objects.filter(qset).distinct()
            else:
                results = []

        template = "search.html"
        return render_to_response(template, { "results": results, "query": query, "page_name": "search" }, context_instance=RequestContext(request))
    elif request.GET:
        query = request.GET.get('id', '')

        if query:
            results = Waypoint.objects.get(id=query, map_id=3)

            if not results:
                results = []
            
        template = "show-item.html"
        return render_to_response(template, { "results": results, "query": query, "page_name": "show_item" }, context_instance=RequestContext(request))
    else:
        results = []
        template = "search.html"
        return render_to_response(template, { "results": results, "query": query, "page_name": "search" }, context_instance=RequestContext(request))

def search_all(request, query=None):
    results = Waypoint.objects.filter(
        Q(map_id=3))

    template = "search-all.html"
    return render_to_response(template, { "results": results, "query": query, "page_name": "search_all" }, context_instance=RequestContext(request))

# Karttapalvelu
def map_index(request, query=None):
    query = request.GET.get('map', '')

    if not query:
        # Haetaan vakiona Acerbin waypointit, jos ei muuta ehdotettu
        results = Waypoint.objects.filter(
            Q(map_id=1))
    if query:
        results = Waypoint.objects.filter(
            Q(map_id=query))
       
    template = "map-index.html"
    return render_to_response(template, { "results": results, "query": query }, context_instance=RequestContext(request))
            
# Testi
def save(request):
    import sys
    from rockart.geo.coordinates import *
    import MySQLdb
            
    conn = MySQLdb.connect(host = "localhost",user = "Rockart",passwd = "Rockart",db = "rockart")
    cursor = conn.cursor ()
    cursor.execute ("select maalaus_nimi, paikkakunta, kuvaus, N, E from maalaukset")
        
    # Haetaan koordinaattidata tauluista
    cursor.execute ("select maalaus_nimi, paikkakunta, kuvaus, N, E from maalaukset")
            
    rows = cursor.fetchall()
        
    KKJ = {0: 'P', 1: 'I'}
    WGS84 = {0: 'La', 1: 'Lo'}
    i = 0
            
    for row in rows:
        KKJ['P'] = float(row[3])
        KKJ['I'] = float(row[4])
        WGS84 = KKJxy_to_WGS84lalo(KKJ)

        if len(row[0]) <= 32:
            Waypoint(map_id=3, name=''+row[0].decode("latin-1")+'', geometry='POINT('+str(WGS84['Lo'])+' '+str(WGS84['La'])+')').save()
        
    cursor.close ()

