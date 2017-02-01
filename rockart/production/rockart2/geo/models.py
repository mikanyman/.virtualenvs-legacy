from django.contrib.gis.db import models
     
class Waypoint(models.Model):
    name = models.CharField(max_length=32)
    geometry = models.PointField(srid=4326)
    place = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.geometry.x, self.geometry.y)
