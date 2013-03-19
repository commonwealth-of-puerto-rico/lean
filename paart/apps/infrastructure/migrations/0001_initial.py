# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FiscalYear'
        db.create_table('infrastructure_fiscalyear', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('infrastructure', ['FiscalYear'])

        # Adding model 'Project'
        db.create_table('infrastructure_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 19, 0, 0))),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='agency_infrastructure_project', to=orm['agencies.Agency'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('infrastructure', ['Project'])

        # Adding unique constraint on 'Project', fields ['agency', 'label']
        db.create_unique('infrastructure_project', ['agency_id', 'label'])

        # Adding model 'ProjectInfo'
        db.create_table('infrastructure_projectinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['infrastructure.Project'], unique=True)),
            ('fiscal_year', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fiscal_year', to=orm['infrastructure.FiscalYear'])),
            ('manager', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('infrastructure', ['ProjectInfo'])

        # Adding model 'ProjectBudget'
        db.create_table('infrastructure_projectbudget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['infrastructure.Project'], unique=True)),
            ('budget', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('design_costs', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('inspection_costs', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('construction_costs', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('infrastructure', ['ProjectBudget'])

        # Adding model 'ProjectFile'
        db.create_table('infrastructure_projectfile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['infrastructure.Project'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('infrastructure', ['ProjectFile'])


    def backwards(self, orm):
        # Removing unique constraint on 'Project', fields ['agency', 'label']
        db.delete_unique('infrastructure_project', ['agency_id', 'label'])

        # Deleting model 'FiscalYear'
        db.delete_table('infrastructure_fiscalyear')

        # Deleting model 'Project'
        db.delete_table('infrastructure_project')

        # Deleting model 'ProjectInfo'
        db.delete_table('infrastructure_projectinfo')

        # Deleting model 'ProjectBudget'
        db.delete_table('infrastructure_projectbudget')

        # Deleting model 'ProjectFile'
        db.delete_table('infrastructure_projectfile')


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
        'infrastructure.fiscalyear': {
            'Meta': {'ordering': "['label']", 'object_name': 'FiscalYear'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'infrastructure.project': {
            'Meta': {'ordering': "['label']", 'unique_together': "(['agency', 'label'],)", 'object_name': 'Project'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agency_infrastructure_project'", 'to': "orm['agencies.Agency']"}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 19, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'infrastructure.projectbudget': {
            'Meta': {'object_name': 'ProjectBudget'},
            'budget': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'construction_costs': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'design_costs': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspection_costs': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['infrastructure.Project']", 'unique': 'True'})
        },
        'infrastructure.projectfile': {
            'Meta': {'object_name': 'ProjectFile'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['infrastructure.Project']"})
        },
        'infrastructure.projectinfo': {
            'Meta': {'object_name': 'ProjectInfo'},
            'fiscal_year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fiscal_year'", 'to': "orm['infrastructure.FiscalYear']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['infrastructure.Project']", 'unique': 'True'})
        }
    }

    complete_apps = ['infrastructure']