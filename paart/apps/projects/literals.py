from django.utils.translation import ugettext_lazy as _

INFRASTRUCTURE_NEW = 'N'
INFRASTRUCTURE_OLD = 'O'

INFRASTRUCTURE_CHOICES = (
    (INFRASTRUCTURE_NEW, _(u'New')),
    (INFRASTRUCTURE_OLD, _(u'Existing')),
)
