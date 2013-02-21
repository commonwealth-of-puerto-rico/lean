# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WorkflowType'
        db.create_table('workflows_workflowtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('workflows', ['WorkflowType'])

        # Adding model 'WorkflowTypeAction'
        db.create_table('workflows_workflowtypeaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workflow_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflows.WorkflowType'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflows.WorkflowTypeState'], null=True, blank=True)),
            ('assignee_content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], blank=True)),
            ('assignee_object_id', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
        ))
        db.send_create_signal('workflows', ['WorkflowTypeAction'])

        # Adding M2M table for field connections on 'WorkflowTypeAction'
        db.create_table('workflows_workflowtypeaction_connections', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_workflowtypeaction', models.ForeignKey(orm['workflows.workflowtypeaction'], null=False)),
            ('to_workflowtypeaction', models.ForeignKey(orm['workflows.workflowtypeaction'], null=False))
        ))
        db.create_unique('workflows_workflowtypeaction_connections', ['from_workflowtypeaction_id', 'to_workflowtypeaction_id'])

        # Adding model 'WorkflowTypeState'
        db.create_table('workflows_workflowtypestate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workflow_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflows.WorkflowType'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('workflows', ['WorkflowTypeState'])

        # Adding model 'WorkflowTypeRelation'
        db.create_table('workflows_workflowtyperelation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workflow_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflows.WorkflowType'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
        ))
        db.send_create_signal('workflows', ['WorkflowTypeRelation'])

        # Adding model 'WorkflowInstance'
        db.create_table('workflows_workflowinstance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 21, 0, 0))),
            ('workflow_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflows.WorkflowType'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('workflows', ['WorkflowInstance'])

        # Adding model 'WorkflowInstanceHistory'
        db.create_table('workflows_workflowinstancehistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 21, 0, 0))),
            ('workflow_instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflows.WorkflowType'])),
            ('workflow_type_action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflows.WorkflowTypeAction'])),
        ))
        db.send_create_signal('workflows', ['WorkflowInstanceHistory'])

        # Adding model 'WorkflowInstanceState'
        db.create_table('workflows_workflowinstancestate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workflow_instance', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['workflows.WorkflowInstance'], unique=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 21, 0, 0))),
            ('workflow_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workflows.WorkflowTypeState'])),
        ))
        db.send_create_signal('workflows', ['WorkflowInstanceState'])


    def backwards(self, orm):
        # Deleting model 'WorkflowType'
        db.delete_table('workflows_workflowtype')

        # Deleting model 'WorkflowTypeAction'
        db.delete_table('workflows_workflowtypeaction')

        # Removing M2M table for field connections on 'WorkflowTypeAction'
        db.delete_table('workflows_workflowtypeaction_connections')

        # Deleting model 'WorkflowTypeState'
        db.delete_table('workflows_workflowtypestate')

        # Deleting model 'WorkflowTypeRelation'
        db.delete_table('workflows_workflowtyperelation')

        # Deleting model 'WorkflowInstance'
        db.delete_table('workflows_workflowinstance')

        # Deleting model 'WorkflowInstanceHistory'
        db.delete_table('workflows_workflowinstancehistory')

        # Deleting model 'WorkflowInstanceState'
        db.delete_table('workflows_workflowinstancestate')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'workflows.workflowinstance': {
            'Meta': {'object_name': 'WorkflowInstance'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 21, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'workflow_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workflows.WorkflowType']"})
        },
        'workflows.workflowinstancehistory': {
            'Meta': {'object_name': 'WorkflowInstanceHistory'},
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 21, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'workflow_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workflows.WorkflowType']"}),
            'workflow_type_action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workflows.WorkflowTypeAction']"})
        },
        'workflows.workflowinstancestate': {
            'Meta': {'object_name': 'WorkflowInstanceState'},
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 21, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'workflow_instance': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['workflows.WorkflowInstance']", 'unique': 'True'}),
            'workflow_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workflows.WorkflowTypeState']"})
        },
        'workflows.workflowtype': {
            'Meta': {'object_name': 'WorkflowType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'workflows.workflowtypeaction': {
            'Meta': {'object_name': 'WorkflowTypeAction'},
            'assignee_content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'blank': 'True'}),
            'assignee_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'connections': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'connections_rel_+'", 'to': "orm['workflows.WorkflowTypeAction']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workflows.WorkflowTypeState']", 'null': 'True', 'blank': 'True'}),
            'workflow_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workflows.WorkflowType']"})
        },
        'workflows.workflowtyperelation': {
            'Meta': {'object_name': 'WorkflowTypeRelation'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'workflow_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workflows.WorkflowType']"})
        },
        'workflows.workflowtypestate': {
            'Meta': {'object_name': 'WorkflowTypeState'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'workflow_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workflows.WorkflowType']"})
        }
    }

    complete_apps = ['workflows']