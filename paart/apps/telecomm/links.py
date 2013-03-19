from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .icons import (icon_circuit_create, icon_circuit_edit,
    icon_circuit_delete, icon_circuit_view, icon_agency_circuits,
    icon_equipment_create, icon_equipment_edit, icon_equipment_delete,
    icon_equipment_view, icon_agency_equipment)
from .permissions import (PERMISSION_CIRCUIT_EDIT, PERMISSION_CIRCUIT_DELETE,
    PERMISSION_CIRCUIT_VIEW, PERMISSION_EQUIPMENT_EDIT, PERMISSION_EQUIPMENT_DELETE,
    PERMISSION_EQUIPMENT_VIEW)

link_equipment_create = Link(text=_(u'add equipment'), view='equipment_create', args='agency.pk', icon=icon_equipment_create)#, permissions=[PERMISSION_EQUIPMENT_EDIT])
link_equipment_edit = Link(text=_(u'edit'), view='equipment_edit', args='resolved_object.pk', icon=icon_equipment_edit)#, permissions=[PERMISSION_EQUIPMENT_EDIT])
link_equipment_delete = Link(text=_(u'delete'), view='equipment_delete', args='resolved_object.pk', icon=icon_equipment_delete)#, permissions=[PERMISSION_EQUIPMENT_DELETE])
link_equipment_view = Link(text=_(u'view'), view='equipment_view', args='resolved_object.pk', icon=icon_equipment_view)#, permissions=[PERMISSION_EQUIPMENT_VIEW])
link_agency_equipment_list = Link(text=_(u'equipment'), view='agency_equipment_list', args='resolved_object.pk', icon=icon_agency_equipment)

link_circuit_create = Link(text=_(u'add circuit'), view='circuit_create', args='agency.pk', icon=icon_circuit_create)#, permissions=[PERMISSION_EQUIPMENT_EDIT])
link_circuit_edit = Link(text=_(u'edit'), view='circuit_edit', args='resolved_object.pk', icon=icon_circuit_edit)#, permissions=[PERMISSION_EQUIPMENT_EDIT])
link_circuit_delete = Link(text=_(u'delete'), view='circuit_delete', args='resolved_object.pk', icon=icon_circuit_delete)#, permissions=[PERMISSION_EQUIPMENT_DELETE])
link_circuit_view = Link(text=_(u'view'), view='circuit_view', args='resolved_object.pk', icon=icon_circuit_view)#, permissions=[PERMISSION_EQUIPMENT_VIEW])
link_agency_circuit_list = Link(text=_(u'circuits'), view='agency_circuit_list', args='resolved_object.pk', icon=icon_agency_circuits)
