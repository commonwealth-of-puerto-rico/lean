from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .icons import (icon_equipment_create, icon_equipment_edit,
    icon_equipment_delete, icon_equipment_view, icon_agency_equipment)
from .permissions import (PERMISSION_EQUIPMENT_EDIT, PERMISSION_EQUIPMENT_DELETE,
    PERMISSION_EQUIPMENT_VIEW)

link_equipment_create = Link(text=_(u'add equipment'), view='equipment_create', args='resolved_object.pk', icon=icon_equipment_create)#, permissions=[PERMISSION_EQUIPMENT_EDIT])
link_equipment_edit = Link(text=_(u'edit'), view='equipment_edit', args='resolved_object.pk', icon=icon_equipment_edit)#, permissions=[PERMISSION_EQUIPMENT_EDIT])
link_equipment_delete = Link(text=_(u'delete'), view='equipment_delete', args='resolved_object.pk', icon=icon_equipment_delete)#, permissions=[PERMISSION_EQUIPMENT_DELETE])
link_equipment_view = Link(text=_(u'view'), view='equipment_view', args='resolved_object.pk', icon=icon_equipment_view)#, permissions=[PERMISSION_EQUIPMENT_VIEW])
link_agency_equipment_list = Link(text=_(u'equipment'), view='agency_equipment_list', args='resolved_object.pk', icon=icon_agency_equipment)

