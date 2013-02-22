from __future__ import absolute_import

from django.contrib.auth.models import User, Group
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from permissions.models import StoredPermission

from .managers import WorkflowInstanceManager


class WorkflowType(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'))
    description = models.TextField(verbose_name=_(u'description'), blank=True)
    initial_state = models.ForeignKey('WorkflowTypeState', verbose_name=_(u'initial state'), blank=True, null=True)
    initial_action = models.ForeignKey('WorkflowTypeAction', verbose_name=_(u'initial action'), blank=True, null=True)

    def __unicode__(self):
        return self.label

    def get_actions(self):
        return self.workflowtypeaction_set.all()

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('project_file_list', [self.project.pk])

    class Meta:
        verbose_name = _(u'workflow type')
        verbose_name_plural = _(u'workflow types')
        ordering = ['label']


class WorkflowTypeAction(models.Model):
    workflow_type = models.ForeignKey(WorkflowType, verbose_name=_(u'workflow type'))
    label = models.CharField(max_length=128, verbose_name=_(u'label'))
    description = models.TextField(verbose_name=_(u'description'), blank=True)
    connections = models.ManyToManyField('self', verbose_name=_(u'connections'), blank=True, symmetrical=False)
    state = models.ForeignKey('WorkflowTypeState', verbose_name=_(u'state'), blank=True, null=True)
    auto_assignee_user = models.ForeignKey(User, verbose_name=_(u'auto assignee user'), blank=True, null=True)
    auto_assignee_group = models.ForeignKey(Group, verbose_name=_(u'auto assignee group'), blank=True, null=True)
    allow_runtime_assignee_user = models.BooleanField(verbose_name=_(u'allow runtime assignee user'))
    allow_runtime_assignee_group = models.BooleanField(verbose_name=_(u'allow runtime assignee group'))
    required_permission = models.ForeignKey(StoredPermission, verbose_name=_(u'required permission'), help_text=_(u'Will be checked globally or in relation to the workflow instance\'s content object.'), blank=True, null=True)

    def __unicode__(self):
        return self.label

    def get_connections_as_string(self):
        return ', '.join(self.connections.values_list('label', flat=True))

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('project_file_list', [self.project.pk])

    class Meta:
        verbose_name = _(u'workflow type action')
        verbose_name_plural = _(u'workflow types actions')
        unique_together = ('workflow_type', 'label')
        ordering = ['label']


class WorkflowTypeState(models.Model):
    workflow_type = models.ForeignKey(WorkflowType, verbose_name=_(u'workflow type'))
    label = models.CharField(max_length=128, verbose_name=_(u'label'))
    description = models.TextField(verbose_name=_(u'description'), blank=True)

    def __unicode__(self):
        return self.label

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('project_file_list', [self.project.pk])

    class Meta:
        verbose_name = _(u'workflow type state')
        verbose_name_plural = _(u'workflow types states')
        unique_together = ('workflow_type', 'label')
        ordering = ['label']


class WorkflowTypeRelation(models.Model):
    content_type = models.ForeignKey(ContentType)
    workflow_type = models.ForeignKey(WorkflowType, verbose_name=_(u'workflow type'))

    class Meta:
        verbose_name = _(u'workflow type relation')
        verbose_name_plural = _(u'workflow types relation')
        unique_together = ('workflow_type', 'content_type')


# Instances


class WorkflowInstance(models.Model):
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    workflow_type = models.ForeignKey(WorkflowType, verbose_name=_(u'workflow type'))

    objects = WorkflowInstanceManager()

    def __unicode__(self):
        #return '%s - %s - %s' % (unicode(self.workflow_type), unicode(self.content_object), unicode(self.datetime_created))
        return unicode(self.workflow_type)

    def get_history(self):
        return self.workflowinstancehistory_set.all()

    def get_latest_action(self):
        try:
            return self.get_history().order_by('-datetime_created')[0]
        except IndexError:
            return None

    def get_states(self):
        return self.workflowinstancestate_set.all()

    def get_latest_state(self):
        try:
            return self.get_states().order_by('-datetime_created')[0]
        except IndexError:
            return None

    def get_actions(self):
        return self.get_latest_action().workflow_type_action.connections.all()

    def commit(self, action, user, comments=None, assignee_group=None, assignee_user=None):
        WorkflowInstanceHistory.objects.create(workflow_instance=self, workflow_type_action=action, user=user, comments=comments, assignee_group=assignee_group, assignee_user=assignee_user)

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('project_file_list', [self.project.pk])

    class Meta:
        verbose_name = _(u'workflow instance')
        verbose_name_plural = _(u'workflow instances')


class WorkflowInstanceHistory(models.Model):
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    workflow_instance = models.ForeignKey(WorkflowInstance, verbose_name=_(u'workflow instance'))
    workflow_type_action = models.ForeignKey(WorkflowTypeAction, verbose_name=_(u'workflow type action'))
    user = models.ForeignKey(User, related_name='user', verbose_name=_(u'user'))
    comments = models.TextField(verbose_name=_(u'comments'), blank=True)
    assignee_user = models.ForeignKey(User, verbose_name=_(u'assignee user'), blank=True, null=True)
    assignee_group = models.ForeignKey(Group, verbose_name=_(u'assignee group'), blank=True, null=True)

    def __unicode__(self):
        return unicode(self.workflow_type_action)

    def save(self, *args, **kwargs):
        super(WorkflowInstanceHistory, self).save(*args, **kwargs)
        if self.workflow_type_action.state:
            WorkflowInstanceState.objects.create(workflow_instance=self.workflow_instance, workflow_state=self.workflow_type_action.state)

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('project_file_list', [self.project.pk])

    class Meta:
        verbose_name = _(u'workflow instance history')
        verbose_name_plural = _(u'workflow instance history')
        ordering = ['datetime_created']


class WorkflowInstanceState(models.Model):
    workflow_instance = models.ForeignKey(WorkflowInstance, verbose_name=_(u'workflow instance'))
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    workflow_state = models.ForeignKey(WorkflowTypeState, verbose_name=_(u'workflow type state'))

    def __unicode__(self):
        return unicode(self.workflow_state)

    class Meta:
        verbose_name = _(u'workflow instance state')
        verbose_name_plural = _(u'workflow instance states')
