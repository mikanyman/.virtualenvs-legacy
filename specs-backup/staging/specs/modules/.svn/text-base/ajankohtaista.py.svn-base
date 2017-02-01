from django.template.loader import get_template
from django.template import Context
from django.db.models import Q
from specs.portal.models import Entry

def list_ajankohtaista():
   
    # Luettelee kaikki jutut, joissa on taytettyna kentta abstract (=ajankohtaista)

    query = Q(abstract__regex=r'\w+') & Q(entrystatus='published') & Q(show_abstract=True)
    e = Entry.objects.filter(query) # jos jutussa ajankohtaista...
    t = get_template('entries/list_ajankohtaista.html')
    
    c = Context({
            'entries': e,
        })
    entries = t.render(c)
    return entries