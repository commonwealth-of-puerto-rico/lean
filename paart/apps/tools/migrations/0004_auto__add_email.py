# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Email'
        db.create_table('tools_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('tools', ['Email'])

        # Adding M2M table for field email on 'ToolsProfile'
        db.create_table('tools_toolsprofile_email', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('toolsprofile', models.ForeignKey(orm['tools.toolsprofile'], null=False)),
            ('email', models.ForeignKey(orm['tools.email'], null=False))
        ))
        db.create_unique('tools_toolsprofile_email', ['toolsprofile_id', 'email_id'])


    def backwards(self, orm):
        # Deleting model 'Email'
        db.delete_table('tools_email')

        # Removing M2M table for field email on 'ToolsProfile'
        db.delete_table('tools_toolsprofile_email')


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
        'tools.database': {
            'Meta': {'ordering': "['label']", 'object_name': 'Database'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'tools.development': {
            'Meta': {'ordering': "['label']", 'object_name': 'Development'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'tools.email': {
            'Meta': {'ordering': "['label']", 'object_name': 'Email'},
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
            'antivirus': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tools.Antivirus']", 'null': 'True', 'blank': 'True'}),
            'backup': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tools.Backup']", 'null': 'True', 'blank': 'True'}),
            'database': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tools.Database']", 'null': 'True', 'blank': 'True'}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 5, 0, 0)'}),
            'desktops': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'development': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tools.Development']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tools.Email']", 'null': 'True', 'blank': 'True'}),
            'firewall': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tools.Firewall']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notebooks': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servers': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tools']