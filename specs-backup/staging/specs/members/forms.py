# -*- coding: UTF-8 -*-
from django import forms
from django.utils.translation import ugettext as _

""" ModelForm """
from django.forms import ModelForm
from specs.members.models import Applicant

TILA = (('act', 'Aktiivinen'),('pass', 'Passiivinen'),('trash', 'Poistettu'))

class JasenhakemusForm(ModelForm):

    """ override/customize all """
    etunimi = forms.CharField(label=_(u'Etunimi'), required=True, widget=forms.TextInput(attrs={'size':'40'}))
    sukunimi = forms.CharField(label=_(u'Sukunimi'), required=True, widget=forms.TextInput(attrs={'size':'40'}))
    katuosoite = forms.CharField(label=_(u'Katuosoite'), required=True, widget=forms.TextInput(attrs={'size':'40'}))
    postinumero = forms.CharField(label=_(u'Postinumero'), required=True, widget=forms.TextInput(attrs={'size':'5', 'maxlength':'5'}))
    postitoimipaikka = forms.CharField(label=_(u'Postitoimipaikka'), required=True, widget=forms.TextInput(attrs={'size':'40'}))
    puhelin = forms.CharField(label=_(u'Puhelin'), required=True, widget=forms.TextInput(attrs={'size':'40'}))
    email = forms.EmailField(label=_(u'Sähköposti'), required=False, widget=forms.TextInput(attrs={'size':'40'}))
    syntymaaika = forms.CharField(label=_(u'Syntymäaika'), required=True, 
        widget=forms.TextInput(attrs={'size':'4', 'maxlength':'4'}), 
        help_text=u'<div class="help_text" style="margin-bottom: 8px;">\
                    Ilmoita vain syntymävuosi, esim. 1980\
                    </div>')
    lisatietoja = forms.CharField(label='Perheenjäsenet', required=False, 
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'4'}),
        help_text=u'<div class="help_text" style="width: 400px">\
                    Mainitse tässä ne samassa taloudessa asuvat perheenjäsenet \
                    (nimi ja syntymäaika), jotka myös haluat ilmoittaa yhdistyksen jäseniksi. \
                    Samassa taloudessa elävien perheenjäsenten jäsenmaksu on 0 &euro;.\
                    </div>')
    perheenjasenet = forms.CharField(label=u'Perustelut', required=False, 
        widget=forms.Textarea(attrs={'cols':'60', 'rows':'4'}),
        help_text=u'<div class="help_text" style="width: 400px; margin-bottom: 8px">\
                    Kerro tässä perustelut jäsenyydellesi, \
                    esim. Lyhyt, Pitkä, Pienijalkainen, Isojalkainen (valitse sinua koskeva). Voit kertoa \
                    myös muuta itsestäsi, esim. asioista joista olet kiinnostunut tai mistä haluaisit \
                    tietää lisää.\
                    </div>')

    class Meta:
        model = Applicant
        exclude = ('status', 'tililla')

    
