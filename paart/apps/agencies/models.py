from django.db import models
from django.utils.translation import ugettext_lazy as _


class Agency(models.Model):
    registration = models.PositiveIntegerField(verbose_name=_(u'registration'), unique=True)
    name = models.CharField(max_length=128, verbose_name=_(u'name'), unique=True)

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return (self.registration,)

    class Meta:
        verbose_name = _(u'agency')
        verbose_name_plural = _(u'agencies')
        ordering = ['name']
