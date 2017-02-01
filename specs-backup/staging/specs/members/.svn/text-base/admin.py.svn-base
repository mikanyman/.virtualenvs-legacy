# -*- coding: UTF-8 -*-
from time import strftime

from django.contrib import admin
from specs.members.models import Member, Event, Yritys, YritysEvent, Applicant

class ApplicantAdmin(admin.ModelAdmin):
    list_display = (
        'sukunimi', 'etunimi', 'hakemus_saapunut', 'status', 'maksu_saapunut'
    )
    # http://groups.google.com/group/django-users/browse_thread/thread/7efc9893df381412/c41557a1f400d35a
    def hakemus_saapunut(self, obj):
        if obj.created is None:
            return u'---'
        else:
            # http://seehuhn.de/pages/pdate
            return obj.created.strftime("%d.%m.%Y") #  %H:%M
    def maksu_saapunut(self, obj):
        if obj.tililla is None:
            return u'---'
        else:
            return obj.tililla.strftime("%d.%m.%Y")

class EventInline(admin.TabularInline):
    model = Event
    extra = 1
    
class YritysEventInline(admin.TabularInline):
    model = YritysEvent
    extra = 1

class MemberAdmin(admin.ModelAdmin):
    list_per_page = 1000
    list_display = (
        'jasennumero', 'sukunimi', 'etunimi', 'postiosoite','postitoimipaikka', 'jasentyyppi', 'tila', 'alle_30'
    )
    list_filter = (
        'varsinainen','perhe','kannatus','kunnia','uudet_jasenet','yri','tila'
    )
    fieldsets = [
        (u'Jäsenyystiedot', {'fields': ['jasennumero', 'sukunimi', 'etunimi', 'jasentyyppi' ]}),
        (u'Kokotiedot', {'fields': ['liittymisvuosi', 'eroaminen', 'ent_sukunimi', 'arvo', 'yritys', 'postiosoite', 'postitoimipaikka', 'postinumeroalue', 'maa_osoitteessa', 'laani', 'puhelin_gsm_faksi', 'email', 'mies', 'nainen', 'pituustyyppi', 'syntymavuosi', 'pituus', 'kenkakoko', 'vaatekoko', 'vartalotyyppi', 'paanymparys', 'kasinekoko', 'tietosuoja_1', 'tietosuoja_2', 'tietosuoja_3', 'tietosuoja_4', 'tietosuoja_5', 'tiedot_paivitetty', 'messuavustus', 'muut_liikkeet', 'tila'], 'classes': ['collapse']}),
        (u'Muuta', {'fields': ['muuta'], 'classes': ['collapse']}),
    ]
    inlines = [EventInline]
    search_fields = ['sukunimi', 'jasennumero']
    
class YritysAdmin(admin.ModelAdmin):
    list_per_page = 1000
    list_display = (
        'jasennumero', 'yritys','postiosoite','postitoimipaikka', 'jasentyyppi'
    )
    list_filter = (
        'varsinainen','perhe','kannatus','kunnia','uudet_jasenet','yri'
    )
    fieldsets = [
        (u'Jäsenyystiedot', {'fields': ['jasennumero', 'yritys' ]}),
        (u'Kokotiedot', {'fields': ['liittymisvuosi', 'eroaminen', 'ent_sukunimi', 'arvo', 'postiosoite', 'postitoimipaikka', 'postinumeroalue', 'maa_osoitteessa', 'laani', 'puhelin_gsm_faksi', 'email', 'mies', 'nainen', 'pituustyyppi', 'syntymavuosi', 'pituus', 'kenkakoko', 'vaatekoko', 'vartalotyyppi', 'paanymparys', 'kasinekoko', 'tietosuoja_1', 'tietosuoja_2', 'tietosuoja_3', 'tietosuoja_4', 'tietosuoja_5', 'tiedot_paivitetty', 'messuavustus', 'muut_liikkeet', 'tila'], 'classes': ['collapse']}),
        (u'Muuta', {'fields': ['muuta'], 'classes': ['collapse']}),
    ]
    inlines = [YritysEventInline]
    search_fields = ['sukunimi', 'jasennumero']
    
class EventAdmin(admin.ModelAdmin):
    list_display = ('member', 'created', 'tapahtuma_tyyppi', 'tapahtuma_aika', 'tapahtumakohde_vuosi')
    
class YritysEventAdmin(admin.ModelAdmin):
    list_display = ('member', 'created', 'tapahtuma_tyyppi', 'tapahtuma_aika', 'tapahtumakohde_vuosi')

class YritysEventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Member, MemberAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Yritys, YritysAdmin)
admin.site.register(YritysEvent, YritysEventAdmin)
admin.site.register(Applicant, ApplicantAdmin)