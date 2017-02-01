# -*- coding: UTF-8 -*-
from django import forms
from django.utils.translation import ugettext as _

# radio
Q51_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)
Q52_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)
Q53_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)

class Questionary1Form(forms.Form):
    q1text = forms.CharField(\
        label=_(u'Mistä sait tiedon yhdistyksen olemassaolosta?'), required=False,\
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'3'}))
    q2text = forms.CharField(\
        label=_(u'Mikä sai sinut liittymään yhdistykseen?'), required=False,\
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'3'}))
    q3text = forms.CharField(\
        label=_(u'Minkä ongelmista koet kohdallasi jo korjaantuneen?'), required=False,\
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'3'}))
    q4text = forms.CharField(\
        label=_(u'Mitä nyt odotat yhdistykseltä?'), required=False,\
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'3'}))
    q51radio = forms.ChoiceField(\
        label=_(u'Vertaistukitapahtumien järjestäminen '), required=False,\
        widget=forms.RadioSelect(), choices=Q51_CHOICES)
    q52radio = forms.ChoiceField(\
        label=_(u'Etujen ajaminen'), required=False,\
        widget=forms.RadioSelect(), choices=Q52_CHOICES)
    q53radio = forms.ChoiceField(\
        label=_(u'Tiedotus tuotteiden ostopaikoista'), required=False,\
        widget=forms.RadioSelect(), choices=Q53_CHOICES)
    q6text = forms.CharField(\
        label=_(u'Parasta, mitä Sinulle on koitunut yhdistyksen jäsenyyden takia?'), required=False,\
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'3'}))
    q7text = forms.CharField(\
        label=_(u'Mikä on tuottanut pettymyksen?'), required=False,\
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'3'}))
    q8text = forms.CharField(\
        label=_(u'Mitä olet ihmetellyt toiminnassa?'), required=False,\
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'3'}))
    q9text = forms.CharField(\
        label=_(u'Toivomuksiasi jäsenlehden sisällöstä?'), required=False,\
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'3'}))
    q10text = forms.CharField(\
        label=_(u'Miksi olet osallistunut/ et ole osallistunut yhdistyksen järjestämiin tapahtumiin?'), required=False,\
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'3'}))
    q11text = forms.CharField(\
        label=_(u'Ehditkö mukaan toimijaksi?'), required=False,\
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'3'}))
