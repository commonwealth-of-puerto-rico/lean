from __future__ import absolute_import

from django.contrib import admin

from .models import (WorkflowType, WorkflowTypeAction, WorkflowTypeState,
    WorkflowTypeRelation, WorkflowInstance, WorkflowInstanceHistory, 
    WorkflowInstanceState)


class WorkflowTypeStateInline(admin.StackedInline):
    model = WorkflowTypeState


class WorkflowTypeAdmin(admin.ModelAdmin):
    model = WorkflowType
    inlines = (WorkflowTypeStateInline,)
    list_display = ('label', 'initial_action')


class WorkflowTypeActionAdmin(admin.ModelAdmin):
    model = WorkflowTypeAction
    list_display = ('workflow_type', 'label', 'required_permission', 'get_connections_as_string', 'state', 'auto_assignee_user', 'auto_assignee_group', 'allow_runtime_assignee_user', 'allow_runtime_assignee_group')
    filter_horizontal = ('connections',)


class WorkflowTypeRelationAdmin(admin.ModelAdmin):
    model = WorkflowTypeRelation
    list_display = ('content_type', 'workflow_type')


##  Instances


class WorkflowInstanceAdmin(admin.ModelAdmin):
    model = WorkflowInstance
    list_display = ('content_object', 'workflow_type', 'datetime_created')


class WorkflowInstanceHistoryAdmin(admin.ModelAdmin):
    model = WorkflowInstanceHistory
    list_display = ('workflow_instance', 'datetime_created', 'workflow_type_action', 'comments')


class WorkflowInstanceStateAdmin(admin.ModelAdmin):
    model = WorkflowInstanceState
    list_display = ('workflow_instance', 'datetime_created', 'workflow_state')


admin.site.register(WorkflowType, WorkflowTypeAdmin)
admin.site.register(WorkflowTypeAction, WorkflowTypeActionAdmin)
admin.site.register(WorkflowTypeRelation, WorkflowTypeRelationAdmin)

admin.site.register(WorkflowInstance, WorkflowInstanceAdmin)
admin.site.register(WorkflowInstanceHistory, WorkflowInstanceHistoryAdmin)
admin.site.register(WorkflowInstanceState, WorkflowInstanceStateAdmin)
