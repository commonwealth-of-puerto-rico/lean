# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Equipment.wifi_costs'
        db.alter_column('telecomm_equipment', 'wifi_costs', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Equipment.wifi_costs'
        raise RuntimeError("Cannot reverse this migration. 'Equipment.wifi_costs' and its values cannot be restored.")

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
            'internet_costs': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'internet_employees': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'internet_provider': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'internet_provider'", 'null': 'True', 'to': "orm['telecomm.Provider']"}),
            'intranet_connectivity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
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
        }
    }

    complete_apps = ['telecomm']