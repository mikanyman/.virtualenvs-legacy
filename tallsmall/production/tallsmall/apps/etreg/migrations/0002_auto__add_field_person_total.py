# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Person.total'
        db.add_column('etreg_person', 'total', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Person.total'
        db.delete_column('etreg_person', 'total')


    models = {
        'etreg.person': {
            'Meta': {'ordering': "['-lastname']", 'object_name': 'Person'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'assistance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'assistancespecify': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'clubmember': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'dateofbirth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dietdiabetic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dietglutenfree': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dietlowlactose': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dietvegetarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'flightarrdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'flightarrlocation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'flightarrtime': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'flightdepdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'flightdeplocation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'flightdeptime': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'guardiansmobile': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'guardiansname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'homephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'hotelarrdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hoteldepdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hotelother': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'membnumb': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'mobilephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'nontallclub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parentsmobile': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'parentsname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'postalcode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'prfrisaunapis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prfrisaunaros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prmo2welcome': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prmonokia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prmotampere': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prsatgala': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prsu1welcome': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prsuarrival': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prsugoodbye': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prsusetting': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'prthujuhannus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prtuadvpark': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prtuboard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prtuboat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prtulunch': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prwefree': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prwehelsinki': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prwesuomenlinna': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'specialneeds': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'specialneedsspecify': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'whichclub': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'withparents': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'yearlyfee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'youngtall': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['etreg']
