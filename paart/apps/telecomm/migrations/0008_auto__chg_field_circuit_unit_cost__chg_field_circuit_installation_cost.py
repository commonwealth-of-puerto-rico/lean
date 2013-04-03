# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Circuit.unit_cost'
        db.alter_column('telecomm_circuit', 'unit_cost', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Circuit.installation_cost'
        db.alter_column('telecomm_circuit', 'installation_cost', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Circuit.unit_cost'
        raise RuntimeError("Cannot reverse this migration. 'Circuit.unit_cost' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Circuit.installation_cost'
        raise RuntimeError("Cannot reverse this migration. 'Circuit.installation_cost' and its values cannot be restored.")

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
            'contract_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'contract_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 3, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installation_cost': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'circuit_provider'", 'to': "orm['telecomm.Provider']"}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'technology': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'circuit_technology'", 'to': "orm['telecomm.Technology']"}),
            'unit_cost': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'units': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'telecomm.equipment': {
            'Meta': {'ordering': "['label']", 'unique_together': "(['agency', 'label'],)", 'object_name': 'Equipment'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 3, 0, 0)'}),
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