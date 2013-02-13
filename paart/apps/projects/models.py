from django.db import models
from django.utils.translation import ugettext_lazy as _

from agencies.models import Agency


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


class FiscalYear(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'))

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = _(u'fiscal year')
        verbose_name_plural = _(u'fiscal years')
        ordering = ['label']


INFRASTRUCTURE_NEW = 'N'
INFRASTRUCTURE_OLD = 'O'

INFRASTRUCTURE_CHOICES = (
    (INFRASTRUCTURE_NEW, _(u'New')),
    (INFRASTRUCTURE_OLD, _(u'Old')),
)


class Project(models.Model):
    agency = models.ForeignKey(Agency, verbose_name=_(u'agency'))
    fiscal_year = models.CharField(max_length=9, verbose_name=_(u'fiscal year'))
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    purpose = models.ForeignKey(Purpose, verbose_name=_(u'purpose'))
    purpose_other = models.CharField(max_length=128, verbose_name=_(u'other purpose'), blank=True)
    classification = models.ForeignKey(Classification, verbose_name=_(u'classification'))
    classification_other = models.CharField(max_length=128, verbose_name=_(u'other classification'), blank=True)
    department = models.CharField(max_length=128, verbose_name=_(u'department/work unit'))
    sponsor = models.CharField(max_length=64, verbose_name=_(u'sponsor'))
    email = models.EmailField(verbose_name=_(u'email'))
    phone_number = models.CharField(max_length=32, verbose_name=_(u'phone number'))
    goals = models.TextField(verbose_name=_(u'goals'))
    needs = models.TextField(verbose_name=_(u'needs'))
    expected_results = models.TextField(verbose_name=_('expected results'))
    methodology = models.TextField(verbose_name=_('methodology'))
    milestones = models.TextField(verbose_name=_(u'milestones'))
    infrastructure = models.CharField(max_length=1, choices=INFRASTRUCTURE_CHOICES, verbose_name=_(u'infrastructure needs'))
    requirements = models.TextField(verbose_name=_(u'requirements'))
    # Presunciones
    limitations = models.TextField(verbose_name=_(u'limitations'))
    risks = models.TextField(verbose_name=_(u'risks'))
    benefits = models.TextField(verbose_name=_(u'benefits'))
    # Adquisition
    director = models.TextField(verbose_name=_(u'project director'))
    # Costs

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'project')
        verbose_name_plural = _(u'projects')
        ordering = ['label']


class Stage(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'))

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = _(u'stage')
        verbose_name_plural = _(u'stages')
        ordering = ['label']


class Detail(models.Model):
    project = models.ForeignKey(Project, verbose_name=_(u'project'))
    start_period = models.ForeignKey(FiscalYear, related_name='start_period', verbose_name=_(u'start period'))
    end_period = models.ForeignKey(FiscalYear, related_name='end_period', verbose_name=_(u'end period'))
    stage = models.ForeignKey(Stage, verbose_name=_(u'stage'))

    def __unicode__(self):
        return unicode(self.project)

    class Meta:
        verbose_name = _(u'detail')
        verbose_name_plural = _(u'details')
        ordering = ['project']
