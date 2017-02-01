# -*- coding: utf-8 -*-
# synapse/segments/models.py

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from django.db.models import Model, ForeignKey, CharField, TextField, DateTimeField # ManyToManyField
#from synapse.docs import Lang


class Page(Model):
    name = CharField(max_length=30)

    def __unicode__(self):
        return self.name



class Lang(Model):
    label = CharField(max_length=2)

    def __unicode__(self):
        return self.label
    

class Segment(Model):
    
    start = CharField(max_length=30, blank=True, null=True)
    end = CharField(max_length=30, blank=True, null=True)
    nomentype = CharField(max_length=200, blank=True, null=True)
    nomen = CharField(max_length=200, blank=True, null=True)
    note = TextField(blank=True, null=True)

    author = ForeignKey(User, related_name='%(app_label)s_%(class)s_related')
    lang = ForeignKey(Lang)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return u'%s' % self.id
    
    class Meta:
        ordering = ('-id',)
        verbose_name = _(u'segmentti')
        verbose_name_plural = _(u'segmentit')
        
    def get_absolute_url(self):
        return "/segments/%s/" % (self.id,)
