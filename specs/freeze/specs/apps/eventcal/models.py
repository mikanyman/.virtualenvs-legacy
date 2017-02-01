# -*- coding: utf-8 -*-

# specs/apps/eventcal.py

from django.db import models
from django.utils.translation import ugettext as _

class Event(models.Model):
    theme = models.CharField(max_length=100, blank=True, null=True, verbose_name='tapahtuman aihe')
    description = models.TextField(blank=True, null=True, verbose_name='tapahtuman kuvaus')
    placename = models.CharField(max_length=100, blank=True, null=True, verbose_name='paikan nimi')
    placedescription = models.TextField(blank=True, null=True, verbose_name='paikan osoite, tulo-ohje')
    evtimestart = models.DateTimeField(blank=True, null=True, verbose_name='alkamis- ajankohta', help_text="kirjoita 00:00 ellet halua kellonaikaa näkyviin")
    evtimend = models.DateTimeField(blank=True, null=True, verbose_name='päättymis- ajankohta', help_text="kirjoita 00:00 ellet halua kellonaikaa näkyviin")
    author = models.CharField(max_length=100, blank=True, null=True, verbose_name='ilmoituksen tekijä tai toivotus')
    first_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)

    def __unicode__(self):
        return u'%s, %s' % (self.theme, self.evtimestart)
    class Meta:
        ordering = ['-evtimestart']
        verbose_name = _(u'tapahtuma')
        verbose_name_plural = _(u'Tapahtumat')
        
class Eventdate(models.Model):
    evtimestart = models.DateTimeField(blank=True, null=True, verbose_name='alkamis- ajankohta')
    evtimend = models.DateTimeField(blank=True, null=True, verbose_name='päättymis- ajankohta')
    event = models.ForeignKey(Event)
        
    def __unicode__(self):
        return u'%s' % self.evtimestart
    class Meta:
        ordering = ['-evtimestart']
        verbose_name = _(u'ajankohta')
        verbose_name_plural = _(u'Ajankohdat')
