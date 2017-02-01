from django.contrib.gis.db import models as gis
from django.db import models
from django.contrib import admin
from maisemapaikka.apps.geomaps.widgets import *

class Waypoint(models.Model):
    name = models.CharField(max_length=64)
    map_id = models.IntegerField()
    #location =  models.CharField(max_length=1024, blank=True, null=True)
    location = LocationField(blank=True, max_length=1024)
    lon = models.FloatField()
    lat = models.FloatField()
    #area = models.FloatField()
    description = models.CharField(max_length=2048, blank=True, null=True)

    # GIS Related objects
    geometry = gis.PointField(srid=4326, null=True, blank=True, editable=False)
    objects = gis.GeoManager()
  
    def __unicode__(self):
        return '%s %s %s' % (self.name, self.lon, self.lat)

class WaypointAdmin(admin.ModelAdmin):
    list_display = ['name', 'map_id', 'description', 'location', 'geometry']
    list_filter = ['name', 'map_id']
    ordering = ['map_id', 'name']
    search_fields = ['name', 'location']
    
    #def save_model(self, request, obj, form, change):
    #    obj.geometry = 'POINT('+str(form.cleaned_data['lon'])+' '+str(form.cleaned_data['lat'])+')'
    #    obj.save(force_insert=True)
    
class Image(models.Model):
    path = models.CharField(max_length=128)
    photographer = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    waypoint = models.ForeignKey(Waypoint)
    
    def __unicode__(self):
        return "%s" % (self.path)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['path', 'photographer', 'description', 'waypoint']
    list_filter = ['waypoint']
    ordering = ['waypoint',]
    search_fields = ['waypoint']

admin.site.register(Waypoint, WaypointAdmin)    
admin.site.register(Image, ImageAdmin)  