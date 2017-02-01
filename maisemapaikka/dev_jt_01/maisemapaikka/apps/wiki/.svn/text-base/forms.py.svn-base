# -*- coding: utf-8 -*-

from django import forms
from tinymce.widgets import TinyMCE

class PageForm(forms.Form):
    
    link_header = forms.CharField(
        max_length="40",
        label='Linkkiotsikko',
        widget=forms.TextInput(attrs={'size': 50}),
        help_text=u'Lyhyt otsikko linkkejä varten. Enimmäispituus 40 merkkiä.'
        )
    header = forms.CharField(
        max_length="80",
        label='Otsikko',
        widget=forms.TextInput(attrs={'size': 80}),
        help_text=u'Otsikko. Enimmäispituus 80 merkkiä.'
        )
    content = forms.CharField(
        label=u'Sisältö',
        widget=TinyMCE(attrs={'cols': 70, 'rows': 30}),
        #widget=forms.Textarea(attrs={'cols': 70, 'rows': 20}),
        help_text=u'Tekstikentän kokoa voi muuttaa oikeasta alareunasta.'
        )

    class Media:
        js = ("/static/tiny_mce/tiny_mce.js", "/static/js/textareas.js")
