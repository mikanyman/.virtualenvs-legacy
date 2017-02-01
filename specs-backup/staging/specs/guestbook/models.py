# -*- coding: utf-8 -*-

# specs/guestbook/models.py

from django.db import models
from django import forms
from django.utils.translation import ugettext as _
#from django.contrib import admin

# User-luokka antaa rekisteroitumattomille kauttajille
# kirjoitusoikeuden vieraskirjaan.
#
# Halutessaan rekisteroitymattomat kayttajat voivat rekisteroitya
# Tata mahdollisuutta tulee tarjota (TO-DO)

class Entry(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    first_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)
    ip_address = models.IPAddressField(blank=True, null=True, editable=False)

    def __unicode__(self):
        return u'%s' % self.username
    class Meta:
        ordering = ('-id',)
        verbose_name = _(u'kirjoitus')
        verbose_name_plural = _(u'Kirjoitukset')

class EntryForm(forms.Form):
    username = forms.CharField(label='Nimi', widget=forms.TextInput(
        attrs={'size':'40'}))
    email = forms.EmailField(label='Sähköposti', widget=forms.TextInput(
        attrs={'size':'40'}), required=False, help_text='&nbsp;&nbsp;(Ei näytetä viestissä)')
    content = forms.CharField(label='Viesti', widget=forms.Textarea(
        attrs={'cols':'60', 'rows':'10'}))

    #def clean_content(self):
    #    content = self.cleaned_data.get('username', '')
    #    if len(content) < 20:
    #         raise forms.ValidationError(u'Viestin on oltava vähintään ' + str(20) + ' merkin mittainen.')    
    #    return content

#admin.site.register(Entry)