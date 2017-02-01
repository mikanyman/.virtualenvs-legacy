# -*- coding: utf-8 -*-

from django.db import models
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

"""
    title = forms.CharField(max_length=3,
                widget=forms.Select(choices=TITLE_CHOICES))
    birth_date = forms.DateField(required=False)
    widget=forms.TextInput(attrs={'size':'40'})
    widget=forms.TextInput(attrs={'class':'special'})
"""

GENDER_CHOICES = ( 
    ('Ms.', 'Ms.'), 
    ('Mrs.', 'Mrs.'), 
    ('Mr.', 'Mr.'), 
)
YESNO_CHOICES = ( 
    ('Yes', 'Yes'), 
    ('No', 'No'), 
)

language1 = _(u'Finnish')
language2 = _(u'English')
language3 = _(u'German')

LANGUAGE_CHOICES = ( 
    ('Finnish', language1), 
    ('English', language2),
    ('German', language3), 
)
TIME_CHOICES = ( 
    ('00:00', '00:00'),
    ('01:00', '01:00'),
    ('02:00', '02:00'),
    ('03:00', '03:00'),
    ('04:00', '04:00'),
    ('05:00', '05:00'),
    ('06:00', '06:00'),
    ('07:00', '07:00'),
    ('08:00', '08:00'),
    ('09:00', '09:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
    ('22:00', '22:00'),
    ('23:00', '23:00'),
)

hotel1 = _(u'Other, Where?')

HOTEL_CHOICES = ( 
    ('Scandic Rosendahl', 'Scandic Rosendahl'),
    ('Scandic City Tampere', 'Scandic City Tampere'),
    ('Cumulus Hämeenpuisto', 'Cumulus Hämeenpuisto'),
    ('Omena Hotel Tampere 1', 'Omena Hotel Tampere 1'),
    ('Omena Hotel Tampere 2', 'Omena Hotel Tampere 2'),
    ('Hostel Sofia', 'Hostel Sofia'),
    ('Other, Where?', hotel1),
)

diet1 = _(u'Vegetarian')
diet2 = _(u'Gluten-free')
diet3 = _(u'Diabetic')
diet4 = _(u'Low lactose')

DIET_CHOICES = {
    ('Vegetarian', diet1),
    ('Gluten-free', diet2),
    ('Diabetic', diet3),
    ('Low lactose', diet4), 
}

class Person(models.Model):
    
    # ---------- r 1:1 ----------
    lastname = models.CharField(max_length=30, blank=True, null=True)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=4, blank=True, null=True, choices=GENDER_CHOICES)
    
    # ---------- r 1:2 ----------
    address = models.CharField(max_length=50, blank=True, null=True)
    dateofbirth = models.DateField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    
    # ---------- r 1:3 ----------
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    clubmember = models.CharField(max_length=3, blank=True, null=True, choices=YESNO_CHOICES)
    
    # ---------- r 1:4 ----------
    country = models.CharField(max_length=30, blank=True, null=True)
    whichclub = models.CharField(max_length=30, blank=True, null=True)
    
    # ---------- r 1:5 ----------
    email = models.EmailField(max_length=75, blank=True, null=True)
    membnumb = models.CharField(max_length=30, blank=True, null=True)
    
    # ---------- r 1:6 ----------
    mobilephone = models.CharField(max_length=30, blank=True, null=True)
    homephone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True, choices=LANGUAGE_CHOICES)
    
    # ---------- r 1:7 ----------
    flightarrdate = models.DateField(blank=True, null=True)
    flightarrtime = models.TimeField(blank=True, null=True, choices=TIME_CHOICES)
    flightdepdate = models.DateField(blank=True, null=True)
    flightdeptime = models.TimeField(blank=True, null=True, choices=TIME_CHOICES)
    
    # ---------- r 1:8 ----------
    hotel = models.CharField(max_length=30, blank=True, null=True, choices=HOTEL_CHOICES)
    hotelother = models.CharField(max_length=30, blank=True, null=True)
    hotelarrdate = models.DateField(blank=True, null=True)
    hoteldepdate = models.DateField(blank=True, null=True)

    # ---------- r 1:9 ----------
    youngtall = models.NullBooleanField()
    withparents = models.CharField(max_length=3, blank=True, null=True, choices=YESNO_CHOICES)
    parentsname = models.CharField(max_length=30, blank=True, null=True)
    parentsmobile = models.CharField(max_length=30, blank=True, null=True)
    guardiansname = models.CharField(max_length=30, blank=True, null=True)
    gurardiansmobile = models.CharField(max_length=30, blank=True, null=True)
    
    # ---------- r 1:10 ----------
    diet = models.CharField(max_length=30, blank=True, null=True, choices=DIET_CHOICES)
    
    # ---------- r 1:11 ----------
    assistance = models.NullBooleanField()
    assistancespecify = models.CharField(max_length=140, blank=True, null=True)
    specialneeds = models.NullBooleanField()
    specialneedsspecify = models.CharField(max_length=140, blank=True, null=True)
    
    
    # ---------- r 2:1 ----------
    test1 = models.NullBooleanField()
    test2 = models.NullBooleanField()

    #specialneedsdescr
    #prsuarrival
    #prsu1welcome
    #prsusetting
    #prmonokia
    #prmotampere
    #prmo2welcome
    #prtuboard
    #prtulunch
    #prtuadvpark
    #prtuboat
    #prwehelsinki
    #prwesuomenlinna
    #prwefree
    #prthujuhannus
    #prfrisaunapis
    #prfrisaunaros
    #prsatgala
    #prsugoodbye
    #yearlyfee
    #nontallclub
    #total
    
    def __unicode__(self):
        return '%s, %s' % (self.lastname, self.firstname)

    class Meta:
        ordering = ["-lastname"]
 
    @models.permalink
    def get_absolute_url(self):
        return ('person-detail', (), {'object_id': self.id})
 
