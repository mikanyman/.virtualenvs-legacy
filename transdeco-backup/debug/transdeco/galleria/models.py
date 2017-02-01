# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

class Site(models.Model):
    title = models.CharField(max_length=20, verbose_name=_(u'Sivuston nimi'), help_text=u'Näkyy selaimen yläreunassa')
    headline = models.CharField(max_length=50, verbose_name=_(u'Etusivun otsikko'))
    abstract = models.TextField(blank=True, null=True, verbose_name=_(u'Etusivun esittely'))
    footer_text = models.TextField(blank=True, null=True, verbose_name=_(u'Etusivun alareuna'))
    
    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = _(u'sivusto')
        verbose_name_plural = _(u'Sivustot')
        
"""
class Counter(models.Model):
    session_id = models.CharField(max_length=32, verbose_name=_(u'Istunto'))
    ip_number = models.IPAddressField(verbose_name=_(u'IP-numero'))
    created = models.DateTimeField(editable=False, verbose_name='Ajankohta')
    referer = models.CharField(max_length=512, verbose_name=_(u'Edellinen sivu'))

    timestamp, URL, referrer and user-agent

    def __unicode__(self):
        return u'%s' % self.session_id

    class Meta:
        verbose_name = _(u'Laskuri')
        verbose_name_plural = _(u'Laskurin tapahtumat')
        
    def save(self):
        ## Documented in http://www.b-list.org/weblog/2006/nov/02/django-tips-auto-populated-fields/
        if not self.id:
            self.session_id
            self.ip_number = request.META['REMOTE_ADDR']
            self.created
            self.created = datetime.datetime.today()
        super(Entry, self).save()
"""

class Artist(models.Model):
    person_name = models.CharField(max_length=50, unique=True, verbose_name=_(u'nimi'), help_text='Malli: Etunimi Sukunimi') # CDWA: Person/Corporate Body Name
    label = models.CharField(max_length=30, unique=True, verbose_name=_(u'tunniste'), help_text='Malli: gullichsen')
    birth_date = models.IntegerField(blank=True, null=True, verbose_name=_(u'syntymävuosi'), help_text='Malli: 1970 (vain vuosiluku)') # CDWA: Birth Date
    descriptive_note = models.TextField(blank=True, null=True, verbose_name=_(u'esittely'), help_text='Taiteilijan esittely') # CDWA: Person/Corporate Body Descriptive Note
    new_work = models.NullBooleanField(blank=True, null=True, default=False, verbose_name=_(u'Uutta')) 

    artist_image_filename = models.ImageField(upload_to='pics/artists', blank=True, null=True, verbose_name=_(u'taiteilijan kuva'))
    square_image_filename_out = models.ImageField(upload_to='img/square', blank=True, null=True, verbose_name=_(u'neliö (out)'), help_text=u'Etusivun neliömäinen kuva perustilassa')
    square_image_filename_in = models.ImageField(upload_to='img/square', blank=True, null=True, verbose_name=_(u'neliö (in)'), help_text=u'Etusivun neiliömäinen kuva mouse over -tilassa')

    def __unicode__(self):
        return u'%s' % self.person_name
           
    class Meta:
        ordering = ('person_name',)
        verbose_name = _(u'taiteilija')
        verbose_name_plural = _(u'Taiteilijat')
    
    @models.permalink
    def get_absolute_url(self):
        return ('artist_detail', None, {'object_id': self.id})


# DISC: Photographer
class Photographer(models.Model):
    person_name = models.CharField(max_length=50, verbose_name=_(u'nimi'), help_text='Malli: Etunimi Sukunimi') # CDWA: Person/Corporate Body Name
    
    def __unicode__(self):
        return u'%s' % self.person_name

    class Meta:
        ordering = ('person_name',)
        verbose_name = _(u'valokuvaaja')
        verbose_name_plural = _(u'Valokuvaajat')


class TechniqueType(models.Model):
    """ CDWA: Materials/Techniques Description """
    label = models.CharField(max_length=50, verbose_name=_(u'Tekniikka'))

    def __unicode__(self):
        return u'%s' % self.label
    
    class Meta:
        ordering = ('label',)
        verbose_name = _(u'tekniikka')
        verbose_name_plural = _(u'Tekniikat')
        

# CDWA: uses Image in different ways (e.g. digital image; Image as an abstract type.)
class Image(models.Model):
    original_image_filename = models.ImageField(upload_to='pics/original', verbose_name=_(u'originaali')) # DISC: Original File Name
    small_image_filename = models.ImageField(upload_to='pics/small_256', blank=True, null=True, verbose_name=_(u'pieni kuva'))
    medium_image_filename = models.ImageField(upload_to='pics/medium_512', blank=True, null=True, verbose_name=_(u'iso kuva'))

    work = models.ForeignKey('Work', blank=True, null=True, verbose_name='teoksen nimi')
    artist = models.ForeignKey(Artist, blank=True, null=True, verbose_name=_(u'taiteilija'))
    photographer = models.ForeignKey(Photographer, verbose_name='valokuvaaja')
    
    def __unicode__(self):
        return u'%s' % self.work

    class Meta:
        ordering = ('work',)
        verbose_name = _(u'valokuva')
        verbose_name_plural = _(u'Valokuvat')
    
    @models.permalink
    def get_absolute_url(self):
        return ('image_detail', None, {'object_id': self.id})
    

class Work(models.Model):
    title_text = models.CharField(max_length=100, verbose_name=_(u'teoksen nimi')) # CDWA: Title Text
    artist = models.ForeignKey(Artist, blank=True, null=True, verbose_name=_(u'taiteilija'))
    item_number = models.IntegerField(blank=True, null=True, verbose_name=_(u'Nro'))
    mater_tech_descr = models.ForeignKey(TechniqueType, blank=True, null=True, verbose_name='tekniikka') # CDWA: Materials/Techniques Description
    creation_date = models.IntegerField(blank=True, null=True, verbose_name=_(u'vuosiluku')) # CDWA: Creation Date
    edition_size = models.IntegerField(blank=True, null=True, verbose_name=_(u'vedosmäärä')) # CDWA: Edition Size
    dimensions_description = models.CharField(max_length=9, blank=True, null=True, verbose_name=_(u'kuva-ala'), help_text='Esim. 50 x 36') # CDWA: Dimensions Description
    price = models.CharField(max_length=6, blank=True, null=True, verbose_name=_(u'hinta'), help_text=u'Käytä tuhaterotinta, esim. 2 900')
    new_work = models.NullBooleanField(blank=True, null=True, default=False, verbose_name=_(u'Uusi'))
    order = models.IntegerField(blank=True, null=True, verbose_name=_(u'Järjestys'))
    
    def __unicode__(self):
        return u'%s, %s, %d' % (self.artist, self.title_text, self.item_number)
        
    class Meta:
        ordering = ('artist', 'order', 'item_number')
        verbose_name = _(u'teos')
        verbose_name_plural = _(u'Teokset')
    