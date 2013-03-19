# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Technology'
        db.create_table('telecomm_technology', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('telecomm', ['Technology'])

        # Adding model 'Circuit'
        db.create_table('telecomm_circuit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 19, 0, 0))),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Agency'])),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('technology', self.gf('django.db.models.fields.related.ForeignKey')(related_name='circuit_technology', to=orm['telecomm.Technology'])),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(related_name='circuit_provider', to=orm['telecomm.Provider'])),
            ('bandwidth', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=128, null=True, blank=True)),
            ('cost', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('installation_cost', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('telecomm', ['Circuit'])


    def backwards(self, orm):
        # Deleting model 'Technology'
        db.delete_table('telecomm_technology')

        # Deleting model 'Circuit'
        db.delete_table('telecomm_circuit')


    models = {
        'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'director': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'physical_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'postal_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prifas': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'telecomm.circuit': {
            'Meta': {'ordering': "['purpose']", 'object_name': 'Circuit'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'bandwidth': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 19, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installation_cost': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'circuit_provider'", 'to': "orm['telecomm.Provider']"}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'technology': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'circuit_technology'", 'to': "orm['telecomm.Technology']"})
        },
        'telecomm.equipment': {
            'Meta': {'ordering': "['label']", 'unique_together': "(['agency', 'label'],)", 'object_name': 'Equipment'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 19, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internet_connectivity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'internet_costs': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'internet_employees': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'internet_provider': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'internet_provider'", 'null': 'True', 'to': "orm['telecomm.Provider']"}),
            'intranet_connectivity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'uses_ogp_antenna': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uses_wifi': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wifi_costs': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wifi_provider': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'wifi_provider'", 'null': 'True', 'to': "orm['telecomm.Provider']"})
        },
        'telecomm.provider': {
            'Meta': {'ordering': "['label']", 'object_name': 'Provider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'telecomm.technology': {
            'Meta': {'ordering': "['label']", 'object_name': 'Technology'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['telecomm']