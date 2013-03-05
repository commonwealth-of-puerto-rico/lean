# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Equipment', fields ['label']
        db.delete_unique('telecomm_equipment', ['label'])


        # Changing field 'Equipment.internet_costs'
        db.alter_column('telecomm_equipment', 'internet_costs', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))
        # Adding unique constraint on 'Equipment', fields ['agency', 'label']
        db.create_unique('telecomm_equipment', ['agency_id', 'label'])


    def backwards(self, orm):
        # Removing unique constraint on 'Equipment', fields ['agency', 'label']
        db.delete_unique('telecomm_equipment', ['agency_id', 'label'])

        # Adding unique constraint on 'Equipment', fields ['label']
        db.create_unique('telecomm_equipment', ['label'])


        # User chose to not deal with backwards NULL issues for 'Equipment.internet_costs'
        raise RuntimeError("Cannot reverse this migration. 'Equipment.internet_costs' and its values cannot be restored.")

    models = {
        'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'director': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'physical_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'postal_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        'telecomm.equipment': {
            'Meta': {'ordering': "['label']", 'unique_together': "(['agency', 'label'],)", 'object_name': 'Equipment'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 5, 0, 0)'}),
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
        }
    }

    complete_apps = ['telecomm']