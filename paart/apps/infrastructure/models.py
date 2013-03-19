from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from agencies.models import Agency
from common.managers import OmitDisabledManager


class FiscalYear(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'))

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = _(u'fiscal year')
        verbose_name_plural = _(u'fiscal years')
        ordering = ['label']


class Project(models.Model):
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    agency = models.ForeignKey(Agency, related_name='agency_infrastructure_project', verbose_name=_(u'agency'))
    label = models.CharField(max_length=128, verbose_name=_(u'name'))
    description = models.TextField(verbose_name=_(u'description'))

    def __unicode__(self):
        return self.label

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('project_view', [self.pk])

    class Meta:
        verbose_name = _(u'project')
        verbose_name_plural = _(u'projects')
        ordering = ['label']
        unique_together = ['agency', 'label']


class ProjectInfo(models.Model):
    project = models.OneToOneField(Project, verbose_name=_(u'project'))
    fiscal_year = models.ForeignKey(FiscalYear, related_name='fiscal_year', verbose_name=_(u'fiscal year'), help_text=_(u'HELP_TEXT_PROYECTINFO_FISCAL_YEAR'))
    manager = models.CharField(max_length=64, verbose_name=_(u'manager'))

    def __unicode__(self):
        return ugettext(u'project information')

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('project_info_view', [self.project.pk])

    class Meta:
        verbose_name = _(u'project information')
        verbose_name_plural = _(u'projects information')


class ProjectBudget(models.Model):
    project = models.OneToOneField(Project, verbose_name=_(u'project'))
    budget = models.PositiveIntegerField(verbose_name=_(u'budget'), blank=True, null=True)
    design_costs = models.PositiveIntegerField(verbose_name=_(u'design costs'), blank=True, null=True)
    inspection_costs = models.PositiveIntegerField(verbose_name=_(u'inspection costs'), blank=True, null=True)
    construction_costs = models.PositiveIntegerField(verbose_name=_(u'construction costs'), blank=True, null=True)
    #change_order_costs = models.PositiveIntegerField(verbose_name=_(u'change order costs'), blank=True, null=True) # <=== TODO: meaning of field?

    def __unicode__(self):
        return ugettext(u'project budget')

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('project_info_view', [self.project.pk])

    class Meta:
        verbose_name = _(u'project budget')
        verbose_name_plural = _(u'projects budgets')


class ProjectFile(models.Model):
    project = models.ForeignKey(Project, verbose_name=_(u'project'))
    label = models.CharField(max_length=128, verbose_name=_(u'label'))
    file = models.FileField(upload_to='project_files', verbose_name=_(u'file'))

    def __unicode__(self):
        return self.label

    def get_base_filename(self):
        return self.file.name.split('/')[1]

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('project_file_list', [self.project.pk])

    class Meta:
        verbose_name = _(u'project file')
        verbose_name_plural = _(u'projects files')
