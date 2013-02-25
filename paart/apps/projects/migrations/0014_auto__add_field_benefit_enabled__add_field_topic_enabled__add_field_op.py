# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Benefit.enabled'
        db.add_column('projects_benefit', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Topic.enabled'
        db.add_column('projects_topic', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Opportunity.enabled'
        db.add_column('projects_opportunity', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Stage.enabled'
        db.add_column('projects_stage', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Classification.enabled'
        db.add_column('projects_classification', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Purpose.enabled'
        db.add_column('projects_purpose', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Benefit.enabled'
        db.delete_column('projects_benefit', 'enabled')

        # Deleting field 'Topic.enabled'
        db.delete_column('projects_topic', 'enabled')

        # Deleting field 'Opportunity.enabled'
        db.delete_column('projects_opportunity', 'enabled')

        # Deleting field 'Stage.enabled'
        db.delete_column('projects_stage', 'enabled')

        # Deleting field 'Classification.enabled'
        db.delete_column('projects_classification', 'enabled')

        # Deleting field 'Purpose.enabled'
        db.delete_column('projects_purpose', 'enabled')


    models = {
        'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'director': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'physical_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'postal_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        'projects.benefit': {
            'Meta': {'ordering': "['label']", 'object_name': 'Benefit'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.classification': {
            'Meta': {'ordering': "['label']", 'object_name': 'Classification'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.project': {
            'Meta': {'ordering': "['label']", 'object_name': 'Project'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.projectbudget': {
            'Meta': {'object_name': 'ProjectBudget'},
            'benefits': ('django.db.models.fields.TextField', [], {}),
            'director': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infrastructure': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'limitations': ('django.db.models.fields.TextField', [], {}),
            'presumptions': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Project']", 'unique': 'True'}),
            'requirements': ('django.db.models.fields.TextField', [], {}),
            'risks': ('django.db.models.fields.TextField', [], {})
        },
        'projects.projectdetails': {
            'Meta': {'object_name': 'ProjectDetails'},
            'benefit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Benefit']"}),
            'benefit_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'end_period': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'end_period'", 'to': "orm['projects.FiscalYear']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Project']", 'unique': 'True'}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Stage']"}),
            'start_period': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'start_period'", 'to': "orm['projects.FiscalYear']"}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Topic']"}),
            'topic_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        'projects.projectfile': {
            'Meta': {'object_name': 'ProjectFile'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"})
        },
        'projects.projectinfo': {
            'Meta': {'object_name': 'ProjectInfo'},
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Classification']"}),
            'classification_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'expected_results': ('django.db.models.fields.TextField', [], {}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fiscal_year'", 'to': "orm['projects.FiscalYear']"}),
            'goals': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'methodology': ('django.db.models.fields.TextField', [], {}),
            'milestones': ('django.db.models.fields.TextField', [], {}),
            'needs': ('django.db.models.fields.TextField', [], {}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Project']", 'unique': 'True'}),
            'purpose': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Purpose']"}),
            'purpose_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'sponsor': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'projects.projectopportunities': {
            'Meta': {'object_name': 'ProjectOpportunities'},
            'explanation': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opportunity': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.Opportunity']", 'symmetrical': 'False'}),
            'other_agencies': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Project']", 'unique': 'True'}),
            'sharing_benefit': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sharing_benefit'", 'symmetrical': 'False', 'to': "orm['projects.Benefit']"})
        },
        'projects.purpose': {
            'Meta': {'ordering': "['label']", 'object_name': 'Purpose'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'projects.stage': {
            'Meta': {'ordering': "['label']", 'object_name': 'Stage'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'projects.topic': {
            'Meta': {'ordering': "['label']", 'object_name': 'Topic'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['projects']