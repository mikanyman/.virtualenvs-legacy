# -*- coding: utf-8 -*-

from django.db import models
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
import datetime

ms = _(u'Ms.')
mrs = _(u'Mrs.')
mr = _(u'Mr.')
GENDER_CHOICES = ( 
    ('Ms.', ms), 
    ('Mrs.', mrs), 
    ('Mr.', mr), 
)

yes = _(u'Yes')
no = _(u'No')
YESNO_CHOICES = ( 
    ('Yes', yes), 
    ('No', no), 
)

finnish = _(u'Finnish')
english = _(u'English')
german = _(u'German')
LANGUAGE_CHOICES = ( 
    ('Finnish', finnish), 
    ('English', english),
    ('German', german), 
)

setting1 = _(u'First setting* at 6pm')
setting2 = _(u'Second setting* at 9pm')
SETTING_CHOICES = ( 
    ('setting_1', setting1), 
    ('setting_2', setting2), 
)

arrtohelsinki = _(u'to Helsinki *')
arrtotampere = _(u'to Tampere')
FLIGHTARRLOC_CHOICES = (
    ('Arrival to Helsinki', arrtohelsinki ),
    ('Arrival to Tampere', arrtotampere),
)
dummy_trans_1 = _('Arrival to Helsinki')
dummy_trans_2 = _('Arrival to Tampere')


depfromtampere = _(u'from Tampere')
depfromhelsinki = _(u'from Helsinki *')
FLIGHTDEPLOC_CHOICES = (
    ('Departure from Tampere', depfromtampere),
    ('Departure from Helsinki', depfromhelsinki),
)
dummy_trans_3 = _('Departure from Tampere')
dummy_trans_4 = _('Departure from Helsinki')

