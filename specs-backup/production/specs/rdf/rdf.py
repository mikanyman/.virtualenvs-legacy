#!/usr/bin/env python2.4

def age():
    
    from sparta import ThingFactory
    from rdflib.Graph import Graph, URIRef
    #from rdflib import RDF, RDFS
        
    store = Graph()
    store.bind("contact", "http://www.example.com/contact#")
    store.bind("person", "http://www.example.com/person#")
    store.bind("xs", "http://www.w3.org/2001/XMLSchema#")
    store.bind("rdfs", "http://www.w3.org/2000/01/rdf-schema#")
    store.bind("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    store.bind("owl", "http://www.w3.org/2002/07/owl#")
    store.bind("cidoc", "http://www8.informatik.uni-erlangen.de/IMMD8/Services/cidoc_crm/cidoc_crm_4.2.4_owl_dl.owl")

    Thing = ThingFactory(store)
    Thing("person_age", rdfs_range=[Thing("xs_int")])
    Thing("person_age", rdf_type=[Thing("owl_FunctionalProperty")])

    bob = Thing("person_bob", person_age=23)
    
    #return bob.person_age
    #person = Thing("cidoc_person", cidoc_person[Thing()]) # RIVI ANTAA VIRHEEN: global name 'cidoc_person' is not defined
    #return person

a = age()
print a




