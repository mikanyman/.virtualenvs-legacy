from django.db import models

class Type(models.Model):
    label = models.CharField(max_length=50)

    def __unicode__(self):
        return self.label
    
class Member(models.Model):
    type = models.ForeignKey(Type)
    label = models.CharField(max_length=50)

    def __unicode__(self):
        return self.label