TIME_CHOICES = (
    ('', ''),
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
TIME_INPUT_FORMATS = ('%H:%M:%S', '%H:%M')

hotel1 = _(u'Other, Where?')
HOTEL_CHOICES = ( 
    ('1', 'Scandic Rosendahl'),
    ('2', 'Scandic City Tampere'),
    ('3', 'Cumulus Hämeenpuisto'),
    ('4', 'Omena Hotel Tampere 1'),
    ('5', 'Omena Hotel Tampere 2'),
    ('6', 'Hostel Sofia'),
    ('7', hotel1),
)

class Person(models.Model):
    
    # ---------- r 1:1 ----------
    lastname = models.CharField(max_length=30, blank=True, null=True)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER_CHOICES)

    # ---------- r 1:2 ----------
    address = models.CharField(max_length=50, blank=True, null=True)
    dateofbirth = models.DateField(blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
 
    # ---------- r 1:3 ----------
    postalcode = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    clubmember = models.CharField(max_length=10, blank=True, null=True, choices=YESNO_CHOICES)
   
    # ---------- r 1:4 ----------
    country = models.CharField(max_length=30, blank=True, null=True)
    whichclub = models.CharField(max_length=75, blank=True, null=True)
    
    # ---------- r 1:5 ----------
    email = models.EmailField(max_length=75, blank=True, null=True)
    membnumb = models.CharField(max_length=30, blank=True, null=True)
  
    # ---------- r 1:6 ----------
    mobilephone = models.CharField(max_length=30, blank=True, null=True)
    homephone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True, choices=LANGUAGE_CHOICES)
    
    # ---------- r 1:7 ----------
    flightarrlocation = models.CharField(max_length=30, blank=True, null=True, choices=FLIGHTARRLOC_CHOICES)
    flightdeplocation = models.CharField(max_length=30, blank=True, null=True, choices=FLIGHTDEPLOC_CHOICES)
    
    flightarrdate = models.DateField(blank=True, null=True)
    flightarrtime = models.CharField(max_length=5, blank=True, null=True, choices=TIME_CHOICES)
    flightdepdate = models.DateField(blank=True, null=True)
    flightdeptime = models.CharField(max_length=5, blank=True, null=True, choices=TIME_CHOICES)
    
    # ---------- r 1:8 ----------
    hotel = models.CharField(max_length=30, blank=True, null=True, choices=HOTEL_CHOICES)
    hotelother = models.CharField(max_length=30, blank=True, null=True)
    hotelarrdate = models.DateField(blank=True, null=True)
    hoteldepdate = models.DateField(blank=True, null=True)
    
    # ---------- r 1:9 ----------
    youngtall = models.BooleanField(default=False)
    withparents = models.CharField(max_length=10, blank=True, null=True, choices=YESNO_CHOICES)
    parentsname = models.CharField(max_length=30, blank=True, null=True)
    parentsmobile = models.CharField(max_length=30, blank=True, null=True)
    guardiansname = models.CharField(max_length=30, blank=True, null=True)
    guardiansmobile = models.CharField(max_length=30, blank=True, null=True)

    # ---------- r 1:10 ----------
    dietvegetarian = models.BooleanField(default=False)
    dietglutenfree = models.BooleanField(default=False)
    dietdiabetic = models.BooleanField(default=False)
    dietlowlactose = models.BooleanField(default=False)
    
    # ---------- r 1:11 ----------
    assistance = models.BooleanField(default=False)
    assistancespecify = models.CharField(max_length=140, blank=True, null=True)
    specialneeds = models.BooleanField(default=False)
    specialneedsspecify = models.CharField(max_length=140, blank=True, null=True)

    # ---------- r 2:1-n ----------
    prsuarrival = models.BooleanField(default=False)
    prsu1welcome = models.BooleanField(default=False)
    prsusetting = models.CharField(max_length=10, blank=True, null=True, choices=SETTING_CHOICES)
    prmonokia = models.BooleanField(default=False)
    prmotampere = models.BooleanField(default=False)
    prmo2welcome = models.BooleanField(default=False)
    prtuboard = models.BooleanField(default=False)
    prtulunch = models.BooleanField(default=False)
    prtuadvpark = models.BooleanField(default=False)
    prtuboat = models.BooleanField(default=False)
    prwehelsinki = models.BooleanField(default=False)
    prwesuomenlinna = models.BooleanField(default=False)
    prwefree = models.BooleanField(default=False)
    prthujuhannus = models.BooleanField(default=False)
    prfrisaunapis = models.BooleanField(default=False)
    prfrisaunaros = models.BooleanField(default=False)
    prsatgala = models.BooleanField(default=False)
    prsugoodbye = models.BooleanField(default=False)
    yearlyfee = models.BooleanField(default=False)
    nontallclub = models.BooleanField(default=False)
    
    # ---------- automated fields ----------
    # http://www.djangorocks.com/hints-and-tips/set-created-updated-datetime-in-your-models.html
    added = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True, auto_now=True)
    
    # ---------- hidden fields ----------
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    total = models.CharField(max_length=10, blank=True, null=True)
    
    def __unicode__(self):
        return '%s, %s' % (self.lastname, self.firstname)

    class Meta:
        ordering = ["-lastname"]
    
    #def save(self, *args, **kwargs):
    #    """ On save, update timestamps """
    #    if not self.id:
    #        self.created = datetime.datetime.today()
    #    self.modified = datetime.datetime.today()
    #    super(Person, self).save(*args, **kwargs)
 
    @models.permalink
    def get_absolute_url(self):
        """ Redirect after save """
        return ('person-detail', (), {'object_id': self.id})
        #return ('person-update', (), {'object_id': self.id})

