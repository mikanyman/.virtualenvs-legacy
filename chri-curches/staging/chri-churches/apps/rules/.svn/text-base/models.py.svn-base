# -*- coding: utf-8 -*-

from django.db import models
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
import datetime

class Rule(models.Model):
    
    description = models.CharField(max_length=400, verbose_name='name')
    rule = models.TextField(verbose_name='description')
    added = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True, auto_now=True)
 
    def __unicode__(self):
        return self.description[:20]
    
    # http://www.djangorocks.com/hints-and-tips/set-created-updated-datetime-in-your-models.html
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        super(Rule, self).save(*args, **kwargs)
 
    @models.permalink
    def get_absolute_url(self):
        return ('rule-detail', (), {'object_id': self.id}) # () for positional parameters

class RuleForm(ModelForm):
    class Meta:
        model = Rule
