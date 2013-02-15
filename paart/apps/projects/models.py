from django.db import models
from django.utils.translation import ugettext_lazy as _

from agencies.models import Agency

from .literals import INFRASTRUCTURE_CHOICES, PRIORITY_CHOICES


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

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = _(u'stage')
        verbose_name_plural = _(u'stages')
        ordering = ['label']


class Benefit(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)

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

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'oportunity')
        verbose_name_plural = _(u'oportunities')
        ordering = ['label']


class Project(models.Model):
    agency = models.ForeignKey(Agency, verbose_name=_(u'agency'))
    fiscal_year = models.ForeignKey(FiscalYear, related_name='fiscal_year', verbose_name=_(u'fiscal year'))
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    purpose = models.ForeignKey(Purpose, verbose_name=_(u'purpose'))
    purpose_other = models.CharField(max_length=128, verbose_name=_(u'other purpose'), blank=True)
    classification = models.ForeignKey(Classification, verbose_name=_(u'classification'))
    classification_other = models.CharField(max_length=128, verbose_name=_(u'other classification'), blank=True)
    department = models.CharField(max_length=128, verbose_name=_(u'department/work unit'))
    sponsor = models.CharField(max_length=64, verbose_name=_(u'sponsor'))
    email = models.EmailField(verbose_name=_(u'email'))
    phone_number = models.CharField(max_length=32, verbose_name=_(u'phone number'))
    goals = models.TextField(verbose_name=_(u'goals/objectives'))
    needs = models.TextField(verbose_name=_(u'project needs'))
    expected_results = models.TextField(verbose_name=_('expected results'))
    methodology = models.TextField(verbose_name=_('methodology'))
    milestones = models.TextField(verbose_name=_(u'milestones'))
    infrastructure = models.CharField(max_length=1, choices=INFRASTRUCTURE_CHOICES, verbose_name=_(u'infrastructure needs'))
    requirements = models.TextField(verbose_name=_(u'project critical requirements'))
    presumptions = models.TextField(verbose_name=_(u'presumptions'))
    limitations = models.TextField(verbose_name=_(u'limitations'))
    risks = models.TextField(verbose_name=_(u'risks'))
    benefits = models.TextField(verbose_name=_(u'benefits'))
    # TODO: Adquisition
    director = models.TextField(verbose_name=_(u'project director'))
    # TODO: Costs
    ## Detalle del Proyecto ##
    # 1. Fecha de comienzo
    start_period = models.ForeignKey(FiscalYear, related_name='start_period', verbose_name=_(u'start period'))
    # 2. Fecha de terminacion
    end_period = models.ForeignKey(FiscalYear, related_name='end_period', verbose_name=_(u'end period'))
    # 3. Etapa del proyecto
    stage = models.ForeignKey(Stage, verbose_name=_(u'stage'))
    # 4. Beneficios de Implementacion
    benefit = models.ForeignKey(Benefit, verbose_name=_(u'implementation benefit'))
    # 5. Otro beneficio
    benefit_other = models.CharField(max_length=128, verbose_name=_(u'other benefit'))
    priority = models.PositiveIntegerField(choices=PRIORITY_CHOICES, verbose_name=_(u'priority'))
    topic = models.ForeignKey(Topic, verbose_name=_(u'topic'))
    topic_other = models.CharField(max_length=128, verbose_name=_(u'other topic'))
    ## Oportunidades interagenciales ##
    opportunity = models.ManyToManyField(Opportunity, verbose_name=_(u'opportunity'))
    sharing_benefit = models.ManyToManyField(Benefit, related_name='sharing_benefit', verbose_name=_(u'sharing benefits'))
    explanation = models.TextField(verbose_name=_('short explanation (50 words or less)'))
    other_agencies = models.TextField(verbose_name=_('other agencies or involved agencies'))

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    @models.permalink
    def get_absolute_url(self):
        return ('project_view', [self.pk])

    class Meta:
        verbose_name = _(u'project')
        verbose_name_plural = _(u'projects')
        ordering = ['label']
