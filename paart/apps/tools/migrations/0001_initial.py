# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Development'
        db.create_table('tools_development', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('tools', ['Development'])

        # Adding model 'Backup'
        db.create_table('tools_backup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('tools', ['Backup'])

        # Adding model 'Firewall'
        db.create_table('tools_firewall', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('tools', ['Firewall'])

        # Adding model 'Antivirus'
        db.create_table('tools_antivirus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('tools', ['Antivirus'])

        # Adding model 'ToolsProfile'
        db.create_table('tools_toolsprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Agency'])),
            ('notebooks', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('desktops', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('servers', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('tools', ['ToolsProfile'])

        # Adding M2M table for field development on 'ToolsProfile'
        db.create_table('tools_toolsprofile_development', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('toolsprofile', models.ForeignKey(orm['tools.toolsprofile'], null=False)),
            ('development', models.ForeignKey(orm['tools.development'], null=False))
        ))
        db.create_unique('tools_toolsprofile_development', ['toolsprofile_id', 'development_id'])

        # Adding M2M table for field backup on 'ToolsProfile'
        db.create_table('tools_toolsprofile_backup', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('toolsprofile', models.ForeignKey(orm['tools.toolsprofile'], null=False)),
            ('backup', models.ForeignKey(orm['tools.backup'], null=False))
        ))
        db.create_unique('tools_toolsprofile_backup', ['toolsprofile_id', 'backup_id'])

        # Adding M2M table for field firewall on 'ToolsProfile'
        db.create_table('tools_toolsprofile_firewall', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('toolsprofile', models.ForeignKey(orm['tools.toolsprofile'], null=False)),
            ('firewall', models.ForeignKey(orm['tools.firewall'], null=False))
        ))
        db.create_unique('tools_toolsprofile_firewall', ['toolsprofile_id', 'firewall_id'])

        # Adding M2M table for field antivirus on 'ToolsProfile'
        db.create_table('tools_toolsprofile_antivirus', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('toolsprofile', models.ForeignKey(orm['tools.toolsprofile'], null=False)),
            ('antivirus', models.ForeignKey(orm['tools.antivirus'], null=False))
        ))
        db.create_unique('tools_toolsprofile_antivirus', ['toolsprofile_id', 'antivirus_id'])


    def backwards(self, orm):
        # Deleting model 'Development'
        db.delete_table('tools_development')

        # Deleting model 'Backup'
        db.delete_table('tools_backup')

        # Deleting model 'Firewall'
        db.delete_table('tools_firewall')

        # Deleting model 'Antivirus'
        db.delete_table('tools_antivirus')

        # Deleting model 'ToolsProfile'
        db.delete_table('tools_toolsprofile')

        # Removing M2M table for field development on 'ToolsProfile'
        db.delete_table('tools_toolsprofile_development')

        # Removing M2M table for field backup on 'ToolsProfile'
        db.delete_table('tools_toolsprofile_backup')

        # Removing M2M table for field firewall on 'ToolsProfile'
        db.delete_table('tools_toolsprofile_firewall')

        # Removing M2M table for field antivirus on 'ToolsProfile'
        db.delete_table('tools_toolsprofile_antivirus')


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
            'desktops': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'development': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.Development']", 'symmetrical': 'False'}),
            'firewall': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tools.Firewall']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notebooks': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servers': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tools']