class PersonForm(ModelForm):
    
    # ---------- r 1:1 ----------
    lastname = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}), 
        label=_(u'Last name')
        )
    firstname = forms.CharField(max_length=30, 
        label=_(u'First name')
        )
    gender = forms.CharField(max_length=10,
        widget=forms.RadioSelect(choices=GENDER_CHOICES), 
        label=_(u'Gender')
        )

    # ---------- r 1:2 ----------
    address = forms.CharField(max_length=50,
        widget=forms.TextInput(attrs={'size':'30'}), 
        label=_(u'Address')
        )
    dateofbirth = forms.DateField( 
        #input_formats = '%d.%m.%Y',
        widget=forms.TextInput(attrs={'size':'10'}), 
        label=_(u'Date of birth (yyyy-mm-dd)')
        )
    height = forms.CharField(max_length=10,
        widget=forms.TextInput(attrs={'size':'3'}), 
        label=_(u'Height')
        )

    # ---------- r 1:3 ----------
    postalcode = forms.CharField(max_length=50,
        widget=forms.TextInput(attrs={'size':'30'}), 
        label=_(u'Postcode')
        )
    city = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}), 
        label=_(u'City')
        )
    clubmember = forms.CharField(max_length=10,
        widget=forms.RadioSelect(choices=YESNO_CHOICES), 
        label=_(u'Member of a Tall Club')
        )

    # ---------- r 1:4 ----------
    country = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Country')
        )
    whichclub = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Which Tall Club are you registered with?')
        )
    
    # ---------- r 1:5 ----------
    email = forms.EmailField(
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}), 
        label=_(u'Email')
        )
    membnumb = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Membership number')
        )

    # ---------- r 1:6 ----------
    mobilephone = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Mobile phone number with country code')
        )
    homephone = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Home phone number with country code')
        )
    fax = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Fax number with country code'),
        )
    language = forms.CharField(max_length=10,
        widget=forms.RadioSelect(choices=LANGUAGE_CHOICES), 
        label=_(u'Language for welcome packets and guided tours')
        )
 
    # ---------- r 1:7 ----------
    flightarrlocation = forms.CharField(max_length=30, 
        widget=forms.RadioSelect(choices=FLIGHTARRLOC_CHOICES),
        label=_(u'Estimated arrival')
        )
    flightdeplocation = forms.CharField(max_length=30, 
        widget=forms.RadioSelect(choices=FLIGHTDEPLOC_CHOICES),
        label=_(u'Estimated departure')
        )
    flightarrdate = forms.DateField(
        widget=forms.TextInput(attrs={'size':'10', 'class': 'datepicker'}), 
        label=_(u'Estimated arrival to Helsinki*/Tampere Date (yyyy-mm-dd)')
        )
    flightarrtime = forms.CharField(
        widget=forms.Select(choices=TIME_CHOICES),
        label=_(u'Time')
        )
    flightdepdate = forms.DateField(
        widget=forms.TextInput(attrs={'size':'10', 'class': 'datepicker'}), 
        label=_(u'Estimated departure from Tampere/Helsinki* (yyyy-mm-dd)')
        )
    flightdeptime = forms.CharField(
        widget=forms.Select(choices=TIME_CHOICES), 
        label=_(u'Time')
        )

    # ---------- r 1:8 ----------
    hotel = forms.CharField(max_length=30, 
        widget=forms.RadioSelect(choices=HOTEL_CHOICES),
        label=_(u'In which hotel/hostel you are staying?')
        )
    hotelother = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'})
        )
    hotelarrdate = forms.DateField(
        widget=forms.TextInput(attrs={'size':'10', 'class': 'datepicker'}), 
        label=_(u'Check-in date (yyyy-mm-dd)')
        )
    hoteldepdate = forms.DateField(
        widget=forms.TextInput(attrs={'size':'10', 'class': 'datepicker'}), 
        label=_(u'Check-out date (yyyy-mm-dd)')
        )
    # ---------- r 1:9 ----------
    youngtall = forms.BooleanField( 
        required=False,
        widget=forms.CheckboxInput(),
        label=_(u'Young & Tall')
        )
    withparents = forms.CharField(max_length=10,
        required=False, 
        widget=forms.RadioSelect(choices=YESNO_CHOICES), 
        label=_(u'Are you travelling with your parents?')
        )    
    parentsname = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Parents name')
        )
    parentsmobile = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u'Parents mobile phone number')
        )
    guardiansname = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u"Guardians name")
        )
    guardiansmobile = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u"Guardians mobile phone number")
        )
    # ---------- r 1:10 ----------
    dietvegetarian = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(),
        label=_(u'Vegetarian')
        )
    dietglutenfree = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(),
        label=_(u'Gluten-free')
        )
    dietdiabetic = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(),
        label=_(u'Diabetic')
        )
    dietlowlactose = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(),
        label=_(u'Low lactose')
        )
    
    # ---------- r 1:11 ----------
    assistance = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(), 
        label=_(u'Do you need any personal assistance (if available) during the events?')
        )
    assistancespecify = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u"Please specify")
        )
    specialneeds = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(), 
        label=_(u'Other special needs or health risk factors the Organisation team should know?')
        )
    specialneedsspecify = forms.CharField(max_length=30,
        required=False, 
        widget=forms.TextInput(attrs={'size':'30'}),
        label=_(u"Please specify")
        )

    # ---------- SUNDAY ----------
    prsuarrival = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput()
        )
    prsu1welcome = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'27,00 €'
        )
    prsusetting = forms.CharField(max_length=10,
        required=False, 
        widget=forms.RadioSelect(choices=SETTING_CHOICES), 
        label=_(u'Choose your wish for setting time*')
        )
    
    # ---------- MONDAY ----------
    prmonokia = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'27,00 €'
        )
    prmotampere = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'27,00 €'
        )
    prmo2welcome = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'53,00 €'
        )
    
    # ---------- TUESDAY ----------
    prtuboard = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput()
        )
    prtulunch = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'8,00 €'
        )
    prtuadvpark = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(), 
        label=u''
        )
    prtuboat = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'40,00 €'
        )

    # ---------- WEDNESDAY ----------
    prwehelsinki = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'68,00 €'
        )
    prwesuomenlinna = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'17,00 €'
        )
    prwefree = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput()
        )

    # ---------- THURSDAY ----------
    prthujuhannus = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'55,00 €'
        )

    # ---------- FRIDAY ----------
    prfrisaunapis = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'37,00€'
        )
    prfrisaunaros = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput()
        )
    prsatgala = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'70,00 €'
        )
    prsugoodbye = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(), 
        label=u''
        )
    yearlyfee = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'8 €'
        )
    nontallclub = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs = {'onclick':'calculateTotal()'}), 
        label=u'20,00 €'
        )
    ip_address = forms.CharField(max_length=15,
        required=False,
        widget=forms.HiddenInput
        )
    total = forms.CharField(max_length=10,
        required=False,
        widget=forms.HiddenInput
        )

    class Meta:
        model = Person
    
    # http://stackoverflow.com/questions/2306800/django-form-validation-making-required-conditional
    """
    def clean(self):
        data = self.cleaned_data
        if data.get('foo_timestamp', None) or (data.get('foo_date', None) and data.get('foo_time', None)):
            return data
        else:
            raise forms.ValidationError('Provide either a date and time or a timestamp')
    
    def clean(self):
        data = self.cleaned_data
        if data.get('youngtall', None):
            raise forms.youngtall.ValidationError('Young & Tall Checkbox required')
        else:
            return data
    """   
    def clean(self):
        
        cleaned_data = self.cleaned_data
        
        youngtall = cleaned_data['youngtall']
        withparents = cleaned_data.get('withparents', None)
        parentsname = cleaned_data.get('parentsname', None)
        parentsmobile = cleaned_data.get('parentsmobile', None)
        guardiansname = cleaned_data.get('guardiansname', None)
        guardiansmobile = cleaned_data.get('guardiansmobile', None)
        
        # https://docs.djangoproject.com/en/1.1/ref/forms/validation/#cleaning-a-specific-field-attribute
        if youngtall:
            
            msg = _(u'This field is required.')
            #msg = str(cleaned_data) # debug

            if withparents == '':
                self._errors["withparents"] = self.error_class([msg])
                
            if withparents == 'No':
                if parentsname == '':
                    self._errors["parentsname"] = self.error_class([msg])
                if parentsmobile == '':
                    self._errors["parentsmobile"] = self.error_class([msg])
                if guardiansname == '':
                    self._errors["guardiansname"] = self.error_class([msg])
                if guardiansmobile == '':
                    self._errors["guardiansmobile"] = self.error_class([msg])

            ## These fields are no longer valid. Remove them from the cleaned data.
            #del data["youngtall"]

        # Always return the cleaned data, whether you have changed it or not.
        return cleaned_data
    
    