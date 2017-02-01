# -*- coding: utf-8 -*-
# specs/tagforum/models.py

from django.db import models
from django import forms
from django.utils.translation import ugettext as _

""" Tagging """
# http://www.mail-archive.com/django-users@googlegroups.com/msg54706.html
import tagging
#from tagging.models import Tag
from tagging.fields import TagField
#from tagging_autocomplete.models import TagAutocompleteField
#from tagging_autocomplete.widgets import TagAutocomplete

# User-luokka antaa rekisteroitumattomille kauttajille
# kirjoitusoikeuden vieraskirjaan.
#
# Halutessaan rekisteroitymattomat kayttajat voivat rekisteroitya
# Tata mahdollisuutta tulee tarjota (TO-DO)

class Entry(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    spam = models.NullBooleanField(blank=True, null=True)
    first_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)
    ip_address = models.IPAddressField(blank=True, null=True, editable=False)
    tag_list = TagField() # TagAutocompleteField()
    
    def __unicode__(self):
        return u'%s' % self.username
    
    @models.permalink
    def get_absolute_url(self):
        return ('entry_tag_list')
      
    class Meta:
        ordering = ('-id',)
        verbose_name = _(u'puheenvuoro')
        verbose_name_plural = _(u'Keskustelupalsta')

def t_list(self):
    return 'ABC'

class EntryForm(forms.Form):
    username = forms.CharField(label='Nimi', widget=forms.TextInput(
        attrs={'size':'40'}))
    email = forms.EmailField(label='Sähköposti', widget=forms.TextInput(
        attrs={'size':'40'}), required=False, help_text="<span class='help_text'>Ei näytetä viestissä</note>")
    content = forms.CharField(label='Viesti', widget=forms.Textarea(
        attrs={'cols':'60', 'rows':'10'}))
    tag_list = forms.CharField(label='Aiheet', widget=forms.TextInput(
        attrs={'size':'40'}), help_text='')
    #tag_list = forms.MultipleChoiceField(label="Aiheet", widget=forms.CheckboxSelectMultiple, choices={'A': 'A'})
    #tag_list = forms.TagField(widget=TagAutocomplete())


        #l = Entry.tag_list
        #return l
        
    #def clean_content(self):
    #    content = self.cleaned_data.get('username', '')
    #    if len(content) < 20:
    #         raise forms.ValidationError(u'Viestin on oltava vähintään ' + str(20) + ' merkin mittainen.')    
    #    return content

#admin.site.register(Entry)
try:
    tagging.register(Entry) # , tag_descriptor_attr='tags'
except tagging.AlreadyRegistered:
    pass
