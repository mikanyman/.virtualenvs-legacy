# -*- coding: utf-8 -*-

# specs/choe/models.py

from django.db import models
from django import forms
from django.contrib import admin
#from django.newforms import ModelForm

# radio
SUKUPUOLI_CHOICES = (
    ('1', 'Nainen'),
    ('2', 'Mies'),
)
# radio
IKARYHMA_CHOICES = (
    ('1', 'alle 10'),
    ('2', '10-19'),
    ('3', '20-35'),
    ('4', 'yli 35'),
)
#radio
KENKAKOKO_CHOICES = (
    ('32', '32'),
    ('33', '33'),
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),
    ('39', '39'),
    ('40', '40'),
    ('41', '41'),
    ('42', '42'),
    ('43', '43'),
    ('44', '44'),
    ('45', '45'),
    ('46', '46'),
    ('47', '47'),
    ('48', '48'),
    ('49', '49'),
    ('50', '50'),
    ('51', '51'),
    ('52', '52'),
    ('53', '53'),
    ('54', '54'),
    ('55', '55'),
    ('56', '56'),
    ('57', '57'),
    ('58', '58'),
    ('59', '59'),
    ('60', '60'),
)
# radio
JALKAKIPUJA_CHOICES = (
    ('1', 'ei'),
    ('2', 'harvoin, satunnaisesti'),
    ('3', 'toistuvasti, silloin tällöin'),
    ('4', 'jatkuvasti, lähes päivittäin'),
)
MISSA_JALKAKIP_CHOICES = (
    ('1', 'jalkaterä'),
    ('2', 'nilkka'),
    ('3', 'sääri'),
    ('4', 'polvi'),
    ('5', 'reisi'),
    ('6', 'lonkka'),
)
# radio
KIPUASTEIKKO_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)
ASIANTUNTIJA_CHOICES = (
    ('1', 'kyllä'),
    ('2', 'ei'),
)
TUKIPOHJALLINEN_SUOS_CHOICES = (
    ('1', 'kyllä'),
    ('2', 'ei'),
)
TUKIPOHJALLINEN_KAYT_CHOICES = (
    ('1', 'kyllä'),
    ('2', 'ei'),
)
MUUTOS_CHOICES = (
    ('1', 'kyllä'),
    ('2', 'ei'),
)
class Entry(models.Model):
    #username = models.CharField(max_length=100, blank=True, null=True)
    #email = models.EmailField(blank=True, null=True)
    #content = models.TextField(blank=True, null=True)
    first_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)
    ip_address = models.IPAddressField(blank=True, null=True, editable=False)

    ### Mitattajan yhteystiedot
    mt_sukunimi = models.CharField(max_length=40, blank=True, null=True)
    mt_etunimi = models.CharField(max_length=40, blank=True, null=True)
    mt_puhelinnumero = models.CharField(max_length=40, blank=True, null=True)
    mt_email = models.CharField(max_length=40, blank=True, null=True)

    ### Mitattavan yhteystiedot
    mv_sukunimi = models.CharField(max_length=40, blank=True, null=True)
    mv_etunimi = models.CharField(max_length=40, blank=True, null=True)
    mv_katuosoite = models.CharField(max_length=40, blank=True, null=True)
    mv_postinumero = models.CharField(max_length=5, blank=True, null=True)
    mv_postitoimipaikka = models.CharField(max_length=40, blank=True, null=True)
    mv_puhelinnumero = models.CharField(max_length=40, blank=True, null=True)
    mv_email = models.CharField(max_length=40, blank=True, null=True)
    
    ### Henkilotiedot
    sukupuoli = models.CharField(max_length=1, blank=True, null=True)
    ikaryhma = models.CharField(max_length=1, blank=True, null=True)
    kenkakoko = models.CharField(max_length=1, blank=True, null=True)

    ### Mittatiedot
    vartalon_pituus = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rinnan_ymparys = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vyotaron_ymparys = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    lantion_ymparys = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    jalan_sivupituus = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    saaren_takapituus = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pohkeen_ymparys = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nilkan_ymparys = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    jalkapohjan_pituus = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pakian_ymparys = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    jalkama = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    ### Jalkojen terveyteen liittyvia ongelmia
    jalkakipuja = models.CharField(max_length=1, blank=True, null=True)
    missa_jalkakipuja = models.NullBooleanField(blank=True, null=True)
    kipuasteikko = models.CharField(max_length=1, blank=True, null=True)
    asiantuntija = models.NullBooleanField(blank=True, null=True)
    tukipohjallinen_suositeltu = models.CharField(max_length=1, blank=True, null=True)
    tukipohjallinen_kaytossa = models.CharField(max_length=1, blank=True, null=True)
    
    asentovirhe = models.NullBooleanField(blank=True, null=True)
    kovettumia = models.NullBooleanField(blank=True, null=True)
    vaivasenluu = models.NullBooleanField(blank=True, null=True)    

    pitk_laskeuma = models.NullBooleanField(blank=True, null=True)
    poik_laskeuma = models.NullBooleanField(blank=True, null=True)
    vasaravarpaat = models.NullBooleanField(blank=True, null=True)
    
    muuta_vaivaa = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % self.sukunimi
    class Meta:
        ordering = ('-id',)
    class Admin:
        list_display = ('sukunimi',)

