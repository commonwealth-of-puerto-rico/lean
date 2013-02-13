# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FiscalYear'
        db.create_table('projects_fiscalyear', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('projects', ['FiscalYear'])

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

        # Adding model 'Stage'
        db.create_table('projects_stage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('projects', ['Stage'])

        # Adding model 'Benefit'
        db.create_table('projects_benefit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('projects', ['Benefit'])

        # Adding model 'Topic'
        db.create_table('projects_topic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('projects', ['Topic'])

        # Adding model 'Opportunity'
        db.create_table('projects_opportunity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('projects', ['Opportunity'])

        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Agency'])),
            ('fiscal_year', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('purpose', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Purpose'])),
            ('purpose_other', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Classification'])),
            ('classification_other', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
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
            ('presumptions', self.gf('django.db.models.fields.TextField')()),
            ('limitations', self.gf('django.db.models.fields.TextField')()),
            ('risks', self.gf('django.db.models.fields.TextField')()),
            ('benefits', self.gf('django.db.models.fields.TextField')()),
            ('director', self.gf('django.db.models.fields.TextField')()),
            ('start_period', self.gf('django.db.models.fields.related.ForeignKey')(related_name='start_period', to=orm['projects.FiscalYear'])),
            ('end_period', self.gf('django.db.models.fields.related.ForeignKey')(related_name='end_period', to=orm['projects.FiscalYear'])),
            ('stage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Stage'])),
            ('benefit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Benefit'])),
            ('benefit_other', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Topic'])),
            ('topic_other', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
            ('other_agencies', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('projects', ['Project'])

        # Adding M2M table for field opportunity on 'Project'
        db.create_table('projects_project_opportunity', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('opportunity', models.ForeignKey(orm['projects.opportunity'], null=False))
        ))
        db.create_unique('projects_project_opportunity', ['project_id', 'opportunity_id'])

        # Adding M2M table for field sharing_benefit on 'Project'
        db.create_table('projects_project_sharing_benefit', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('benefit', models.ForeignKey(orm['projects.benefit'], null=False))
        ))
        db.create_unique('projects_project_sharing_benefit', ['project_id', 'benefit_id'])


    def backwards(self, orm):
        # Deleting model 'FiscalYear'
        db.delete_table('projects_fiscalyear')

        # Deleting model 'Purpose'
        db.delete_table('projects_purpose')

        # Deleting model 'Classification'
        db.delete_table('projects_classification')

        # Deleting model 'Stage'
        db.delete_table('projects_stage')

        # Deleting model 'Benefit'
        db.delete_table('projects_benefit')

        # Deleting model 'Topic'
        db.delete_table('projects_topic')

        # Deleting model 'Opportunity'
        db.delete_table('projects_opportunity')

        # Deleting model 'Project'
        db.delete_table('projects_project')

        # Removing M2M table for field opportunity on 'Project'
        db.delete_table('projects_project_opportunity')

        # Removing M2M table for field sharing_benefit on 'Project'
        db.delete_table('projects_project_sharing_benefit')


    models = {
        'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        'projects.benefit': {
            'Meta': {'ordering': "['label']", 'object_name': 'Benefit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.classification': {
            'Meta': {'ordering': "['label']", 'object_name': 'Classification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.fiscalyear': {
            'Meta': {'ordering': "['label']", 'object_name': 'FiscalYear'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'projects.opportunity': {
            'Meta': {'ordering': "['label']", 'object_name': 'Opportunity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.project': {
            'Meta': {'ordering': "['label']", 'object_name': 'Project'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'benefit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Benefit']"}),
            'benefit_other': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'benefits': ('django.db.models.fields.TextField', [], {}),
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Classification']"}),
            'classification_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'director': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'end_period': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'end_period'", 'to': "orm['projects.FiscalYear']"}),
            'expected_results': ('django.db.models.fields.TextField', [], {}),
            'explanation': ('django.db.models.fields.TextField', [], {}),
            'fiscal_year': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'goals': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infrastructure': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'limitations': ('django.db.models.fields.TextField', [], {}),
            'methodology': ('django.db.models.fields.TextField', [], {}),
            'milestones': ('django.db.models.fields.TextField', [], {}),
            'needs': ('django.db.models.fields.TextField', [], {}),
            'opportunity': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.Opportunity']", 'symmetrical': 'False'}),
            'other_agencies': ('django.db.models.fields.TextField', [], {}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'presumptions': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'purpose': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Purpose']"}),
            'purpose_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'requirements': ('django.db.models.fields.TextField', [], {}),
            'risks': ('django.db.models.fields.TextField', [], {}),
            'sharing_benefit': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sharing_benefit'", 'symmetrical': 'False', 'to': "orm['projects.Benefit']"}),
            'sponsor': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Stage']"}),
            'start_period': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'start_period'", 'to': "orm['projects.FiscalYear']"}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Topic']"}),
            'topic_other': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'projects.purpose': {
            'Meta': {'ordering': "['label']", 'object_name': 'Purpose'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.stage': {
            'Meta': {'ordering': "['label']", 'object_name': 'Stage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'projects.topic': {
            'Meta': {'ordering': "['label']", 'object_name': 'Topic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['projects']