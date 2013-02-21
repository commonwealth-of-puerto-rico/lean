# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'WorkflowTypeAction.auto_assignee_group'
        db.alter_column('workflows_workflowtypeaction', 'auto_assignee_group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.Group'], null=True))

        # Changing field 'WorkflowTypeAction.auto_assignee_user'
        db.alter_column('workflows_workflowtypeaction', 'auto_assignee_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'WorkflowTypeAction.auto_assignee_group'
        raise RuntimeError("Cannot reverse this migration. 'WorkflowTypeAction.auto_assignee_group' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'WorkflowTypeAction.auto_assignee_user'
        raise RuntimeError("Cannot reverse this migration. 'WorkflowTypeAction.auto_assignee_user' and its values cannot be restored.")

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
            'allow_runtime_assignee_group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_runtime_assignee_user': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_assignee_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            'auto_assignee_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
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