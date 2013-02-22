from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.api import register_model_list_columns

from .models import WorkflowInstance, WorkflowInstanceHistory


register_model_list_columns(WorkflowInstance, [
    {'name': _(u'type'), 'attribute': 'workflow_type'},
    {'name': _(u'latest action'), 'attribute': 'get_latest_action'},
    {'name': _(u'lastest state'), 'attribute': 'get_latest_state'},
])

register_model_list_columns(WorkflowInstanceHistory, [
    {'name': _(u'date and time'), 'attribute': 'datetime_created'},
    {'name': _(u'action'), 'attribute': 'workflow_type_action'},
    {'name': _(u'user'), 'attribute': 'user'},
    {'name': _(u'assignee group'), 'attribute': 'assignee_group'},
    {'name': _(u'assignee user'), 'attribute': 'assignee_user'},
    {'name': _(u'comments'), 'attribute': 'comments'},
])
