from django.forms import *
from django.db import models
from maisemapaikka.apps.geomaps.widgets import *
from maisemapaikka.apps.geomaps.models import *
from django.db.models import Q

class WaypointForm(Form):
    id = IntegerField(required=False)
    name = CharField(max_length=64)
    description = CharField(max_length=2048)
    location = LocationField(blank=True, max_length=1024)
    lon = FloatField()
    lat = FloatField()

    def save(self, id=None):
        if id is None:
            waypoint = Waypoint(name = self.cleaned_data['name'], map_id = 4, location = ''+str(self.cleaned_data['lat'])+','+str(self.cleaned_data['lon'])+'', description = self.cleaned_data['description'], lat = float(self.cleaned_data['lat']), lon = float(self.cleaned_data['lon']), geometry = 'POINT('+str(self.cleaned_data['lon'])+' '+str(self.cleaned_data['lat'])+')')
            waypoint.save(force_insert=True)
        else:
            waypoint = Waypoint.objects.filter(id=int(id)).update(name = self.cleaned_data['name'], location = ''+str(self.cleaned_data['lat'])+','+str(self.cleaned_data['lon'])+'', description = self.cleaned_data['description'], lat = float(self.cleaned_data['lat']), lon = float(self.cleaned_data['lon']), geometry = 'POINT('+str(self.cleaned_data['lon'])+' '+str(self.cleaned_data['lat'])+')')