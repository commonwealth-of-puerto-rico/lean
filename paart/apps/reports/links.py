from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from agencies.permissions import PERMISSION_AGENCY_EDIT, PERMISSION_AGENCY_VIEW
from navigation.classes import Link

from .icons import (icon_project_reports_view)
from .permissions import (PERMISSION_PROJECT_VIEW)

link_project_reports_view = Link(text=_(u'reports'), view='agency_search_report', icon=icon_project_reports_view)
