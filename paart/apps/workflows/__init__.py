from __future__ import absolute_import

from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from common.utils import encapsulate
from navigation.api import register_model_list_columns

from .models import WorkflowInstance, WorkflowInstanceHistory, WorkflowTypeRelation


register_model_list_columns(WorkflowInstance, [
    {'name': _(u'type'), 'attribute': 'workflow_type'},
    {'name': _(u'latest action'), 'attribute': 'get_latest_action'},
    {'name': _(u'lastest state'), 'attribute': 'get_latest_state'},
])

register_model_list_columns(WorkflowInstanceHistory, [
    {'name': _(u'date and time'), 'attribute': 'datetime_created'},
    {'name': _(u'action'), 'attribute': 'workflow_type_action'},
    {'name': _(u'user'), 'attribute': encapsulate(lambda x: x.user or '')},
    {'name': _(u'assignee group'), 'attribute': encapsulate(lambda x: x.assignee_group or '')},
    {'name': _(u'assignee user'), 'attribute': encapsulate(lambda x: x.assignee_user or '')},
    {'name': _(u'comments'), 'attribute': 'comments'},
])

@receiver(post_save, dispatch_uid='launch_workflow_on_create')
def launch_workflow_on_create(sender, **kwargs):
    if kwargs['created']:
        content_type = ContentType.objects.get_for_model(kwargs['instance'])
        for relation in WorkflowTypeRelation.objects.filter(content_type=content_type):
            workflow_instance = WorkflowInstance.objects.create(content_object=kwargs['instance'],
                workflow_type=relation.workflow_type)
