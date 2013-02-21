from django.contrib.auth.models import User, Group
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


class WorkflowType(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'))
    description = models.TextField(verbose_name=_(u'description'), blank=True)
    initial_state = models.ForeignKey('WorkflowTypeState', verbose_name=_(u'initial state'), blank=True, null=True)
    initial_action = models.ForeignKey('WorkflowTypeAction', verbose_name=_(u'initial action'), blank=True, null=True)

    def __unicode__(self):
        return self.label

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
    workflow_type = models.ForeignKey(WorkflowType, verbose_name=_(u'workflow type'))
    content_type = models.ForeignKey(ContentType)

    class Meta:
        verbose_name = _(u'workflow type relation')
        verbose_name_plural = _(u'workflow types relation')
        unique_together = ('workflow_type', 'content_type')


# Instances


class WorkflowInstance(models.Model):
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    workflow_type = models.ForeignKey(WorkflowType, verbose_name=_(u'workflow type'))
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    #def __unicode__(self):
    #    return self.label

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('project_file_list', [self.project.pk])

    class Meta:
        verbose_name = _(u'workflow type state')
        verbose_name_plural = _(u'workflow types states')


class WorkflowInstanceHistory(models.Model):
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    workflow_instance = models.ForeignKey(WorkflowType, verbose_name=_(u'workflow instance'))
    workflow_type_action = models.ForeignKey(WorkflowTypeAction, verbose_name=_(u'workflow type action'))
    comments = models.TextField(verbose_name=_(u'comments'), blank=True)

    #def __unicode__(self):
    #    return self.label

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('project_file_list', [self.project.pk])

    class Meta:
        verbose_name = _(u'workflow instance history')
        verbose_name_plural = _(u'workflow instance history')


class WorkflowInstanceState(models.Model):
    workflow_instance = models.OneToOneField(WorkflowInstance, verbose_name=_(u'workflow instance'))
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    workflow_state = models.ForeignKey(WorkflowTypeState, verbose_name=_(u'workflow type state'))

    class Meta:
        verbose_name = _(u'workflow instance state')
        verbose_name_plural = _(u'workflow instance states')
