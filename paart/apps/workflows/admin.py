from __future__ import absolute_import

from django.contrib import admin

from .models import WorkflowType, WorkflowTypeAction, WorkflowTypeState


class WorkflowTypeStateInline(admin.StackedInline):
    model = WorkflowTypeState
    #list_display = ('label', 'state', 'auto_assignee_user', 'auto_assignee_group', 'allow_runtime_assignee_user', 'allow_runtime_assignee_group')
    #filter_horizontal = ('connections',)


class WorkflowTypeAdmin(admin.ModelAdmin):
    model = WorkflowType
    inlines = (WorkflowTypeStateInline,)
    list_display = ('label', 'initial_state', 'initial_action')
    #filter_horizontal = ('opportunity', 'sharing_benefit')


class WorkflowTypeActionAdmin(admin.ModelAdmin):
    model = WorkflowTypeAction
    list_display = ('workflow_type', 'label', 'get_connections_as_string', 'state', 'auto_assignee_user', 'auto_assignee_group', 'allow_runtime_assignee_user', 'allow_runtime_assignee_group')
    filter_horizontal = ('connections',)


admin.site.register(WorkflowType, WorkflowTypeAdmin)
admin.site.register(WorkflowTypeAction, WorkflowTypeActionAdmin)
