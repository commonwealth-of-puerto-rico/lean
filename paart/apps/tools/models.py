from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from agencies.models import Agency


class Development(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'development tool')
        verbose_name_plural = _(u'development tools')
        ordering = ['label']


class Backup(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'backup tool')
        verbose_name_plural = _(u'backup tools')
        ordering = ['label']



class Firewall(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'firewall tool')
        verbose_name_plural = _(u'firewall tools')
        ordering = ['label']


class Antivirus(models.Model):
    label = models.CharField(max_length=128, verbose_name=_(u'label'), unique=True)

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.label,)

    class Meta:
        verbose_name = _(u'antivirus tool')
        verbose_name_plural = _(u'antivirus tools')
        ordering = ['label']


class ToolsProfile(models.Model):
    datetime_created = models.DateTimeField(editable=False, verbose_name=_(u'creation date and time'), default=lambda: now())
    agency = models.ForeignKey(Agency, verbose_name=_(u'agency'))
    development = models.ManyToManyField(Development, verbose_name=_(u'development tools'), blank=True, null=True)
    backup = models.ManyToManyField(Backup, verbose_name=_(u'backup tools'), blank=True, null=True)
    firewall = models.ManyToManyField(Firewall, verbose_name=_(u'firewall tools'), blank=True, null=True)
    antivirus = models.ManyToManyField(Antivirus, verbose_name=_(u'antivirus tools'), blank=True, null=True)
    notebooks = models.PositiveIntegerField(verbose_name=_(u'notebooks'), blank=True, null=True)
    desktops = models.PositiveIntegerField(verbose_name=_(u'desktops'), blank=True, null=True)
    servers = models.PositiveIntegerField(verbose_name=_(u'servers'), blank=True, null=True)

    def __unicode__(self):
        return unicode(self.datetime_created)

    def natural_key(self):
        return (self.datetime_created,)

    @models.permalink
    def get_absolute_url(self):
        return ('tool_profile_view', [self.pk])

    class Meta:
        verbose_name = _(u'tool profile')
        verbose_name_plural = _(u'tool profiles')
        ordering = ['agency']
