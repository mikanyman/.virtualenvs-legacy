## modules/object.py
## forms a pair with list.py - both take params from the URL

from django.db.models import Q
from specs.portal.models import Entry

def get_object(url_pg, url_id=None):
    
    if url_id:
        entry = Entry.objects.get(id=url_id)
        return entry
    else:        
        ## query is identical to get_list.py
        query = Q(entrystatus='published') & Q(categories__pages__label=url_pg)
        entry = Entry.objects.filter(query).latest()
        return entry        
    
