from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .icons import (icon_agency_software_create, icon_agency_software_delete,
    icon_agency_software_edit, icon_agency_software_view, icon_agency_software)
from .permissions import (PERMISSION_AGENCY_SOFTWARE_EDIT, PERMISSION_AGENCY_SOFTWARE_DELETE,
    PERMISSION_AGENCY_SOFTWARE_VIEW)

link_agency_software_create = Link(text=_(u'add software'), view='agency_software_create', args='agency.pk', icon=icon_agency_software_create)#, permissions=[PERMISSION_AGENCY_SOFTWARE_EDIT])
link_agency_software_delete = Link(text=_(u'delete'), view='agency_software_delete', args='resolved_object.pk', icon=icon_agency_software_delete)#, permissions=[PERMISSION_AGENCY_SOFTWARE_DELETE])
link_agency_software_edit = Link(text=_(u'edit'), view='agency_software_edit', args='resolved_object.pk', icon=icon_agency_software_edit)#, permissions=[PERMISSION_AGENCY_SOFTWARE_EDIT])
link_agency_software_view = Link(text=_(u'details'), view='agency_software_view', args='resolved_object.pk', icon=icon_agency_software_view)#, permissions=[PERMISSION_AGENCY_SOFTWARE_VIEW])
link_agency_software_list = Link(text=_(u'software'), view='agency_software_list', args='resolved_object.pk', icon=icon_agency_software)
