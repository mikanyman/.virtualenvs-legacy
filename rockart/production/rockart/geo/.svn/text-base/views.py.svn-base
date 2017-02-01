from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.views.generic.list_detail import object_list, object_detail
from django.db.models import *

from rockart.geo.models import *
from rockart import settings

def index(request):
    waypoints = Waypoint.objects.order_by('name')
    template = "waypoints.html"
    return render_to_response(template, { "waypoints": waypoints, "page_name": "index" })

def search(request, query=None):
    query = request.POST.get('nimi', '')
    
    if query:
        qset = (
            Q(name__icontains=query)
            )
        results = Waypoint.objects.filter(qset).distinct()
    else:
        results = []
        
    template = "search.html"
    return render_to_response(template, { "results": results, "query": query, "page_name": "search" })

def search_all(request, submit=None):
    submit = request.POST.get('listaus', '')

    if submit:
        results = Waypoint.objects.all()
    else:
        results = []
    
    
def save(request):
    conn = MySQLdb.connect (host = "localhost",
                            user = "Rockart",
                            passwd = "Rockart",
                            db = "rockart")
    cursor = conn.cursor ()
    cursor.execute ("select maalaus_nimi, paikkakunta, kuvaus, N, E from maalaukset")
    rows = cursor.fetchall()
   
    for rown in rows:
        print "%s, %s, %f, %f" % (row[0], row[1], float(row[3])/100000, float(row[4])/10000)
       
    cursor.close ()
    conn.close ()

