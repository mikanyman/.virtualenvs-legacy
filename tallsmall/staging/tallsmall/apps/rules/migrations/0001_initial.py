# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Rule'
        db.create_table('rules_rule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rule', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('rules', ['Rule'])


    def backwards(self, orm):
        
        # Deleting model 'Rule'
        db.delete_table('rules_rule')


    models = {
        'rules.rule': {
            'Meta': {'object_name': 'Rule'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rule': ('django.db.models.fields.TextField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rules']
