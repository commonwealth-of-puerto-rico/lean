from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .icons import (icon_data_create, icon_data_edit, icon_data_delete,
    icon_data_view, icon_agency_data)
from .permissions import (PERMISSION_DATA_EDIT, PERMISSION_DATA_DELETE,
    PERMISSION_DATA_VIEW)

link_data_create = Link(text=_(u'add data'), view='data_create', args='agency.pk', icon=icon_data_create)#, permissions=[PERMISSION_EQUIPMENT_EDIT])
link_data_edit = Link(text=_(u'edit'), view='data_edit', args='resolved_object.pk', icon=icon_data_edit)#, permissions=[PERMISSION_EQUIPMENT_EDIT])
link_data_delete = Link(text=_(u'delete'), view='data_delete', args='resolved_object.pk', icon=icon_data_delete)#, permissions=[PERMISSION_EQUIPMENT_DELETE])
link_data_view = Link(text=_(u'view'), view='data_view', args='resolved_object.pk', icon=icon_data_view)#, permissions=[PERMISSION_EQUIPMENT_VIEW])
link_agency_data_list = Link(text=_(u'data'), view='agency_data_list', args='resolved_object.pk', icon=icon_agency_data)
