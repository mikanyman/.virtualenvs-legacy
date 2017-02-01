import datetime

#from django.db import models
from django.db.models import CharField, DateTimeField, ForeignKey, TextField, ManyToManyField, Model
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class Page(Model):
    name = CharField(max_length=30)

    def __unicode__(self):
        return self.name
    
class Lang(Model):
    label = CharField(max_length=2)

    def __unicode__(self):
        return self.label



# autocomplete http://www.b-list.org/weblog/2008/dec/24/admin/
# django-autoslug 1.3.8 Examples http://pypi.python.org/pypi/django-autoslug/1.3.8
# Django Autoslug v1.3 documentation http://packages.python.org/django-autoslug/index.html

class Entry(Model):
    title = CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True) # not unique = for humans; if needed create unique
    summary = TextField(blank=True, null=True)
    content = TextField()
    page = ForeignKey(Page)
    author = ForeignKey(User)
    lang = ForeignKey(Lang)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'created'
        ordering = ('-created',)
        verbose_name_plural = 'entries'
    
    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return "/%s/%s/" % (self.lang, self.page)
        #return "/%s/" % self.created.strftime("%Y/%b/%d",)
