from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from agencies.models import Agency


class DataType(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'data type')
        verbose_name_plural = _(u'data types')
        ordering = ['label']


class AgencyData(models.Model):
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    agency = models.ForeignKey(Agency, verbose_name=_(u'agency'))
    label = models.CharField(max_length=128, verbose_name=_(u'label'))
    description = models.TextField(verbose_name=_(u'description'))
    data_type = models.ForeignKey(DataType, verbose_name=_(u'data type'))

    def __unicode__(self):
        return self.label

    @models.permalink
    def get_absolute_url(self):
        return ('data_view', [self.pk])

    class Meta:
        verbose_name = _(u'agency data')
        verbose_name_plural = _(u'agency data')
        ordering = ['label']
        unique_together = ['agency', 'label']
