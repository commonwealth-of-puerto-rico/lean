from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .icons import (icon_agencies, icon_agency_edit, icon_agency_delete,
    icon_agency_details, icon_agency_view, icon_agency_acls)
from .permissions import (PERMISSION_AGENCY_EDIT, PERMISSION_AGENCY_DELETE,
    PERMISSION_AGENCY_VIEW)

link_agency_list = Link(text=_(u'all agencies'), view='agency_list', icon=icon_agencies)
link_agencies = Link(text=_(u'agencies'), view='agency_list', icon=icon_agencies)
link_agency_edit = Link(text=_(u'edit'), view='agency_edit', args='resolved_object.pk', icon=icon_agency_edit, permissions=[PERMISSION_AGENCY_EDIT])
link_agency_delete = Link(text=_(u'delete'), view='agency_delete', args='resolved_object.pk', icon=icon_agency_delete, permissions=[PERMISSION_AGENCY_DELETE])
link_agency_details = Link(text=_(u'forms'), view='agency_details', args='resolved_object.pk', icon=icon_agency_details, permissions=[PERMISSION_AGENCY_VIEW])
link_agency_view = Link(text=_(u'view'), view='agency_view', args='resolved_object.pk', icon=icon_agency_view, permissions=[PERMISSION_AGENCY_VIEW])

link_agency_acl_details = Link(text=_(u'acls'), view='agency_acl_list', args='resolved_object.pk', icon=icon_agency_acls)#, permissions=[PERMISSION_AGENCY_ACLS_VIEW])
