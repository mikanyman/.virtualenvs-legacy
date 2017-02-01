from django.db.models import Q
from specs.apps.eventcal.models import Event

def list_events():
    queryset = Event.objects.all().order_by('evtimestart')
    return queryset

