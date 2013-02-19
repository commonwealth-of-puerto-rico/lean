from django.utils.translation import ugettext_lazy as _

INFRASTRUCTURE_NEW = 'N'
INFRASTRUCTURE_OLD = 'O'

INFRASTRUCTURE_CHOICES = (
    (INFRASTRUCTURE_NEW, _(u'New')),
    (INFRASTRUCTURE_OLD, _(u'Existing')),
)

PRIORITY_1 = 1
PRIORITY_2 = 2
PRIORITY_3 = 3
PRIORITY_4 = 4
PRIORITY_5 = 5

PRIORITY_CHOICES = (
    (PRIORITY_1, _(u'Priority 1 (Very low)')),
    (PRIORITY_2, _(u'Priority 2 (Low)')),
    (PRIORITY_3, _(u'Priority 3 (Medium)')),
    (PRIORITY_4, _(u'Priority 4 (High)')),
    (PRIORITY_5, _(u'Priority 5 (Very high)')),
)
