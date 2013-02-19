# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ProjectDetails'
        db.delete_table('projects_projectdetails')

        # Removing M2M table for field opportunity on 'ProjectDetails'
        db.delete_table('projects_projectdetails_opportunity')

        # Removing M2M table for field sharing_benefit on 'ProjectDetails'
        db.delete_table('projects_projectdetails_sharing_benefit')

        # Adding model 'ProjectBudget'
        db.create_table('projects_projectbudget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.Project'], unique=True)),
            ('infrastructure', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('requirements', self.gf('django.db.models.fields.TextField')()),
            ('presumptions', self.gf('django.db.models.fields.TextField')()),
            ('limitations', self.gf('django.db.models.fields.TextField')()),
            ('risks', self.gf('django.db.models.fields.TextField')()),
            ('benefits', self.gf('django.db.models.fields.TextField')()),
            ('director', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('projects', ['ProjectBudget'])

        # Adding model 'ProjectInfo'
        db.create_table('projects_projectinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.Project'], unique=True)),
            ('fiscal_year', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fiscal_year', to=orm['projects.FiscalYear'])),
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
        ))
        db.send_create_signal('projects', ['ProjectInfo'])


    def backwards(self, orm):
        # Adding model 'ProjectDetails'
        db.create_table('projects_projectdetails', (
            ('limitations', self.gf('django.db.models.fields.TextField')()),
            ('other_agencies', self.gf('django.db.models.fields.TextField')()),
            ('infrastructure', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Topic'])),
            ('classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Classification'])),
            ('presumptions', self.gf('django.db.models.fields.TextField')()),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
            ('start_period', self.gf('django.db.models.fields.related.ForeignKey')(related_name='start_period', to=orm['projects.FiscalYear'])),
            ('fiscal_year', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fiscal_year', to=orm['projects.FiscalYear'])),
            ('director', self.gf('django.db.models.fields.TextField')()),
            ('milestones', self.gf('django.db.models.fields.TextField')()),
            ('goals', self.gf('django.db.models.fields.TextField')()),
            ('requirements', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Stage'])),
            ('purpose_other', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('project', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.Project'], unique=True)),
            ('needs', self.gf('django.db.models.fields.TextField')()),
            ('classification_other', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('benefits', self.gf('django.db.models.fields.TextField')()),
            ('purpose', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Purpose'])),
            ('methodology', self.gf('django.db.models.fields.TextField')()),
            ('topic_other', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('benefit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Benefit'])),
            ('sponsor', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('risks', self.gf('django.db.models.fields.TextField')()),
            ('end_period', self.gf('django.db.models.fields.related.ForeignKey')(related_name='end_period', to=orm['projects.FiscalYear'])),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('benefit_other', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('expected_results', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('projects', ['ProjectDetails'])

        # Adding M2M table for field opportunity on 'ProjectDetails'
        db.create_table('projects_projectdetails_opportunity', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectdetails', models.ForeignKey(orm['projects.projectdetails'], null=False)),
            ('opportunity', models.ForeignKey(orm['projects.opportunity'], null=False))
        ))
        db.create_unique('projects_projectdetails_opportunity', ['projectdetails_id', 'opportunity_id'])

        # Adding M2M table for field sharing_benefit on 'ProjectDetails'
        db.create_table('projects_projectdetails_sharing_benefit', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectdetails', models.ForeignKey(orm['projects.projectdetails'], null=False)),
            ('benefit', models.ForeignKey(orm['projects.benefit'], null=False))
        ))
        db.create_unique('projects_projectdetails_sharing_benefit', ['projectdetails_id', 'benefit_id'])

        # Deleting model 'ProjectBudget'
        db.delete_table('projects_projectbudget')

        # Deleting model 'ProjectInfo'
        db.delete_table('projects_projectinfo')


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
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 18, 0, 0)'}),
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