from django.contrib.gis.db import models as gis
from django.db import models

class Waypoint(models.Model):
    name = models.CharField(max_length=64)
    map_id = models.IntegerField()
    geometry = gis.PointField(srid=4326)
    place = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=1024, blank=True)
    base_map = models.CharField(max_length=32, blank=True)
    map_name = models.CharField(max_length=32, blank=True)
    nearest_address = models.CharField(max_length=64, blank=True)
    area = models.CharField(max_length=64, blank=True)
    n = models.IntegerField(null=True)
    e = models.IntegerField(null=True)
    x = models.IntegerField(null=True)
    y = models.IntegerField(null=True)
    p = models.IntegerField(null=True)
    i = models.IntegerField(null=True)

    objects = gis.GeoManager()
    
    # Relations
    image_of_waypoint = models.ManyToManyField('Image', through="ImageOfWaypoint")
    
    def __unicode__(self):
        return '%s %s %s' % (self.name, self.geometry.y, self.geometry.x)

class Image(models.Model):
    name = models.CharField(max_length=32, blank=True)
    photographer = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return "%s" % (self.name)
    
# Relations
class ImageOfWaypoint(models.Model):
    waypoint = models.ForeignKey(Waypoint)
    image = models.ForeignKey(Image)
    