class TunnistetiedotForm(forms.Form):
    # Henkilon tunnistetiedot
    arvo = forms.CharField(label=_(u'Arvo'), required=False, widget=forms.TextInput(attrs={'size':'40'}))
    etunimi = forms.CharField(label=_(u'Etunimi'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    sukunimi = forms.CharField(label=_(u'Sukunimi'), required=False, widget=forms.TextInput(attrs={'size':'40'}))
    ent_sukunimi = forms.CharField(label=_(u'Entinen sukunimi'), required=False, widget=forms.TextInput(attrs={'size':'40'})) 

class JasentiedotForm(forms.Form):
    # Jasentiedot: Tapahtumat
    jasennumero = forms.CharField(label=_(u'Jäsennumero'), widget=forms.TextInput(attrs={'size':'6', 'maxlength':'6'}), required=False)
    liittymisvuosi = forms.CharField(label=_(u'Liittymisvuosi'), widget=forms.TextInput(attrs={'size':'30'}), required=False)
    eroaminen = forms.CharField(label=_(u'Eroaminen'), widget=forms.TextInput(attrs={'size':'20'}), required=False)
    varsinainen = forms.BooleanField(label=_(u'Varsinainen jäsen'), required=False)
    perhe = forms.BooleanField(label=_(u'Perhejäsen'), required=False)
    kannatus = forms.BooleanField(label=_(u'Kannatusjäsen'), required=False)
    kunnia = forms.BooleanField(label=_(u'Kunniajäsen'), required=False)
    yri = forms.BooleanField(label=_(u'Yritysjäsen'), required=False)
    uudet_jasenet = forms.BooleanField(label=_(u'Uusi jäsen'), required=False)
    tila = forms.ChoiceField(label=_(u'Tila'), widget=forms.Select(), required=False, choices=TILA)
    
    def clean_jasennumero(self):
        # salli vain kuusi numeroa
        jasennumero = self.cleaned_data.get('jasennumero', '')
        import re
        pattern = re.compile('^\d{6}$')
        result = pattern.match(jasennumero)
        if not result:
            raise forms.ValidationError(_(u'Jäsennumerossa oltava kuusi numeroa. Vain numerot ovat sallittuja'))
        return jasennumero

class YhteystiedotForm(forms.Form):
    # Henkilon yhteystiedot
    yritys = forms.CharField(label=_(u'Yritys'), required=False, widget=forms.TextInput(attrs={'size':'40'}))
    postiosoite = forms.CharField(label=_(u'Postiosoite'), required=False, widget=forms.TextInput(attrs={'size':'80'}))
    postitoimipaikka = forms.CharField(label=_(u'Postitoimipaikka'), required=False, widget=forms.TextInput(attrs={'size':'80'}))
    postinumeroalue = forms.CharField(label=_(u'Postinumeroalue'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    maa_osoitteessa = forms.CharField(label=_(u'Maa osoitteessa'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    laani = forms.CharField(label=_(u'Lääni'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    puhelin_gsm_faksi = forms.CharField(label=_(u'Puhelin, kännykkä, faksi'), required=False, widget=forms.TextInput(attrs={'size':'80'}))
    email = forms.CharField(label=_(u'Sähköposti'), required=False, widget=forms.TextInput(attrs={'size':'80'}))

class HenkKokotiedotForm(forms.Form):
    # Henkilon tyyppitiedot
    syntymavuosi = forms.CharField(label=_(u'Syntymävuosi'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    mies = forms.CharField(label=_(u'Mies'), required=False, widget=forms.TextInput(attrs={'size':'1'}))
    nainen = forms.CharField(label=_(u'Nainen'), required=False, widget=forms.TextInput(attrs={'size':'1'}))
    pituustyyppi = forms.CharField(label=_(u'Pituustyyppi'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    pituus = forms.CharField(label=_(u'Pituus'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    vartalotyyppi = forms.CharField(label=_(u'Vartalotyyppi'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    paanymparys = forms.CharField(label=_(u'Päänympärys'), required=False, widget=forms.TextInput(attrs={'size':'20'})) 

class VaatKokotiedotForm(forms.Form):
    # Vaatteisiin ja jalkineiden kokotiedot
    kenkakoko = forms.CharField(label=_(u'Kenkä'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    vaatekoko = forms.CharField(label=_(u'Vaate'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    kasinekoko = forms.CharField(label=_(u'Käsinekoko'), required=False, widget=forms.TextInput(attrs={'size':'20'}))

class YritystiedotForm(forms.Form):
    # Yritykseen tiedot 
    messuavustus = forms.CharField(label=_(u'Messuavustus'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    muut_liikkeet = forms.CharField(label=_(u'Muut liikkeet'), required=False, widget=forms.TextInput(attrs={'size':'20'}))

class DataForm(forms.Form):
    # Tietosuoja
    tietosuoja_1 = forms.BooleanField(label=_(u'1 tietosuoja'), required=False)
    tietosuoja_2 = forms.BooleanField(label=_(u'2 tietosuoja'), required=False)
    tietosuoja_3 = forms.BooleanField(label=_(u'3 tietosuoja'), required=False)
    tietosuoja_4 = forms.BooleanField(label=_(u'4 tietosuoja'), required=False)
    tietosuoja_5 = forms.BooleanField(label=_(u'5 tietosuoja'), required=False)
    
    # Tietojen tallennusta koskevat tiedot
    tiedot_paivitetty = forms.CharField(label=_(u'Tiedot päivitetty'), required=False, widget=forms.TextInput(attrs={'size':'20'}))
    
class MuutForm(forms.Form):
    # Muut tiedot   
    muuta = forms.CharField(label=_(u'Muuta'), required=False, widget=forms.Textarea(attrs={'cols':'60', 'rows':'3'}))
    