class PersonForm(ModelForm):
    
    # ---------- r 1:1 ----------
    lastname = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}), 
        label=_(u'Last name')
        )
    firstname = forms.CharField(max_length=10, 
        label=_(u'First name')
        )
    gender = forms.CharField(max_length=4,
        widget=forms.RadioSelect(choices=GENDER_CHOICES), 
        label=_(u'Gender')
        )
    
    # ---------- r 1:2 ----------
    address = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}), 
        label=_(u'Address')
        )
    dateofbirth = forms.DateField( 
        #input_formats = '%d.%m.%Y',
        widget=forms.TextInput(attrs={'size':'10'}), 
        label=_('Date of birth (yyyy-mm-dd)')
        )
    height = forms.CharField(max_length=50,
        widget=forms.TextInput(attrs={'size':'4'}), 
        label=_(u'Height')
        )
    
    # ---------- r 1:3 ----------
    postalcode = forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={'size':'10'}), 
        label='Postcode'
        )
    city = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'20'}), 
        label='City'
        )
    clubmember = forms.CharField(max_length=3,
        widget=forms.RadioSelect(choices=YESNO_CHOICES), 
        label=_(u'Member of a Tall Club')
        )
    
    # ---------- r 1:4 ----------
    country = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Country')
        )
    whichclub = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Which Tall Club are you registered with?')
        )
    
    # ---------- r 1:5 ----------
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'size':'30'}), 
        label=_('Email')
        )
    membnumb = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_('Membership number')
        )
    
    # ---------- r 1:6 ----------
    mobilephone = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_('Mobile phone number with country code')
        )
    homephone = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_('Home phone number with country code')
        )
    fax = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_('Fax number with country code'),
        )
    language = forms.CharField(max_length=10,
        widget=forms.CheckboxSelectMultiple(choices=LANGUAGE_CHOICES),
        label=_('Which language(s) do you speak?')
        )
    
    # ---------- r 1:7 ----------
    flightarrdate = forms.DateField(
        widget=forms.TextInput(attrs={'size':'10', 'class': 'datepicker'}), 
        label=_('Estimated arrival to Helsinki*/Tampere Date (yyyy-mm-dd)')
        )
    flightarrtime = forms.TimeField(
        widget=forms.Select(choices=TIME_CHOICES),
        label=_('Time')
        )
    flightdepdate = forms.DateField(
        widget=forms.TextInput(attrs={'size':'10', 'class': 'datepicker'}), 
        label=_('Estimated departure from Tampere/Helsinki* (yyyy-mm-dd)')
        )
    flightdeptime = forms.TimeField(
        widget=forms.Select(choices=TIME_CHOICES), 
        label=_('Time')
        )
    
    # ---------- r 1:8 ----------
    hotelarrdate = forms.DateField(
        widget=forms.TextInput(attrs={'size':'16', 'class': 'datepicker'}), 
        label=_('Arr. /Date')
        )
    hoteldepdate = forms.DateField(
        widget=forms.TextInput(attrs={'size':'16', 'class': 'datepicker'}), 
        label=_('Dep. /Date')
        )
    hotel = forms.CharField(max_length=10,
        widget=forms.RadioSelect(choices=HOTEL_CHOICES),
        label=_('In which hotel/hostel you are staying?')
        )
    hotelother = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'})
        )
    hotelarrdate = forms.DateField(
        widget=forms.TextInput(attrs={'size':'10', 'class': 'datepicker'}), 
        label=_('Check-in date (yyyy-mm-dd)')
        )
    hoteldepdate = forms.DateField(
        widget=forms.TextInput(attrs={'size':'10', 'class': 'datepicker'}), 
        label=_('Check-out date (yyyy-mm-dd)')
        )

    # ---------- r 1:9 ----------
    youngtall = forms.NullBooleanField(
        widget=forms.CheckboxInput(), 
        label=_('Young & Tall')
        )
    withparents = forms.CharField(max_length=3,
        widget=forms.RadioSelect(choices=YESNO_CHOICES), 
        label=_(u'Are you travelling with your parents?')
        )
    parentsname = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Parents name')
        )
    parentsmobile = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Parents mobile phone number')
        )
    guardiansname = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u"Guardians name")
        )
    gurardiansmobile = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u"Guardians mobile phone number")
        )
    
    # ---------- r 1:10 ----------
    diet = forms.CharField(max_length=10,
        widget=forms.CheckboxSelectMultiple(choices=DIET_CHOICES),
        label=_('Diet')
        )
    
    # ---------- r 1:11 ----------
    assistance = forms.NullBooleanField(
        widget=forms.CheckboxInput(), 
        label=_('Do you need any personal assistance (if available) during the events?')
        )
    assistancespecify = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u"Please specify")
        )
    specialneeds = forms.NullBooleanField(
        widget=forms.CheckboxInput(), 
        label=_('Other special needs or health risk factors the Organisation team should know?')
        )
    specialneedsspecify = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u"Please specify")
        )


    # ---------- r 2:1 ----------
    test1 = forms.NullBooleanField(
        widget=forms.CheckboxInput(), 
        label=_('Test 1')
        )
    test2 = forms.NullBooleanField(
        widget=forms.CheckboxInput(), 
        label=_('Test 2')
        )

        
    class Meta:
        model = Person
        
