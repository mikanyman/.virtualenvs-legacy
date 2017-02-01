from django.template.loader import get_template
from django.template import Context
from specs.portal.models import Entry

def common_entry(entry_id):
    
    try:
        e = Entry.objects.get(id=entry_id)
        if e.entrystatus == 'published':
            t = get_template('entries/common_entry.html')
            c = Context({
                'title': e.title,
                'body': e.body
                })
            entry = t.render(c)
        else:
            entry = '' 
    except Entry.DoesNotExist:
        entry = ''

    return entry



