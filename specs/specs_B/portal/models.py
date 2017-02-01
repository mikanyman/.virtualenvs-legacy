# -*- coding: utf-8 -*-
# specs/portal/models.py

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from specs.modules import request_params
import datetime
import re


class Application(models.Model):
    label = models.CharField(max_length=30)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['order']
        verbose_name_plural = _(u'sovellukset (Application)')
        verbose_name = _(u'sovellus')

class Callable(models.Model):
    label = models.CharField(max_length=100)
    call = models.CharField(max_length=100, blank=True, null=True)
    template = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.call, self.template)
    class Meta:
        ordering = ['label']
        verbose_name_plural = _(u'ohjelmakomponentit (Callable)')
        verbose_name = _(u'ohjelmakomponentti')
  
class Layout(models.Model):
    label = models.CharField(max_length=30)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['label', 'order']
        verbose_name_plural = _(u'layoutit (Layout)')
        verbose_name = _(u'layout')

class Form(models.Model):
    label = models.CharField(max_length=30)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['label', 'order']
        verbose_name_plural = _(u'lomakeluokat (Form)')
        verbose_name = _(u'lomakeluokka')

class FormLayout(models.Model):
    label = models.CharField(max_length=30)
    form = models.ForeignKey(Form)
    legend = models.CharField(max_length=100)
    intro = models.TextField(blank=True, null=True)
    endnote = models.TextField(blank=True, null=True)
    submit = models.CharField(max_length=30)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['label', 'order']
        verbose_name_plural = _(u'lomakepohjat (FormLayout)')
        verbose_name = _(u'lomakepohja')

class Template(models.Model):
    label = models.CharField(max_length=30)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['order']
        verbose_name_plural = _(u'templatet (Template)')
        verbose_name = _(u'template')

class Menu(models.Model):
    label = models.CharField(max_length=30)
    visible_name = models.CharField(max_length=30)
    template = models.ForeignKey(Template, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['order']
        verbose_name_plural = _(u'menut (Menu)')
        verbose_name = _(u'menu')

class Menuitem(models.Model):
    label = models.CharField(max_length=30)
    visible_name = models.CharField(max_length=30)
    query_string = models.CharField(max_length=100, blank=True, null=True)
    page = models.ForeignKey('Page') # refered page
    application = models.ForeignKey(Application)
    menu = models.ForeignKey(Menu, related_name='FK_Menuitem_menu')
    submenu = models.ForeignKey(Menu, blank=True, null=True, related_name='FK_Menuitem_submenu')
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['menu', 'order']
        verbose_name_plural = _(u'menulinkit (MenuItem)')
        verbose_name = _(u'menulinkki')
        
class Tab(models.Model):
    label = models.CharField(max_length=30)
    visible_name = models.CharField(max_length=30)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['order']
        verbose_name_plural = _(u'pääosastot (Tab)')
        verbose_name = _(u'pääosasto')

class Page(models.Model):
    label = models.CharField(max_length=30, verbose_name="tunniste")
    visible_name = models.CharField(max_length=50, verbose_name="näkyvä nimi")
    parent = models.ForeignKey('self', blank=True, null=True) # TO-DO: remove null=True
    tab = models.ForeignKey(Tab)
    application = models.ForeignKey(Application)
    layout = models.ForeignKey(Layout)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['application', 'order', 'visible_name']
        verbose_name_plural = _(u'sivut (Page)')
        verbose_name = _(u'sivu')

class Box(models.Model):
    label = models.CharField(max_length=30)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['label', 'order']
        verbose_name_plural = _(u'taustat (Box)')
        verbose_name = _(u'tausta')
    
class Celllocation(models.Model):
    label = models.CharField(max_length=3)
    
    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['label']
        verbose_name_plural = _(u'solujen sijainnit (CellLocation)')
        verbose_name = _(u'solun sijainti')
         
class Cell(models.Model):
    label = models.CharField(max_length=30)
    application = models.ForeignKey(Application)
    page = models.ForeignKey(Page)
    celllocation = models.ForeignKey(Celllocation)
    box = models.ForeignKey(Box)
    order = models.IntegerField(blank=True, null=True)
    # ManyToMany with Entry
    
    def __unicode__(self):
        return u'%s' % self.label
    class Meta:
        ordering = ['label']
        verbose_name_plural = _(u'solut (Cell)')
        verbose_name = _(u'solu')

class Include(models.Model):
    label = models.CharField(max_length=30)
    path = models.CharField(max_length=100)
    order = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % self.path
    class Meta:
        ordering = ['path']
        verbose_name_plural = _(u'HTML-tekstit (Include)')
        verbose_name = _(u'HTML-teksti')
        
class Category(models.Model):
    visible_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="kategoria (näkyvä nimi)")
    label = models.CharField(max_length=50, blank=True, null=True, verbose_name="kategoria (tunniste)")
    pages = models.ManyToManyField(Page, blank=True, null=True, verbose_name="sivu")
    
    def __unicode__(self):
        return u'%s' % self.label
    class Meta: 
        ordering = ['label']
        verbose_name_plural = _(u'kategoriat (Category)')
        verbose_name = _(u'kategoria')
        
