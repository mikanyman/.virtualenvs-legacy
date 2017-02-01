# -*- coding: utf-8 -*-

from django.db import models
from tinymce import models as tinymce_models
from django.utils.translation import ugettext_lazy as _
from maisemapaikka import settings

class Creator(models.Model):
    firstname = models.CharField(max_length='20')
    lastname = models.CharField(max_length='40')

    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)

    class Meta:
        verbose_name = _(u'creator')
        verbose_name_plural = _(u'Creators')

class Tab(models.Model):
    tabname = models.CharField(max_length='40')
    visiblename = models.CharField(max_length='40')

    def __unicode__(self):
        return u'%s' % self.visiblename

    class Meta:
        verbose_name = _(u'tab')
        verbose_name_plural = _(u'Tabs')

class RemoteHtml(models.Model):
    #creator = models.CharField(max_length='40')
    creator = models.ForeignKey('Creator')
    link_header = models.CharField(max_length='80')
    url = models.URLField(max_length=200, blank=True, null=True)
    tab = models.ForeignKey('Tab')

    def __unicode__(self):
        return u'%s' % self.link_header

    class Meta:
        verbose_name = _(u'remote page')
        verbose_name_plural = _(u'Remote pages')

class Page(models.Model):

    link_header = models.CharField(max_length='40')
    url = models.URLField(max_length=200, blank=True, null=True)
    #header = models.CharField(max_length='40', blank=True, null=True)
    #content = models.TextField(blank=True)
    #content = tinymce_models.HTMLField(blank=True, null=True)
    #slug = models.CharField(max_length='60', blank=True) # , primary_key=True
    
    #creator = models.CharField(max_length='40')
    #moderator = models.CharField(max_length='40')
    #version = models.IntegerField()

    #uuid1_original = models.IntegerField()
    #uuid1_revision = models.IntegerField()

    #time_zone = models.CharField(max_length='30', default=settings.TIME_ZONE, editable=False)
    #first_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)
    #version_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)
    #ip_address = models.IPAddressField(blank=True, null=True, editable=False)
    
    def __unicode__(self):
        return u'%s' % self.link_header

    class Meta:
        verbose_name = _(u'page')
        verbose_name_plural = _(u'Pages')



