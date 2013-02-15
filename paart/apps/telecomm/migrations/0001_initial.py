# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Provider'
        db.create_table('telecomm_provider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('telecomm', ['Provider'])

        # Adding model 'Equipment'
        db.create_table('telecomm_equipment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Agency'])),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('intranet_connectivity', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('internet_connectivity', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('internet_provider', self.gf('django.db.models.fields.related.ForeignKey')(related_name='internet_provider', to=orm['telecomm.Provider'])),
            ('internet_costs', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('uses_ogp_antenna', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('uses_wifi', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wifi_provider', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wifi_provider', to=orm['telecomm.Provider'])),
            ('wifi_costs', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('internet_employees', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('telecomm', ['Equipment'])


    def backwards(self, orm):
        # Deleting model 'Provider'
        db.delete_table('telecomm_provider')

        # Deleting model 'Equipment'
        db.delete_table('telecomm_equipment')


    models = {
        'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        'telecomm.equipment': {
            'Meta': {'ordering': "['label']", 'object_name': 'Equipment'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internet_connectivity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'internet_costs': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'internet_employees': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'internet_provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'internet_provider'", 'to': "orm['telecomm.Provider']"}),
            'intranet_connectivity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'uses_ogp_antenna': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uses_wifi': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wifi_costs': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'wifi_provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wifi_provider'", 'to': "orm['telecomm.Provider']"})
        },
        'telecomm.provider': {
            'Meta': {'ordering': "['label']", 'object_name': 'Provider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['telecomm']