class Entrystatus(models.Model):
    status = models.CharField(max_length=30, verbose_name=_(u'Tila'))
    order = models.IntegerField(verbose_name=_(u'Järjestys'))
    default_status = models.IntegerField(blank=True, null=True, verbose_name='Oletustila')

    def __unicode__(self):
        return u'%s' % self.status
    class Meta:
        ordering = ['order']
        verbose_name_plural = _(u'Jutun tilavaihtoehdot (EntryStatus)')
        verbose_name = _(u'Jutun tila')
        
class Entry(models.Model):
    PROFILE_CHOICES = (
        ('all', _(u'Kaikki')),
        ('small', _(u'Lyhyet')),
        ('tall', _(u'Pitkät')),
    )
    LANGUAGE_CHOICES = (
        ('fi', 'Suomi'),
        ('en', 'Englanti'),
    )
    ENTRYSTATUS_CHOICES = (
        ('draft', 'Luonnos'),
        ('needs_approval', 'Odottaa tarkistusta'),
        ('pending', 'Valmis julkaistavaksi'),
        ('published', 'Julkaistu'),
        ('archived', 'Arkistoitu'),
    )
    FAKE_BOOLEAN = (
        ('1', 'Näytä Ajankohtaista-palstan Lue lisää-linkki'),
    )

    label = models.CharField(max_length=50, verbose_name='tunniste', help_text='tunniste: sivu, solu, otsikon lyhenne')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='otsikko')
    abstract = models.TextField(blank=True, null=True, verbose_name='ajankohtaista')
    show_abstract = models.BooleanField(default=True, verbose_name='näytä Ajankohtaista-teksti etusivulla')
    show_more = models.BooleanField(default=True, verbose_name='näytä Ajankohtaista-palstan Lue lisää-linkki')
    body = models.TextField(blank=True, null=True, verbose_name='teksti')
    creator = models.ForeignKey(User, verbose_name=u'tekijä')
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='fi_FI', verbose_name='kieli')
    profile = models.CharField(max_length=10, choices=PROFILE_CHOICES, default='all', verbose_name=u'kohderyhmä')
    application = models.ForeignKey(Application, verbose_name='sovellus (Application)')
    tab = models.ForeignKey(Tab, verbose_name='välilehti (Tab)')
    categories = models.ManyToManyField(Category, blank=True, null=True, verbose_name='kategoriat (Categories)')
    entrystatus = models.CharField(max_length=20, choices=ENTRYSTATUS_CHOICES, default='draft', verbose_name='jutun tila')
    list_latest = models.BooleanField(default=True, verbose_name='näytä etusivun Uusimmat-luettelossa')
    created = models.DateTimeField(editable=False, verbose_name='luotu')
    modified = models.DateTimeField(editable=False, verbose_name='muokattu')
            
    def __unicode__(self):
        return u'%s' % self.label
    class Meta: 
        ordering = ['-created']
        verbose_name_plural = _(u'jutut (Entry)')
        verbose_name = _(u'juttu')
        get_latest_by = 'created'
    def get_absolute_url(self):
        return '/%s/%s/e0/%s/%s/%i/' % (self.language, self.profile, self.application, self.tab, self.id)
    def save(self):
        ## Documented in http://www.b-list.org/weblog/2006/nov/02/django-tips-auto-populated-fields/
        if not self.id:
            self.created = datetime.datetime.today()
            # self.tab = 2 # TO-DO: Yritettiin määrittää default arvo mutta ei toiminut
        self.modified = datetime.datetime.today()
        super(Entry, self).save()

class Feed(models.Model):
    CONFIRM = (
        ('t', _(u'Varmistettu')),
    )
    label = models.CharField(max_length=50, verbose_name='nimike (Label)')
    entry = models.ForeignKey(Entry, blank=True, null=True, verbose_name='teksti (Entry)')
    application = models.ForeignKey(Application, blank=True, null=True, verbose_name='sovellus (Application)')
    menu = models.ForeignKey(Menu, blank=True, null=True, verbose_name='menu (Menu)')
    include = models.ForeignKey(Include, blank=True, null=True, verbose_name='HTML-teksti (Include)')
    callable = models.ForeignKey(Callable, blank=True, null=True, verbose_name='ohjelma (Callable)')
    cells = models.ManyToManyField(Cell, verbose_name='solut (Cells)')
    auth = models.BooleanField(verbose_name='vaatii kirjautumisen')
    confirmation = models.CharField(max_length=20, blank=True, null=True, choices=CONFIRM, verbose_name='varmistus')

    def __unicode__(self):
        return u'%s' % self.label

    class Meta: 
        ordering = ['label']
        verbose_name_plural = _(u'syötteet (Feed)')
        verbose_name = _(u'syöte')
        
class Test(models.Model):
    slug = models.SlugField(max_length=50, verbose_name='Tunniste', help_text='Tunniste: sivu, solu, otsikon lyhenne')
    creator = models.ForeignKey(User, related_name='test_creator')


