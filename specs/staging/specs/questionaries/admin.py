# -*- coding: utf-8 -*-
from django.contrib import admin
from specs.questionaries.models import Questionary, Fieldtype, Question

"""
class Questionary(models.Model):
    title = models.CharField(max_length=200, verbose_name=_(u'Kysymys'))
    intro = models.TextField(verbose_name=_(u'Johdando'))
    note = models.TextField(verbose_name=_(u'Ohjeet'))
    pub_date = models.DateTimeField(verbose_name=_(u'Julkaisupäivämäärä'))

class Fieldtype(models.Model):
    label = models.CharField(max_length=20, verbose_name=_(u'Kenttätyyppi'))

class Question(models.Model):
    questionary = models.ForeignKey(Questionary, verbose_name=_(u'Kysely'))
    question = models.TextField(max_length=200, verbose_name=_(u'Kysymys'))
    fieldtype = models.ForeignKey(Fieldtype, verbose_name=_(u'Kenttätyyppi'))
    textarea_content = models.TextField(verbose_name=_(u'Tekstisisältö'))
    order = models.IntegerField(verbose_name=_(u'Järjestys'))
"""

class QuestionaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    fieldsets = [
        (u'Kyselyn määritykset', {'fields': ['title', 'intro', 'note', 'pub_date']}),
    ]
    
class FieldtypeAdmin(admin.ModelAdmin):
    list_display = ('label',)
    fieldsets = [
        (u'Kenttätyyppi', {'fields': ['label']}),
    ]
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'fieldtype', 'order')
    fieldsets = [
        (u'Kysymyksen määritykset', {'fields': ['question', 'fieldtype', 'order']}),
    ]
    
admin.site.register(Questionary, QuestionaryAdmin)
admin.site.register(Fieldtype, FieldtypeAdmin)
admin.site.register(Question, QuestionAdmin)