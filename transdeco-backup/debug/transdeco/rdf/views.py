# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from rdflib.Graph import Graph
from rdflib.Literal import Literal
from rdflib.Namespace import Namespace

def index(request):
    return render_to_response('rdf/geomaster.html')

def kommuner(request):
    g = Graph()
    g.parse("http://kulturarvsdata.se/resurser/aukt/geo/municipality/municipality.rdf") # Kommun

    graph_as_list = []
    init = ''
    initial_letter = ''
    
    if request.GET:
        init = request.GET['init']

        if init == 'all':
            initial_letter = ''
        elif init == 'AR':
            initial_letter = u'Å'
            initial_letter.encode('UTF-8')
            #initial_letter = 'Å'
            #initial_letter = '\xc5'
            #initial_letter = u'\xc5'
            #initial_letter.encode('HEX')
        else:
            initial_letter = init
    
    for row in g.query("\
        PREFIX attribute: <http://kulturarvsdata.se/schema/ksamsok-rdf#>\
        SELECT ?o\
        WHERE {\
            ?s attribute:name ?o . FILTER regex(?o, '^%s')\
        }\
        ORDER BY ?o" % initial_letter):
        graph_as_list.append(row[0])
        
    return render_to_response('rdf/kommuner.html', {'graph_as_list': graph_as_list})


def lan(request):
    g = Graph()
    g.parse("http://kulturarvsdata.se/resurser/aukt/geo/county/county.rdf") # Län
    #g.parse("http://kulturarvsdata.se/resurser/aukt/geo/municipality/municipality.rdf") # Kommun
    #g.parse("http://kulturarvsdata.se/resurser/aukt/geo/province/province.rdf") # Landskap
    #g.parse("http://kulturarvsdata.se/resurser/aukt/geo/parish/parish.rdf") # Socken

    graph_as_list = []
    
    for row in g.query("\
        BASE <http://kulturarvsdata.se/>\
        PREFIX attribute: <http://kulturarvsdata.se/schema/ksamsok-rdf#>\
        SELECT ?o\
        WHERE {\
            ?p attribute:name ?o . FILTER regex(?p, '/[0-9]{2}$')\
        }\
        ORDER BY ?o"):
        graph_as_list.append(row[0])
        
    return render_to_response('rdf/lan.html', {'graph_as_list': graph_as_list})


def lan2(request):
    g = Graph()
    g.parse("http://kulturarvsdata.se/resurser/aukt/geo/county/county.rdf") # Län
    #g.parse("http://kulturarvsdata.se/resurser/aukt/geo/municipality/municipality.rdf") # Kommun
    #g.parse("http://kulturarvsdata.se/resurser/aukt/geo/province/province.rdf") # Landskap
    #g.parse("http://kulturarvsdata.se/resurser/aukt/geo/parish/parish.rdf") # Socken

    graph_as_list = []
    
    for row in g.query("\
        PREFIX attribute: <http://kulturarvsdata.se/schema/ksamsok-rdf#>\
        PREFIX country: <http://kulturarvsdata.se/resurser/aukt/geo/country#>\
        SELECT ?o\
        WHERE {\
            ?p attribute:name country:se .\
        }\
        ORDER BY ?o"):
        graph_as_list.append(row[0])
        
    return render_to_response('rdf/lan.html', {'graph_as_list': graph_as_list})


def intro_sparql(request): 
    """ Introduction to using SPARQL to query an rdflib graph - http://code.google.com/p/rdflib/wiki/IntroSparql """
    g = Graph()
    g.parse("http://bigasterisk.com/foaf.rdf")
    g.parse("http://www.w3.org/People/Berners-Lee/card.rdf")
    FOAF = Namespace("http://xmlns.com/foaf/0.1/")
    g.parse("http://danbri.livejournal.com/data/foaf") 
    [g.add((s, FOAF['name'], n)) for s,_,n in g.triples((None, FOAF['member_name'], None))]
    graph_as_list = []
    """ The Graph.parse 'initNs' argument is a dictionary of namespaces to be expanded in the query string """
    """ Example 'row': (rdflib.Literal('Dan Brickley', language=u'en', datatype=None), rdflib.Literal('Brad Fitzpatrick', language=u'en', datatype=None))  """
    for row in g.query(
        'SELECT ?aname ?bname \
         WHERE {\
             ?a foaf:knows ?b .\
             ?a foaf:name ?aname .\
             ?b foaf:name ?bname .\
             }', initNs=dict(foaf=Namespace("http://xmlns.com/foaf/0.1/"))):
        exec "line = '%s knows %s'" % row
        row = row # explore...
        graph_as_list.append(line)
    context = {
        'row': row,
        'graph': graph_as_list,
        }
    return render_to_response('rdf/intro_sparql.html', context)
        
    
