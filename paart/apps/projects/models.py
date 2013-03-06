from __future__ import absolute_import

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from agencies.models import Agency
from common.managers import OmitDisabledManager

from .literals import INFRASTRUCTURE_CHOICES


class FiscalYear(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'))

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = _(u'fiscal year')
        verbose_name_plural = _(u'fiscal years')
        ordering = ['label']


class Purpose(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    enabled = models.BooleanField(verbose_name=_(u'enabled'), default=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'purpose')
        verbose_name_plural = _(u'purposes')
        ordering = ['label']


class Classification(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    enabled = models.BooleanField(verbose_name=_(u'enabled'), default=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'classification')
        verbose_name_plural = _(u'classifications')
        ordering = ['label']


class Stage(models.Model):
    """
    Model to hold different stages a project can be in.  A project state.
    """
    label = models.CharField(max_length=128, verbose_name=_(u'label'))
    enabled = models.BooleanField(verbose_name=_(u'enabled'), default=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = _(u'stage')
        verbose_name_plural = _(u'stages')
        ordering = ['label']


class Benefit(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    enabled = models.BooleanField(verbose_name=_(u'enabled'), default=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'benefit')
        verbose_name_plural = _(u'benefits')
        ordering = ['label']


class Topic(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    enabled = models.BooleanField(verbose_name=_(u'enabled'), default=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'topic')
        verbose_name_plural = _(u'topics')
        ordering = ['label']


class Opportunity(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    enabled = models.BooleanField(verbose_name=_(u'enabled'), default=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'oportunity')
        verbose_name_plural = _(u'oportunities')
        ordering = ['label']


class Department(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    enabled = models.BooleanField(verbose_name=_(u'enabled'), default=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'department')
        verbose_name_plural = _(u'departments')
        ordering = ['label']


class Priority(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    enabled = models.BooleanField(verbose_name=_(u'enabled'), default=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'priority')
        verbose_name_plural = _(u'priorities')
        ordering = ['label']


class Methodology(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    enabled = models.BooleanField(verbose_name=_(u'enabled'), default=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'methodology')
        verbose_name_plural = _(u'methodologies')
        ordering = ['label']


class Goal(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    enabled = models.BooleanField(verbose_name=_(u'enabled'), default=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'goal')
        verbose_name_plural = _(u'goals')
        ordering = ['label']


class Project(models.Model):
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    agency = models.ForeignKey(Agency, verbose_name=_(u'agency'))
    label = models.CharField(max_length=128, verbose_name=_(u'name'))

    def __unicode__(self):
        return self.label

    @models.permalink
    def get_absolute_url(self):
        return ('project_view', [self.pk])

    def get_completion(self):
        total = 26
        count = 0
        for model in [self, 'projectinfo', 'projectbudget', 'projectdetails', 'projectopportunities']:
            if model == self:
                opts = model._meta
            else:
                try:
                    opts = getattr(self, model)._meta
                except ObjectDoesNotExist as e:
                    pass
                else:
                    for f in sorted(opts.fields + opts.many_to_many):
                        count += 1
                        print '%s: %s' % (f.name, f)

        return str(100 * float(count) / float(total))[0:5]

    class Meta:
        verbose_name = _(u'project')
        verbose_name_plural = _(u'projects')
        ordering = ['label']
        unique_together = ['agency', 'label']


class ProjectInfo(models.Model):
    project = models.OneToOneField(Project, verbose_name=_(u'project'))
    ## Informacion general - Paso 1  ##
    fiscal_year = models.ForeignKey(FiscalYear, related_name='fiscal_year', verbose_name=_(u'fiscal year'), help_text=_(u'HELP_TEXT_PROYECTINFO_FISCAL_YEAR'))
    purpose = models.ForeignKey(Purpose, verbose_name=_(u'purpose'), help_text=_(u'HELP_TEXT_PROYECTINFO_PURPOSE'))
    purpose_other = models.CharField(max_length=128, verbose_name=_(u'other purpose'), blank=True, help_text=_(u'HELP_TEXT_PROYECTINFO_PURPOSE_OTHER'))
    classification = models.ForeignKey(Classification, verbose_name=_(u'classification'), help_text=_(u'HELP_TEXT_PROYECTINFO_CLASSIFICATION'))
    classification_other = models.CharField(max_length=128, verbose_name=_(u'other classification'), blank=True, help_text=_(u'HELP_TEXT_PROYECTINFO_CLASSIFICATION_OTHER'))
    methodology = models.ForeignKey(Methodology, verbose_name=_('methodology'), help_text=_(u'HELP_TEXT_PROYECTINFO_METHODOLOGY'))
    methodology_other = models.CharField(max_length=128, verbose_name=_(u'other methodology'), blank=True)
    goals = models.ManyToManyField(Goal, verbose_name=_(u'goals'))
    # REMOVED: department = models.CharField(max_length=128, verbose_name=_(u'department/work unit'))
    department = models.ForeignKey(Department, verbose_name=_(u'department/work unit'), help_text=_(u'HELP_TEXT_PROYECTINFO_DEPARTMENT'))
    sponsor = models.CharField(max_length=64, verbose_name=_(u'sponsor'))
    # Remove email of sponsor as per Giancarlo's recommendations
    # REMOVED: email = models.EmailField(verbose_name=_(u'email'))
    # REMOVED: phone_number = models.CharField(max_length=32, verbose_name=_(u'phone number'))
    # REMOVED: goals = models.TextField(verbose_name=_(u'goals/objectives'), help_text=_(u'HELP_TEXT_PROYECTINFO_GOALS'))
    # REMOVED: needs = models.TextField(verbose_name=_(u'project needs'), help_text=_(u'HELP_TEXT_PROYECTINFO_NEEDS'))
    expected_results = models.TextField(verbose_name=_('expected results'), help_text=_(u'HELP_TEXT_PROYECTINFO_EXPECTED_RESULTS'))
    milestones = models.TextField(verbose_name=_(u'milestones'), help_text=_(u'HELP_TEXT_PROYECTINFO_MILESTONES'))

    def __unicode__(self):
        return ugettext(u'project information')

    @models.permalink
    def get_absolute_url(self):
        return ('project_info_view', [self.project.pk])

    class Meta:
        verbose_name = _(u'project details')
        verbose_name_plural = _(u'projects details')


class ProjectBudget(models.Model):
    project = models.OneToOneField(Project, verbose_name=_(u'project'))
    ## Presupuesto - Paso 2 ##
    infrastructure = models.CharField(max_length=1, choices=INFRASTRUCTURE_CHOICES, verbose_name=_(u'infrastructure needs'))
    requirements = models.TextField(verbose_name=_(u'project critical requirements'))
    presumptions = models.TextField(verbose_name=_(u'presumptions'), help_text=_(u'HELP_TEXT_PROYECTBUDGET_PRESUMPTIONS'))
    limitations = models.TextField(verbose_name=_(u'limitations'), help_text=_(u'HELP_TEXT_PROYECTBUDGET_LIMITATIONS'))
    risks = models.TextField(verbose_name=_(u'risks'), help_text=_(u'HELP_TEXT_PROYECTBUDGET_RISKS'))
    benefits = models.TextField(verbose_name=_(u'benefits'))
    # TODO: Adquisition
    director = models.TextField(verbose_name=_(u'project director'))
    # TODO: Costs

    def __unicode__(self):
        return ugettext(u'project budget')

    @models.permalink
    def get_absolute_url(self):
        return ('project_budget_view', [self.project.pk])

    class Meta:
        verbose_name = _(u'project budget')
        verbose_name_plural = _(u'projects budgets')


class ProjectDetails(models.Model):
    project = models.OneToOneField(Project, verbose_name=_(u'project'))
    ## Detalle del Proyecto - Paso 3 ##
    # 1. Fecha de comienzo
    start_period = models.ForeignKey(FiscalYear, related_name='start_period', verbose_name=_(u'start period'), help_text=_(u'HELP_TEXT_PROYECTDETAILS_START_PERIOD'))
    # 2. Fecha de terminacion
    end_period = models.ForeignKey(FiscalYear, related_name='end_period', verbose_name=_(u'end period'), help_text=_(u'HELP_TEXT_PROYECTDETAILS_END_PERIOD'))
    # 3. Etapa del proyecto
    stage = models.ForeignKey(Stage, verbose_name=_(u'stage'), help_text=_(u'HELP_TEXT_PROYECTDETAILS_STAGE'))
    # 4. Beneficios de Implementacion
    # Remove Topic and Benefit fields as per Giancarlo's comments
    # benefit = models.ForeignKey(Benefit, verbose_name=_(u'implementation benefit'))
    # 5. Otro beneficio
    # benefit_other = models.CharField(max_length=128, verbose_name=_(u'other benefit'), blank=True)
    priority = models.ForeignKey(Priority, verbose_name=_(u'priority'), help_text=_(u'HELP_TEXT_PROYECTDETAILS_PRIORITY'))
    # topic = models.ForeignKey(Topic, verbose_name=_(u'topic'))
    # topic_other = models.CharField(max_length=128, verbose_name=_(u'other topic'), blank=True)

    def __unicode__(self):
        return ugettext(u'project details')

    @models.permalink
    def get_absolute_url(self):
        return ('project_details_view', [self.project.pk])

    class Meta:
        verbose_name = _(u'project details')
        verbose_name_plural = _(u'projects details')


class ProjectOpportunities(models.Model):
    project = models.OneToOneField(Project, verbose_name=_(u'project'))
    ## Oportunidades interagenciales - Paso 4
    opportunity = models.ManyToManyField(Opportunity, verbose_name=_(u'opportunity'))
    sharing_benefit = models.ManyToManyField(Benefit, related_name='sharing_benefit', verbose_name=_(u'sharing benefits'))
    explanation = models.TextField(verbose_name=_('short explanation (50 words or less)'))
    other_agencies = models.ManyToManyField(Agency, verbose_name=_('other agencies or involved agencies'), null=True, blank=True)

    def __unicode__(self):
        return ugettext(u'project opportunities')

    @models.permalink
    def get_absolute_url(self):
        return ('project_opportunities_view', [self.project.pk])

    class Meta:
        verbose_name = _(u'project opportunities')
        verbose_name_plural = _(u'projects opportunities')


#class ProjectAdquisition(models.Model):
#class ProjectCosts(models.Model):

class ProjectFile(models.Model):
    project = models.ForeignKey(Project, verbose_name=_(u'project'))
    label = models.CharField(max_length=128, verbose_name=_(u'label'))
    file = models.FileField(upload_to='project_files', verbose_name=_(u'file'))

    def __unicode__(self):
        return self.label

    def get_base_filename(self):
        return self.file.name.split('/')[1]

    @models.permalink
    def get_absolute_url(self):
        return ('project_file_list', [self.project.pk])

    class Meta:
        verbose_name = _(u'project file')
        verbose_name_plural = _(u'projects files')
