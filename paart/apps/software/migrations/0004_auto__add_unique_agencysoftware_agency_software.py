# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'AgencySoftware', fields ['agency', 'software']
        db.create_unique('software_agencysoftware', ['agency_id', 'software_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'AgencySoftware', fields ['agency', 'software']
        db.delete_unique('software_agencysoftware', ['agency_id', 'software_id'])


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
        'software.agencysoftware': {
            'Meta': {'ordering': "['software']", 'unique_together': "(['agency', 'software'],)", 'object_name': 'AgencySoftware'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'software': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['software.Software']"})
        },
        'software.software': {
            'Meta': {'ordering': "['software_type', 'label']", 'object_name': 'Software'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'software_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['software.SoftwareType']"})
        },
        'software.softwaretype': {
            'Meta': {'ordering': "['label']", 'object_name': 'SoftwareType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['software']