def parse_remote(request):
    """ Reading an NT file - http://code.google.com/p/rdflib/wiki/IntroParsing """
    g = Graph()
    g.parse("http://bigasterisk.com/foaf.rdf")  # , format="xml"
    exec "len_g = 'the lenght of the graph is: %s'" % len(g)
    graph = []
    for stmt in g:
        graph.append(stmt)
    context = {
        'graph': graph,
        'len_g': len_g
        }
    return render_to_response('rdf/parse_remote.html', context)


def read_nt(request):
    """ Reading an NT file - http://code.google.com/p/rdflib/wiki/IntroParsing """
    nt_file ='/var/django/transdeco/rdf/demo.nt'
    g = Graph()
    g.parse(nt_file, format="nt")
    exec "len_g = 'the lenght of the graph is: %s'" % len(g)
    graph = []
    for stmt in g:
        graph.append(stmt)
    context = {
        'len_g': len_g,
        'graph': graph
        }
    return render_to_response('rdf/read_nt.html', context)


def len_graph(request):
    """ This Works..."""

    #store = Graph()
    #store.bind("contact", "http://www.example.com/contact#")
    #store.bind("person", "http://www.example.com/person#")
    #store.bind("xs", "http://www.w3.org/2001/XMLSchema#")
    #store.bind("rdfs", "http://www.w3.org/2000/01/rdf-schema#")
    #store.bind("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    #store.bind("owl", "http://www.w3.org/2002/07/owl#")
    
    # Declare namespaces to use.
    ns_sn = Namespace("http://www.snee.com/ns/misc#")
    ns_sd = Namespace("http://www.snee.com/docs/")
    ns_dc = Namespace("http://purl.org/dc/elements/1.1/")
    ns_pr = Namespace("http://prismstandard.org/1.0#")

    myfile ='/var/rdf/municipality.rdf'

    # Create storage object for triples.
    store = Graph()

    # Add triples to store.
    graph.add((ns_sd["d1001"], ns_dc["title"], Literal("Sample Acrobat document")))
    graph.add((ns_sd["d1001"], ns_dc["format"], Literal("PDF")))
    graph.add((ns_sd["d1001"], ns_dc["creator"], Literal("Billy Shears")))
    graph.add((ns_sd["d1001"], ns_pr["publicationTime"], Literal("2002-12-19")))

    graph.add((ns_sd["d1002"], ns_dc["title"], Literal("Sample RTF document")))
    graph.add((ns_sd["d1002"], ns_dc["format"], Literal("RTF")))
    graph.add((ns_sd["d1002"], ns_dc["creator"], Literal("Nanker Phelge")))
    graph.add((ns_sd["d1002"], ns_pr["publicationTime"], Literal("2002-12-15")))
    
    graph.add((ns_sd["d1003"], ns_dc["title"], Literal("Sample LaTeX document")))
    graph.add((ns_sd["d1003"], ns_dc["format"], Literal("LaTeX")))
    graph.add((ns_sd["d1003"], ns_dc["creator"], Literal("Richard Mutt")))
    graph.add((ns_sd["d1003"], ns_pr["publicationTime"], Literal("2002-12-16")))
    graph.add((ns_sd["d1003"], ns_sn["quality"], Literal("pretty good")))

    #store.parse (myfile)
    rdf_subjects = graph.subjects()
    rdf_predicates = graph.predicates()
    rdf_objects = graph.objects()
    
    select_predicate_by_subject = graph.predicates(subject=ns_sd["d1001"])
    select_object_by_predicate = graph.objects(predicate=ns_dc["title"])

    g = Graph()
    g.parse(myfile, format="xml")
    exec "html = 'the lenght of the graph is: %s'" % len(g)
    
    context = {
        'html': html,
        'g': select_predicate_by_subject
        }

    return render_to_response('len_graph.html', context)
