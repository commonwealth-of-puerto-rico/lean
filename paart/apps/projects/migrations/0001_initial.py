# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Purpose'
        db.create_table('projects_purpose', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('projects', ['Purpose'])

        # Adding model 'Classification'
        db.create_table('projects_classification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('projects', ['Classification'])

        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Agency'])),
            ('fiscal_year', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('purpose', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Purpose'])),
            ('purpose_other', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Classification'])),
            ('classification_other', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('sponsor', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('goals', self.gf('django.db.models.fields.TextField')()),
            ('needs', self.gf('django.db.models.fields.TextField')()),
            ('expected_results', self.gf('django.db.models.fields.TextField')()),
            ('methodology', self.gf('django.db.models.fields.TextField')()),
            ('milestones', self.gf('django.db.models.fields.TextField')()),
            ('infrastructure', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('requirements', self.gf('django.db.models.fields.TextField')()),
            ('limitations', self.gf('django.db.models.fields.TextField')()),
            ('risks', self.gf('django.db.models.fields.TextField')()),
            ('benefits', self.gf('django.db.models.fields.TextField')()),
            ('director', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('projects', ['Project'])

        # Adding model 'Detail'
        db.create_table('projects_detail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
        ))
        db.send_create_signal('projects', ['Detail'])


    def backwards(self, orm):
        # Deleting model 'Purpose'
        db.delete_table('projects_purpose')

        # Deleting model 'Classification'
        db.delete_table('projects_classification')

        # Deleting model 'Project'
        db.delete_table('projects_project')

        # Deleting model 'Detail'
        db.delete_table('projects_detail')


    models = {
        'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        'projects.classification': {
            'Meta': {'ordering': "['label']", 'object_name': 'Classification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.detail': {
            'Meta': {'ordering': "['project']", 'object_name': 'Detail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"})
        },
        'projects.project': {
            'Meta': {'ordering': "['label']", 'object_name': 'Project'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'benefits': ('django.db.models.fields.TextField', [], {}),
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Classification']"}),
            'classification_other': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'director': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'expected_results': ('django.db.models.fields.TextField', [], {}),
            'fiscal_year': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'goals': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infrastructure': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'limitations': ('django.db.models.fields.TextField', [], {}),
            'methodology': ('django.db.models.fields.TextField', [], {}),
            'milestones': ('django.db.models.fields.TextField', [], {}),
            'needs': ('django.db.models.fields.TextField', [], {}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'purpose': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Purpose']"}),
            'purpose_other': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'requirements': ('django.db.models.fields.TextField', [], {}),
            'risks': ('django.db.models.fields.TextField', [], {}),
            'sponsor': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'projects.purpose': {
            'Meta': {'ordering': "['label']", 'object_name': 'Purpose'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['projects']