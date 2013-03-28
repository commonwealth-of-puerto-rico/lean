from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from agencies.models import Agency


class SoftwareType(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'software type')
        verbose_name_plural = _(u'software types')
        ordering = ['label']


class Software(models.Model):
    software_type = models.ForeignKey(SoftwareType, verbose_name=_(u'software type'))
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)
    # TODO: Add enabled field

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'software')
        verbose_name_plural = _(u'software')
        ordering = ['label']


class AgencySoftware(models.Model):
    agency = models.ForeignKey(Agency, verbose_name=_(u'agency'))
    software = models.ForeignKey(Software, verbose_name=_(u'software'))
    amount = models.PositiveIntegerField(verbose_name=_(u'amount'), null=True, blank=True)

    def __unicode__(self):
        return unicode(self.software)

    def natural_key(self):
        return (self.datetime_created,)

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('tool_profile_view', [self.pk])

    class Meta:
        verbose_name = _(u'agency software')
        verbose_name_plural = _(u'agencies software')
        ordering = ['software']
