# -*- coding: UTF-8 -*-
# sql/views.py
# http://b71.myrootshell.com/wrk/specs/sql/init_create_modify/
from django.http import HttpResponse

def init_create_modify(request):

    # kursorin malli: specs/members/views.py
    import psycopg2
    connection = psycopg2.connect("dbname='specs' user='specs' password='specs'")
    cursor = connection.cursor()
    
    #for k, v in kdict.iteritems():
    #    cursor.execute("""
    #        UPDATE members_member
    #        SET tila='%s'
    #        WHERE id=%s""" % (v[0], k))

    cursor.execute('SELECT id, modified from portal_entry')
    rows = cursor.fetchall()
    id_date = []
    
    for row in rows:
        id_date = row
        cursor.execute("""
            UPDATE portal_entry
            SET modified_date='%s'
            WHERE id=%d""" % (id_date[1], id_date[0]))
    
    connection.commit()
    connection.close()
    
    return HttpResponse(id_date)