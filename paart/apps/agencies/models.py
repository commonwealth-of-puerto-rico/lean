from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.managers import OmitDisabledManager


class Agency(models.Model):
    enabled = models.BooleanField(verbose_name=_(u'enabled'), default=True)
    registration = models.PositiveIntegerField(verbose_name=_(u'registration'), unique=True)
    name = models.CharField(max_length=128, verbose_name=_(u'name'), unique=True)
    director = models.CharField(max_length=128, verbose_name=_(u'director'), blank=True)
    physical_address = models.TextField(verbose_name=_(u'physical address'), blank=True)
    postal_address = models.TextField(verbose_name=_(u'postal address'), blank=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return (self.registration,)

    class Meta:
        verbose_name = _(u'agency')
        verbose_name_plural = _(u'agencies')
        ordering = ['name']
