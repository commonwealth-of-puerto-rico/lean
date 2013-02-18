# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ToolsProfile.datetime_created'
        db.add_column('tools_toolsprofile', 'datetime_created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 18, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ToolsProfile.datetime_created'
        db.delete_column('tools_toolsprofile', 'datetime_created')


    models = {
        'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        'tools.antivirus': {
            'Meta': {'ordering': "['label']", 'object_name': 'Antivirus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'tools.backup': {
            'Meta': {'ordering': "['label']", 'object_name': 'Backup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'tools.development': {
            'Meta': {'ordering': "['label']", 'object_name': 'Development'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'tools.firewall': {
            'Meta': {'ordering': "['label']", 'object_name': 'Firewall'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'tools.toolsprofile': {
            'Meta': {'ordering': "['agency']", 'object_name': 'ToolsProfile'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'antivirus': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.Antivirus']", 'symmetrical': 'False'}),
            'backup': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.Backup']", 'symmetrical': 'False'}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {}),
            'desktops': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'development': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.Development']", 'symmetrical': 'False'}),
            'firewall': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.Firewall']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notebooks': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servers': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tools']