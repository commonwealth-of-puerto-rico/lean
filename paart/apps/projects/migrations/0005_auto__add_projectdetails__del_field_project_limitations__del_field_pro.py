# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectDetails'
        db.create_table('projects_projectdetails', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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
            ('benefit_other', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('priority', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Topic'])),
            ('topic_other', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
            ('other_agencies', self.gf('django.db.models.fields.TextField')()),
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

        # Deleting field 'Project.limitations'
        db.delete_column('projects_project', 'limitations')

        # Deleting field 'Project.other_agencies'
        db.delete_column('projects_project', 'other_agencies')

        # Deleting field 'Project.infrastructure'
        db.delete_column('projects_project', 'infrastructure')

        # Deleting field 'Project.classification'
        db.delete_column('projects_project', 'classification_id')

        # Deleting field 'Project.presumptions'
        db.delete_column('projects_project', 'presumptions')

        # Deleting field 'Project.start_period'
        db.delete_column('projects_project', 'start_period_id')

        # Deleting field 'Project.explanation'
        db.delete_column('projects_project', 'explanation')

        # Deleting field 'Project.fiscal_year'
        db.delete_column('projects_project', 'fiscal_year_id')

        # Deleting field 'Project.director'
        db.delete_column('projects_project', 'director')

        # Deleting field 'Project.milestones'
        db.delete_column('projects_project', 'milestones')

        # Deleting field 'Project.goals'
        db.delete_column('projects_project', 'goals')

        # Deleting field 'Project.requirements'
        db.delete_column('projects_project', 'requirements')

        # Deleting field 'Project.stage'
        db.delete_column('projects_project', 'stage_id')

        # Deleting field 'Project.purpose_other'
        db.delete_column('projects_project', 'purpose_other')

        # Deleting field 'Project.topic'
        db.delete_column('projects_project', 'topic_id')

        # Deleting field 'Project.needs'
        db.delete_column('projects_project', 'needs')

        # Deleting field 'Project.classification_other'
        db.delete_column('projects_project', 'classification_other')

        # Deleting field 'Project.benefits'
        db.delete_column('projects_project', 'benefits')

        # Deleting field 'Project.purpose'
        db.delete_column('projects_project', 'purpose_id')

        # Deleting field 'Project.methodology'
        db.delete_column('projects_project', 'methodology')

        # Deleting field 'Project.priority'
        db.delete_column('projects_project', 'priority')

        # Deleting field 'Project.benefit'
        db.delete_column('projects_project', 'benefit_id')

        # Deleting field 'Project.sponsor'
        db.delete_column('projects_project', 'sponsor')

        # Deleting field 'Project.risks'
        db.delete_column('projects_project', 'risks')

        # Deleting field 'Project.topic_other'
        db.delete_column('projects_project', 'topic_other')

        # Deleting field 'Project.end_period'
        db.delete_column('projects_project', 'end_period_id')

        # Deleting field 'Project.department'
        db.delete_column('projects_project', 'department')

        # Deleting field 'Project.benefit_other'
        db.delete_column('projects_project', 'benefit_other')

        # Deleting field 'Project.phone_number'
        db.delete_column('projects_project', 'phone_number')

        # Deleting field 'Project.email'
        db.delete_column('projects_project', 'email')

        # Deleting field 'Project.expected_results'
        db.delete_column('projects_project', 'expected_results')

        # Removing M2M table for field sharing_benefit on 'Project'
        db.delete_table('projects_project_sharing_benefit')

        # Removing M2M table for field opportunity on 'Project'
        db.delete_table('projects_project_opportunity')


    def backwards(self, orm):
        # Deleting model 'ProjectDetails'
        db.delete_table('projects_projectdetails')

        # Removing M2M table for field opportunity on 'ProjectDetails'
        db.delete_table('projects_projectdetails_opportunity')

        # Removing M2M table for field sharing_benefit on 'ProjectDetails'
        db.delete_table('projects_projectdetails_sharing_benefit')


        # User chose to not deal with backwards NULL issues for 'Project.limitations'
        raise RuntimeError("Cannot reverse this migration. 'Project.limitations' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.other_agencies'
        raise RuntimeError("Cannot reverse this migration. 'Project.other_agencies' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.infrastructure'
        raise RuntimeError("Cannot reverse this migration. 'Project.infrastructure' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.classification'
        raise RuntimeError("Cannot reverse this migration. 'Project.classification' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.presumptions'
        raise RuntimeError("Cannot reverse this migration. 'Project.presumptions' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.start_period'
        raise RuntimeError("Cannot reverse this migration. 'Project.start_period' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.explanation'
        raise RuntimeError("Cannot reverse this migration. 'Project.explanation' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.fiscal_year'
        raise RuntimeError("Cannot reverse this migration. 'Project.fiscal_year' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.director'
        raise RuntimeError("Cannot reverse this migration. 'Project.director' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.milestones'
        raise RuntimeError("Cannot reverse this migration. 'Project.milestones' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.goals'
        raise RuntimeError("Cannot reverse this migration. 'Project.goals' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.requirements'
        raise RuntimeError("Cannot reverse this migration. 'Project.requirements' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.stage'
        raise RuntimeError("Cannot reverse this migration. 'Project.stage' and its values cannot be restored.")
        # Adding field 'Project.purpose_other'
        db.add_column('projects_project', 'purpose_other',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Project.topic'
        raise RuntimeError("Cannot reverse this migration. 'Project.topic' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.needs'
        raise RuntimeError("Cannot reverse this migration. 'Project.needs' and its values cannot be restored.")
        # Adding field 'Project.classification_other'
        db.add_column('projects_project', 'classification_other',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Project.benefits'
        raise RuntimeError("Cannot reverse this migration. 'Project.benefits' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.purpose'
        raise RuntimeError("Cannot reverse this migration. 'Project.purpose' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.methodology'
        raise RuntimeError("Cannot reverse this migration. 'Project.methodology' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.priority'
        raise RuntimeError("Cannot reverse this migration. 'Project.priority' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.benefit'
        raise RuntimeError("Cannot reverse this migration. 'Project.benefit' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.sponsor'
        raise RuntimeError("Cannot reverse this migration. 'Project.sponsor' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.risks'
        raise RuntimeError("Cannot reverse this migration. 'Project.risks' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.topic_other'
        raise RuntimeError("Cannot reverse this migration. 'Project.topic_other' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.end_period'
        raise RuntimeError("Cannot reverse this migration. 'Project.end_period' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.department'
        raise RuntimeError("Cannot reverse this migration. 'Project.department' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.benefit_other'
        raise RuntimeError("Cannot reverse this migration. 'Project.benefit_other' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.phone_number'
        raise RuntimeError("Cannot reverse this migration. 'Project.phone_number' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.email'
        raise RuntimeError("Cannot reverse this migration. 'Project.email' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.expected_results'
        raise RuntimeError("Cannot reverse this migration. 'Project.expected_results' and its values cannot be restored.")
        # Adding M2M table for field sharing_benefit on 'Project'
        db.create_table('projects_project_sharing_benefit', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('benefit', models.ForeignKey(orm['projects.benefit'], null=False))
        ))
        db.create_unique('projects_project_sharing_benefit', ['project_id', 'benefit_id'])

        # Adding M2M table for field opportunity on 'Project'
        db.create_table('projects_project_opportunity', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('opportunity', models.ForeignKey(orm['projects.opportunity'], null=False))
        ))
        db.create_unique('projects_project_opportunity', ['project_id', 'opportunity_id'])


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
        'projects.projectdetails': {
            'Meta': {'object_name': 'ProjectDetails'},
            'benefit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Benefit']"}),
            'benefit_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'benefits': ('django.db.models.fields.TextField', [], {}),
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Classification']"}),
            'classification_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'director': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'end_period': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'end_period'", 'to': "orm['projects.FiscalYear']"}),
            'expected_results': ('django.db.models.fields.TextField', [], {}),
            'explanation': ('django.db.models.fields.TextField', [], {}),
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fiscal_year'", 'to': "orm['projects.FiscalYear']"}),
            'goals': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infrastructure': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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
            'topic_other': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
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