class EntryForm(forms.Form):

    #username = forms.CharField(label='Nimi', widget=forms.TextInput(
    #    attrs={'size':'40'}))
    #email = forms.EmailField(label='Sahkoposti', widget=forms.TextInput(
    #    attrs={'size':'40'}), required=False, help_text='&nbsp;&nbsp;(Ei nayteta viestissa)')
    #content = forms.CharField(label='Viesti', widget=forms.Textarea(
    #    attrs={'cols':'60', 'rows':'10'}))

     ### Mitattaaajan yhteystiedot
    sukunimi = forms.CharField(label='Sukunimi', widget=forms.TextInput(
        attrs={'size':'53'}))
    etunimi = forms.CharField(label='Etunimi', widget=forms.TextInput(
        attrs={'size':'20'}))
    puhelinnumero = forms.CharField(label='Puhelin', widget=forms.TextInput(
        attrs={'size':'20'}))
    email = forms.CharField(label='Sähköposti', widget=forms.TextInput(
        attrs={'size':'53'}))

     ### Mitattavan yhteystiedot
    sukunimi = forms.CharField(label='Sukunimi', widget=forms.TextInput(
        attrs={'size':'53'}))
    etunimi = forms.CharField(label='Etunimi', widget=forms.TextInput(
        attrs={'size':'20'}))
    katuosoite = forms.CharField(label='Osoite', widget=forms.TextInput(
        attrs={'size':'20'}))
    postinumero = forms.CharField(label='Postinro ja ', widget=forms.TextInput(
        attrs={'size':'5', 'max_length':'5'}))
    postitoimipaikka = forms.CharField(label='-toimipaikka', widget=forms.TextInput(
        attrs={'size':'34'}))
    puhelinnumero = forms.CharField(label='Puhelin', widget=forms.TextInput(
        attrs={'size':'20'}))
    email = forms.CharField(label='Sähköposti', widget=forms.TextInput(
        attrs={'size':'53'}))

    ### Henkilotiedot
    sukupuoli = forms.ChoiceField(label='Sukupuoli', widget=forms.RadioSelect(), 
        choices=SUKUPUOLI_CHOICES)
    ikaryhma = forms.ChoiceField(label='Ikäryhmä', widget=forms.RadioSelect(),
        choices=IKARYHMA_CHOICES)
    kenkakoko = forms.ChoiceField(label='Kenkäkoko', widget=forms.RadioSelect(),
        choices=KENKAKOKO_CHOICES)

    ### Mittatiedot
    vartalon_pituus = forms.DecimalField(label='Vartalon pituus', widget=forms.TextInput(
        attrs={'size':'3', 'max_length':'3'}), help_text='Mitataan ilman jalkineita, pituus esim. 148,5 cm')
    rinnan_ymparys = forms.DecimalField(label='Rinnan ympärys', widget=forms.TextInput(
        attrs={'size':'3', 'max_length':'3'}), help_text='Rinnan korkein kohta')
    vyotaron_ymparys = forms.DecimalField(label='Vyötärön ympärys', widget=forms.TextInput(
        attrs={'size':'3', 'max_length':'3'}), help_text='Ohuin kohta tai housun vyötärön linja')
    lantion_ymparys = forms.DecimalField(label='Lantion ympärys', widget=forms.TextInput(
        attrs={'size':'3', 'max_length':'3'}), help_text='Levein kohta')
    jalan_sivupituus = forms.DecimalField(label='Jalan sivupituus', widget=forms.TextInput(
        attrs={'size':'3', 'max_length':'3'}), help_text='Vyötäröltä maahan lonkkaluun yläpuolelta')
    saaren_takapituus = forms.DecimalField(label='Säären pituus', widget=forms.TextInput(
        attrs={'size':'3', 'max_length':'2'}), help_text='Takaa polvitaipeesta maahan')
    pohkeen_ymparys = forms.DecimalField(label='Pohkeen ympärys', widget=forms.TextInput(
        attrs={'size':'3', 'max_length':'2'}), help_text='Levein kohta')
    nilkan_ymparys = forms.DecimalField(label='Nilkan ympärys', widget=forms.TextInput(
        attrs={'size':'3', 'max_length':'2'}), help_text='Nilkkaluun yläpuolelta')
    jalkapohjan_pituus = forms.DecimalField(label='Jalkapohjan pituus', widget=forms.TextInput(
        attrs={'size':'3', 'max_length':'2'}), help_text='Piirrä jalkakuva. Mittaa varpaista kantapäähän')
    pakian_ymparys = forms.DecimalField(label='Päkiän ympärys', widget=forms.TextInput(
        attrs={'size':'3', 'max_length':'2'}), help_text='Levein kohta')
    jalkama = forms.DecimalField(label='Jalkama/rintavuus', widget=forms.TextInput(
        attrs={'size':'3', 'max_length':'2'}), help_text='Jalkapöydän ympärys viistosti kantaluun takaa nilkan ja jalkaterän yhtymäkohtaan')

    ### Jalkojen terveyteen liittyvia ongelmia
    jalkakipuja = forms.ChoiceField(label='Jalkakipuja 5 ed. vuoden aikana', widget=forms.RadioSelect(),
        choices=JALKAKIPUJA_CHOICES)
    missa_jalkakipuja = forms.ChoiceField(label='Missä kipuja on esiintynyt?', widget=forms.CheckboxSelectMultiple(),
        choices=MISSA_JALKAKIP_CHOICES)
    kipuasteikko = forms.ChoiceField(label='Kipu asteikolla 1=lievä, 10=erittäin voimakas', widget=forms.RadioSelect(),
        choices=KIPUASTEIKKO_CHOICES)
    asiantuntija = forms.ChoiceField(label='Onko asiantuntija, esim. jalkaterapeutti tai kouluterveydenhoitaja tutkinut jalkojen kuntoa', widget=forms.RadioSelect(),
        choices=ASIANTUNTIJA_CHOICES)
    tukipohjallinen_suositeltu = forms.ChoiceField(label='Onko suositeltu tukipohjallista', widget=forms.RadioSelect(),
        choices=TUKIPOHJALLINEN_SUOS_CHOICES)
    tukipohjallinen_kaytossa = forms.ChoiceField(label='Tukipohjallinen käytössä', widget=forms.RadioSelect(),
        choices=TUKIPOHJALLINEN_SUOS_CHOICES)
    asentovirhe = forms.ChoiceField(label='Asentovirhe', widget=forms.RadioSelect(),
        choices=MUUTOS_CHOICES)
    kovettumia = forms.ChoiceField(label='Kovettumia', widget=forms.RadioSelect(),
        choices=MUUTOS_CHOICES)
    vaivasenluu = forms.ChoiceField(label='Vaivasenlu', widget=forms.RadioSelect(),
        choices=MUUTOS_CHOICES)
    pitk_laskeuma = forms.ChoiceField(label='Pitkittäiskaaren laskeuma', widget=forms.RadioSelect(),
        choices=MUUTOS_CHOICES)
    poik_laskeuma = forms.ChoiceField(label='Poikittaiskaaren laskeuma', widget=forms.RadioSelect(),
        choices=MUUTOS_CHOICES)
    vasaravarpaat = forms.ChoiceField(label='Vasaravarpaat', widget=forms.RadioSelect(),
        choices=MUUTOS_CHOICES)

    muuta_vaivaa = forms.CharField(label='Muuta vaivaa', widget=forms.Textarea(
        attrs={'cols':'82', 'rows':'3'}))

admin.site.register(Entry)





