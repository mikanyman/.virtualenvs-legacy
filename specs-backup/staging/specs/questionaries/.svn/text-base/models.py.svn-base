# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

class Questionary(models.Model):
    title = models.CharField(max_length=200, verbose_name=_(u'Kysymys'))
    intro = models.TextField(verbose_name=_(u'Johdanto'))
    note = models.TextField(verbose_name=_(u'Ohjeet'))
    pub_date = models.DateTimeField(verbose_name=_(u'Julkaisu'))
    
    def __unicode__(self):
        return u'%s' % self.title
    class Meta:
        ordering = ('pub_date',)
        verbose_name = _(u'kysely')
        verbose_name_plural = _(u'Kyselyt')

class Fieldtype(models.Model):
    label = models.CharField(max_length=20, verbose_name=_(u'Nimi'))
    
    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ('label',)
        verbose_name = _(u'kenttätyyppi')
        verbose_name_plural = _(u'Kenttätyypit')

class Question(models.Model):
    questionary = models.ForeignKey(Questionary, verbose_name=_(u'Kysely'))
    question = models.CharField(max_length=200, verbose_name=_(u'Kysymys'))
    fieldtype = models.ForeignKey(Fieldtype, verbose_name=_(u'Kenttätyyppi'))
    textarea_content = models.TextField(blank=True, null=True, verbose_name=_(u'Tekstisisältö'))
    radio_3_horiz = models.NullBooleanField(blank=True, null=True, verbose_name=_(u'Valinta'))
    order = models.IntegerField(verbose_name=_(u'Järjestys'))
    
    def __unicode__(self):
        return u'%s' % self.question
    class Meta:
        ordering = ('order',)
        verbose_name = _(u'kysymys')
        verbose_name_plural = _(u'Kysymykset')
        
class Questionary1(models.Model):
    q1text = models.TextField(blank=True, null=True)
    q2text = models.TextField(blank=True, null=True)
    q3text = models.TextField(blank=True, null=True)
    q4text = models.TextField(blank=True, null=True)
    q51radio = models.CharField(max_length=20, blank=True, null=True)
    q52radio = models.CharField(max_length=20, blank=True, null=True)
    q53radio = models.CharField(max_length=20, blank=True, null=True)
    q6text = models.TextField(blank=True, null=True)
    q7text = models.TextField(blank=True, null=True)
    q8text = models.TextField(blank=True, null=True)
    q9text = models.TextField(blank=True, null=True)
    q11text = models.TextField(blank=True, null=True)
    ip = models.IPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def save(self):
        ## Documented in http://www.b-list.org/weblog/2006/nov/02/django-tips-auto-populated-fields/
        self.ip = '0.0.0.0'
        super(Questionary1, self).save()
        