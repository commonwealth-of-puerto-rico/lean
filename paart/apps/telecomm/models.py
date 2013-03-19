from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from agencies.models import Agency


class Provider(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'provider')
        verbose_name_plural = _(u'providers')
        ordering = ['label']


class Technology(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'technology')
        verbose_name_plural = _(u'technologies')
        ordering = ['label']


class Equipment(models.Model):
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    agency = models.ForeignKey(Agency, verbose_name=_(u'agency'))
    label = models.CharField(max_length=128, verbose_name=_(u'label'))
    intranet_connectivity = models.BooleanField(verbose_name=_(u'intranet connectivity?'))
    # TODO: is purpose a dropdown?
    purpose = models.CharField(max_length=128, verbose_name=_(u'purpose'))
    internet_connectivity = models.BooleanField(verbose_name=_(u'internet connectivity?'))
    internet_provider = models.ForeignKey(Provider, related_name='internet_provider', verbose_name=_(u'internet provider'), blank=True, null=True)
    internet_costs = models.PositiveIntegerField(verbose_name=_(u'internet costs'), blank=True, null=True)
    uses_ogp_antenna = models.BooleanField(verbose_name=_(u'uses OGP antenna?'))
    uses_wifi = models.BooleanField(verbose_name=_(u'uses WIFI?'))
    wifi_provider = models.ForeignKey(Provider, related_name='wifi_provider', verbose_name=_(u'WIFI provider'), blank=True, null=True)
    wifi_costs = models.PositiveIntegerField(verbose_name=_(u'WIFI costs'), blank=True, null=True)
    internet_employees = models.BooleanField(verbose_name=_(u'internet employees?'))

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    @models.permalink
    def get_absolute_url(self):
        return ('equipment_view', [self.pk])

    class Meta:
        verbose_name = _(u'telecomm equipment')
        verbose_name_plural = _(u'telecomm equipment')
        ordering = ['label']
        unique_together = ['agency', 'label']


class Circuit(models.Model):
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    agency = models.ForeignKey(Agency, verbose_name=_(u'agency'))
    provider = models.ForeignKey(Provider, related_name='circuit_provider', verbose_name=_(u'provider'))
    purpose = models.CharField(max_length=128, verbose_name=_(u'purpose'))
    technology = models.ForeignKey(Technology, related_name='circuit_technology', verbose_name=_(u'technology'))
    bandwidth = models.PositiveIntegerField(max_length=128, verbose_name=_(u'bandwidth (in megabits)'), blank=True, null=True)
    unit_cost = models.PositiveIntegerField(verbose_name=_(u'unit cost'))
    units = models.PositiveIntegerField(default=1, verbose_name=_(u'units'))
    installation_cost = models.PositiveIntegerField(verbose_name=_(u'installation cost'))
    contract_start_date = models.DateField(verbose_name=_(u'contract start date'), null=True, blank=True)
    contract_end_date = models.DateField(verbose_name=_(u'contract end date'), null=True, blank=True)

    def __unicode__(self):
        return self.purpose

    #def natural_key(self):
    #    return (self.agency, self.purpose,)

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('equipment_view', [self.pk])

    class Meta:
        verbose_name = _(u'telecomm circuit')
        verbose_name_plural = _(u'telecomm circuit')
        ordering = ['purpose']
