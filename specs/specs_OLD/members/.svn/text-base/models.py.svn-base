# -*- coding: utf-8 -*-
# specs/members/models.py

import datetime

from django.db import models, connection
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

""" Signals """
from django.db.models.signals import post_save


class ProjectionManager(models.Manager):
        
    def select_dates(self, object_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.object_created
            FROM members_member m
            WHERE id=%s""" % object_id) 
        row = cursor.fetchone()
        result_dict = {}
        result_dict['object_created'] = row[0]
        return result_dict
    
    def select_tunnistetiedot(self, object_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.sukunimi, m.etunimi, m.arvo, m.ent_sukunimi
            FROM members_member m
            WHERE id=%s""" % object_id) 
        row = cursor.fetchone()
        result_dict = {}
        result_dict['sukunimi'] = row[0]
        result_dict['etunimi'] = row[1]
        result_dict['arvo'] = row[2]
        result_dict['ent_sukunimi'] = row[3]
        return result_dict
    
    def select_jasentiedot(self, object_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.jasennumero, m.liittymisvuosi, m.eroaminen, m.varsinainen, m.perhe, m.kannatus, m.kunnia, m.yri, m.uudet_jasenet, m.tila
            FROM members_member m
            WHERE id=%s""" % object_id) 
        row = cursor.fetchone()
        result_dict = {}
        result_dict['jasennumero'] = row[0]
        result_dict['liittymisvuosi'] = row[1]
        result_dict['eroaminen'] = row[2]
        result_dict['varsinainen'] = row[3]
        result_dict['perhe'] = row[4]
        result_dict['kannatus'] = row[5]
        result_dict['kunnia'] = row[6]
        result_dict['yri'] = row[7]
        result_dict['uudet_jasenet'] = row[8]
        result_dict['tila'] = row[9]
        return result_dict

    def select_yhteystiedot(self, object_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.yritys, m.postiosoite, m.postitoimipaikka, m.postinumeroalue, m.maa_osoitteessa, m.laani, m.puhelin_gsm_faksi, m.email
            FROM members_member m
            WHERE id=%s""" % object_id) 
        row = cursor.fetchone()
        result_dict = {}
        result_dict['yritys'] = row[0]
        result_dict['postiosoite'] = row[1]
        result_dict['postitoimipaikka'] = row[2]
        result_dict['postinumeroalue'] = row[3]
        result_dict['maa_osoitteessa'] = row[4]
        result_dict['laani'] = row[5]
        result_dict['puhelin_gsm_faksi'] = row[6]
        result_dict['email'] = row[7]
        return result_dict
        
    def select_henkkokotiedot(self, object_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.syntymavuosi, m.mies, m.nainen, m.pituustyyppi, m.pituus, m.vartalotyyppi, m.paanymparys
            FROM members_member m
            WHERE id=%s""" % object_id) 
        row = cursor.fetchone()
        result_dict = {}
        result_dict['syntymavuosi'] = row[0]
        result_dict['mies'] = row[1]
        result_dict['nainen'] = row[2]
        result_dict['pituustyyppi'] = row[3]
        result_dict['pituus'] = row[4]
        result_dict['vartalotyyppi'] = row[5]
        result_dict['paanymparys'] = row[6]
        return result_dict
        
    def select_vaatkokotiedot(self, object_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.kenkakoko, m.vaatekoko, m.kasinekoko
            FROM members_member m
            WHERE id=%s""" % object_id) 
        row = cursor.fetchone()
        result_dict = {}
        result_dict['kenkakoko'] = row[0]
        result_dict['vaatekoko'] = row[1]
        result_dict['kasinekoko'] = row[2]
        return result_dict
    
    def select_yritystiedot(self, object_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.messuavustus, m.muut_liikkeet
            FROM members_member m
            WHERE id=%s""" % object_id) 
        row = cursor.fetchone()
        result_dict = {}
        result_dict['messuavustus'] = row[0]
        result_dict['muut_liikkeet'] = row[1]
        return result_dict
    
    def select_datatiedot(self, object_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.tietosuoja_1, m.tietosuoja_2, m.tietosuoja_3, m.tietosuoja_4, m.tietosuoja_5, m.tiedot_paivitetty
            FROM members_member m
            WHERE id=%s""" % object_id) 
        row = cursor.fetchone()
        result_dict = {}
        result_dict['tietosuoja_1'] = row[0]
        result_dict['tietosuoja_2'] = row[1]
        result_dict['tietosuoja_3'] = row[2]
        result_dict['tietosuoja_4'] = row[3]
        result_dict['tietosuoja_5'] = row[4]
        result_dict['tiedot_paivitetty'] = row[5]
        return result_dict
        
    def select_muuttiedot(self, object_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT m.muuta
            FROM members_member m
            WHERE id=%s""" % object_id) 
        row = cursor.fetchone()
        result_dict = {}
        result_dict['muuta'] = row[0]
        return result_dict


class Test(models.Model):
    user = models.ForeignKey(User, unique=True)
    object_created = models.DateTimeField(auto_now_add=True, editable=False)
    yri = models.NullBooleanField(blank=True, null=True, default=False, verbose_name=_(u'Yritys'))

class Applicant(models.Model):
    
    APPLICATION_STATUS = (
        (1, u'Uusi hakemus'),
        (2, u'Lomake lähetetty'),
        (3, u'Jäsenmaksu maksettu'),
        (4, u'Siirretty jäsenrekisteriin'),
    )
    
    status = models.IntegerField(blank=False, null=False, \
        choices=APPLICATION_STATUS, verbose_name='Tila', default=1)
    tililla = models.DateField(blank=True, null=True, verbose_name="Maksu saapunut")
    pid = models.CharField(max_length=30, blank=True, null=True, editable=False)
    etunimi = models.CharField(max_length=40, verbose_name=u'Etunimi')
    sukunimi = models.CharField(max_length=40, verbose_name=u'Sukunimi')
    katuosoite = models.CharField(max_length=40, verbose_name=u'Katuosoite')
    postinumero = models.CharField(max_length=5, verbose_name=u'Postinumero')
    postitoimipaikka = models.CharField(max_length=40, verbose_name=u'Postitoimip')
    puhelin = models.CharField(max_length=40, verbose_name=u'Puhelin')
    email = models.EmailField(max_length=40, blank=True, null=True, verbose_name=u'Sähköposti')
    syntymaaika = models.CharField(max_length=10, verbose_name=u'Syntymäaika')
    perheenjasenet = models.TextField(blank=True, null=True, verbose_name=u'Perheenjäsenet')
    lisatietoja = models.TextField(blank=True, null=True, verbose_name=u'Lisätietoja')
    parentId = models.IntegerField(blank=True, null=True, editable=False)
    created = models.DateTimeField(blank=True, null=True, editable=False, verbose_name=u'Päivämäärä')
    modified = models.DateTimeField(blank=True, null=True, editable=False)

    def __unicode__(self):
        return u'%s, %s' % (self.sukunimi, self.etunimi)

    # http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        super(Applicant, self).save(*args, **kwargs)
                
    def get_absolute_url(self):
        return '../update/%i/' % (self.id,)
    
    class Meta:
        ordering = ('sukunimi', 'etunimi')
        verbose_name = _(u'Jäsenyttä hakeva henkilö')
        verbose_name_plural = _(u'Jäsenyyttä hakevat henkilöt')
        

class Member(models.Model):
    
    STATUS_OPTIONS = (
        ('act', 'Aktiivinen'),
        ('pass', 'Passiivinen'),
        ('trash', 'Poistettu'),
    )

    JASENTYYPPI_CHOICES = (
        ('Varsinainen', 'Varsinainen'),
        ('Perhe', 'Perhe'),
        ('Kannatus', 'Kannatus'),
        ('Kunnia', 'Kunnia'),
        ('Uusi', 'Uusi'),
    )
    
    # profile -- requires import from django.contrib.auth.models import User
    user = models.ForeignKey(User, blank=True, null=True, unique=True)
    
    object_created = models.DateTimeField(auto_now_add=True, editable=False)
    jasennumero = models.CharField(max_length=6, blank=True, null=True, verbose_name=_(u'Jäsennumero'))
    
    jasentyyppi = models.CharField(max_length=20, blank=True, null=True, choices=JASENTYYPPI_CHOICES, verbose_name=_(u'Jäsentyyppi'))
    
    varsinainen = models.NullBooleanField(blank=True, null=True, verbose_name=_(u'Varsinainen'))
    perhe = models.NullBooleanField(blank=True, null=True, verbose_name=_(u'Perhe'))
    kannatus = models.NullBooleanField(blank=True, null=True, verbose_name=_(u'Kannatus'))
    kunnia = models.NullBooleanField(blank=True, null=True, verbose_name=_(u'Kunnia'))
    
    yri = models.NullBooleanField(blank=True, null=True, default=False, verbose_name=_(u'Yritys'))
    uudet_jasenet = models.NullBooleanField(blank=True, null=True, verbose_name=_(u'Uusi'))
    liittymisvuosi = models.CharField(max_length=30, blank=True, null=True, verbose_name=_(u'Liittymisvuosi'))
    eroaminen = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Eroaminen'))
    sukunimi = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u'Sukunimi'))
    etunimi = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Etunimi'))
    ent_sukunimi = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u'Entinen sukunimi'))
    arvo = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u'Arvo'))
    yritys = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u'Yritys'))
    postiosoite = models.CharField(max_length=80, blank=True, null=True, verbose_name=_(u'Postiosoite'))
    postitoimipaikka = models.CharField(max_length=80, blank=True, null=True, verbose_name=_(u'Postitoimipaikka'))
    postinumeroalue = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Postinumeroalue'))
    maa_osoitteessa = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Maa osoitteessa'))
    laani = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Lääni'))
    puhelin_gsm_faksi = models.CharField(max_length=100, blank=True, null=True, verbose_name=_(u'Puhelin, kännykkä, faksi'))
    email = models.CharField(max_length=80, blank=True, null=True, verbose_name=_(u'Sähköposti'))
    mies = models.CharField(max_length=1, blank=True, null=True, verbose_name=_(u'Mies'))
    nainen = models.CharField(max_length=1, blank=True, null=True, verbose_name=_(u'Nainen'))
    pituustyyppi = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Pituus'))
    syntymavuosi = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Syntymävuosi'))
    pituus = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Pituus'))
    kenkakoko = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Kenkä'))
    vaatekoko = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Vaate'))
    vartalotyyppi = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Vartalotyyppi'))
    paanymparys = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Päänympärys'))
    kasinekoko = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Käsinekoko'))
    tietosuoja_1 = models.NullBooleanField(blank=True, null=True, verbose_name=_(u'1 tietosuoja'))
    tietosuoja_2 = models.NullBooleanField(blank=True, null=True, verbose_name=_(u'2 tietosuoja'))
    tietosuoja_3 = models.NullBooleanField(blank=True, null=True, verbose_name=_(u'3 tietosuoja'))
    tietosuoja_4 = models.NullBooleanField(blank=True, null=True, verbose_name=_(u'4 tietosuoja'))
    tietosuoja_5 = models.NullBooleanField(blank=True, null=True, verbose_name=_(u'5 tietosuoja'))
    muuta = models.TextField(blank=True, null=True, verbose_name=_(u'Muuta'))
    tiedot_paivitetty = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Tiedot päivitetty'))
    messuavustus = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Messuavustus'))
    muut_liikkeet = models.TextField(blank=True, null=True, verbose_name=_(u'Muut liikkeet'))
    tila = models.CharField(max_length=20, blank=True, null=True, default='act', choices=STATUS_OPTIONS, verbose_name=_(u'Tila'))
    
    objects = ProjectionManager()

    def __unicode__(self):
        return u'%s, %s - %s' % (self.sukunimi, self.etunimi, self.jasennumero)

    # http://docs.djangoproject.com/en/dev/ref/contrib/admin/ "colored_name"
    def alle_30(self):
        today = datetime.date.today()
        this_year = today.strftime("%Y")
        ty = int(this_year)
        
        birth_year = self.syntymavuosi
        if birth_year.isdigit():
            by = int(birth_year)
            diff = ty - by
            if diff < 30:
                return diff
            else:
                return ''
        else:
            return ''
    
    def latest_payment(self):
        events = Event.objects.filter(member=self.id)
        payment_list = []
        latest_payment = ''
        for event in events:
            payment_list.append(event.tapahtumakohde_vuosi)
            if len(payment_list) > 1:
                latest_payment = max(payment_list)
            else:
                latest_payment = payment_list[0]
        return latest_payment

    class Meta:
        ordering = ('sukunimi', 'etunimi', 'jasennumero')
        verbose_name = _(u'Jäsen')
        verbose_name_plural = _(u'Jäsenet')
        
class Event(models.Model):
    
    TAPAHTUMATYYPPI_CHOICES = (
        ('jasenmaksu', 'Jäsenmaksu'),
    )
    TAPAHTUMAKOHDEVUOSI_CHOICES = (
        ('2005', '2005'),
        ('2006', '2006'),
        ('2007', '2007'),
        ('2008', '2008'),
        ('2009', '2009'),
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
    )
    tapahtuma_tyyppi = models.CharField(max_length=20, blank=True, null=True, choices=TAPAHTUMATYYPPI_CHOICES, default='jasenmaksu', verbose_name=_(u'Tapahtumatyyppi'))
    tapahtuma_aika = models.DateField(blank=True, null=True, verbose_name=_(u'Päivämäärä, jolloin maksettu'))
    tapahtumakohde_vuosi = models.CharField(max_length=4, blank=True, null=True, choices=TAPAHTUMAKOHDEVUOSI_CHOICES, verbose_name=_(u'Vuosi jota maksu koskee'))
    created = models.DateTimeField(auto_now=True, verbose_name='Luotu')
    member = models.ForeignKey('Member')
    
    def __unicode__(self):
        return u'%s' % (self.member)
    
    class Meta:
        ordering = ('-tapahtuma_aika',)
        verbose_name = _(u'tapahtuma')
        verbose_name_plural = _(u'Tapahtumat')
        
        
class Yritys(models.Model):
    
    STATUS_OPTIONS = (
        ('act', 'Aktiivinen'),
        ('pass', 'Passiivinen'),
        ('trash', 'Poistettu'),
    )

    JASENTYYPPI_CHOICES = (
        ('Varsinainen', 'Varsinainen'),
        ('Perhe', 'Perhe'),
        ('Kannatus', 'Kannatus'),
        ('Kunnia', 'Kunnia'),
        ('Uusi', 'Uusi'),
    )
    
    # profile -- requires import from django.contrib.auth.models import User
    user = models.ForeignKey(User, blank=True, null=True, unique=True)
    object_created = models.CharField(max_length=100, blank=True, null=True)
    jasennumero = models.CharField(max_length=6, blank=True, null=True, verbose_name=_(u'Jäsennumero'))
    jasentyyppi = models.CharField(max_length=20, blank=True, null=True, choices=JASENTYYPPI_CHOICES, verbose_name=_(u'Jäsentyyppi'))

    varsinainen = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'Varsinainen'))
    perhe = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'Perhe'))
    kannatus = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'Kannatus'))
    kunnia = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'Kunnia'))
    yri = models.CharField(max_length=10, blank=True, null=True, default=False, verbose_name=_(u'Yritys'))
    uudet_jasenet = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'Uusi'))
    
    liittymisvuosi = models.CharField(max_length=30, blank=True, null=True, verbose_name=_(u'Liittymisvuosi'))
    eroaminen = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Eroaminen'))
    sukunimi = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u'Sukunimi'))
    etunimi = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Etunimi'))
    ent_sukunimi = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u'Entinen sukunimi'))
    arvo = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u'Arvo'))
    yritys = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u'Yritys'))
    postiosoite = models.CharField(max_length=80, blank=True, null=True, verbose_name=_(u'Postiosoite'))
    postitoimipaikka = models.CharField(max_length=80, blank=True, null=True, verbose_name=_(u'Postitoimipaikka'))
    postinumeroalue = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Postinumeroalue'))
    maa_osoitteessa = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Maa osoitteessa'))
    laani = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Lääni'))
    puhelin_gsm_faksi = models.CharField(max_length=100, blank=True, null=True, verbose_name=_(u'Puhelin, kännykkä, faksi'))
    email = models.CharField(max_length=80, blank=True, null=True, verbose_name=_(u'Sähköposti'))
    mies = models.CharField(max_length=1, blank=True, null=True, verbose_name=_(u'Mies'))
    nainen = models.CharField(max_length=1, blank=True, null=True, verbose_name=_(u'Nainen'))
    pituustyyppi = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Pituus'))
    syntymavuosi = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Syntymävuosi'))
    pituus = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Pituus'))
    kenkakoko = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Kenkä'))
    vaatekoko = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Vaate'))
    vartalotyyppi = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Vartalotyyppi'))
    paanymparys = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Päänympärys'))
    kasinekoko = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Käsinekoko'))
    
    tietosuoja_1 = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'1 tietosuoja'))
    tietosuoja_2 = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'2 tietosuoja'))
    tietosuoja_3 = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'3 tietosuoja'))
    tietosuoja_4 = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'4 tietosuoja'))
    tietosuoja_5 = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'5 tietosuoja'))
    
    muuta = models.TextField(blank=True, null=True, verbose_name=_(u'Muuta'))
    tiedot_paivitetty = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Tiedot päivitetty'))
    messuavustus = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Messuavustus'))
    muut_liikkeet = models.TextField(blank=True, null=True, verbose_name=_(u'Muut liikkeet'))
    tila = models.CharField(max_length=20, blank=True, null=True, default='act', choices=STATUS_OPTIONS, verbose_name=_(u'Tila'))
    
    objects = ProjectionManager()

    def __unicode__(self):
        return u'%s, %s - %s' % (self.sukunimi, self.etunimi, self.jasennumero)
    
    def latest_payment(self):
        events = Event.objects.filter(member=self.id)
        payment_list = []
        latest_payment = ''
        for event in events:
            payment_list.append(event.tapahtumakohde_vuosi)
            if len(payment_list) > 1:
                latest_payment = max(payment_list)
            else:
                latest_payment = payment_list[0]
        return latest_payment

    class Meta:
        ordering = ('sukunimi', 'etunimi', 'jasennumero')
        verbose_name = _(u'Yritys')
        verbose_name_plural = _(u'Yritykset')
        
class YritysEvent(models.Model):
    
    TAPAHTUMATYYPPI_CHOICES = (
        ('jasenmaksu', 'Jäsenmaksu'),
    )
    TAPAHTUMAKOHDEVUOSI_CHOICES = (
        ('2005', '2005'),
        ('2006', '2006'),
        ('2007', '2007'),
        ('2008', '2008'),
        ('2009', '2009'),
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
    )
    tapahtuma_tyyppi = models.CharField(max_length=20, blank=True, null=True, choices=TAPAHTUMATYYPPI_CHOICES, default='jasenmaksu', verbose_name=_(u'Tapahtumatyyppi'))
    tapahtuma_aika = models.DateField(blank=True, null=True, verbose_name=_(u'Päivämäärä, jolloin maksettu'))
    tapahtumakohde_vuosi = models.CharField(max_length=4, blank=True, null=True, choices=TAPAHTUMAKOHDEVUOSI_CHOICES, verbose_name=_(u'Vuosi jota maksu koskee'))
    created = models.DateTimeField(auto_now=True, verbose_name='Luotu')
    member = models.ForeignKey('Yritys')
    
    def __unicode__(self):
        return u'%s' % (self.member)
    
    class Meta:
        ordering = ('-tapahtuma_aika',)
        verbose_name = _(u'tapahtuma')
        verbose_name_plural = _(u'Tapahtumat')
        

""" Signal Handlers """
def update_pid_at_post_save(sender, **kwargs):
    """ initialize persistent id-field after save """

    instance = kwargs['instance']
    created = kwargs['created']
    provenience = 'pikry'
    version = '_1_' 
    
    if created:
        instance.pid = '%s%s%s' % (provenience, version, instance.id)
        instance.save()

""" Registration of signals """
post_save.connect(update_pid_at_post_save, sender=Applicant)

