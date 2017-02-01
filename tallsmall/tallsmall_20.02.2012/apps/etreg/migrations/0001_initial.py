# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Person'
        db.create_table('etreg_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('dateofbirth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('postalcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('clubmember', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('whichclub', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('membnumb', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('mobilephone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('homephone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('etreg', ['Person'])


    def backwards(self, orm):
        
        # Deleting model 'Person'
        db.delete_table('etreg_person')


    models = {
        'etreg.person': {
            'Meta': {'ordering': "['-lastname']", 'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'clubmember': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'dateofbirth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'homephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'membnumb': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'mobilephone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'postalcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'whichclub': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['etreg']
