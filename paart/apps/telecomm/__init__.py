from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from acls.api import class_permissions
#from agencies.classes import AgencyElement
from agencies.models import Agency
from common.utils import encapsulate
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link

from .links import (link_circuit_create, link_circuit_delete, link_circuit_edit,
    link_circuit_view, link_agency_circuit_list, link_equipment_create,
    link_equipment_delete, link_equipment_edit, link_equipment_view, link_agency_equipment_list)
from .models import Circuit, Equipment
from .permissions import (PERMISSION_CIRCUIT_CREATE, PERMISSION_CIRCUIT_DELETE,
    PERMISSION_CIRCUIT_EDIT, PERMISSION_CIRCUIT_VIEW, PERMISSION_EQUIPMENT_CREATE,
    PERMISSION_EQUIPMENT_DELETE, PERMISSION_EQUIPMENT_EDIT, PERMISSION_EQUIPMENT_VIEW)

#Link.bind_links(['equipment_list'], [link_equipment_list], menu_name='secondary_menu')
Link.bind_links(['agency_equipment_list', 'equipment_create', Equipment], [link_equipment_create], menu_name='secondary_menu')
Link.bind_links([Agency], [link_agency_equipment_list])
Link.bind_links([Equipment], [link_equipment_view, link_equipment_edit, link_equipment_delete])

Link.bind_links(['agency_circuit_list', 'circuit_create', Circuit], [link_circuit_create], menu_name='secondary_menu')
Link.bind_links([Agency], [link_agency_circuit_list])
Link.bind_links([Circuit], [link_circuit_view, link_circuit_edit, link_circuit_delete])

register_model_list_columns(Equipment, [
    {'name': _(u'name'), 'attribute': 'label'},
])

register_model_list_columns(Circuit, [
    {'name': _(u'purpose'), 'attribute': 'purpose'},
    {'name': _(u'provider'), 'attribute': 'provider'},
    {'name': _(u'technology'), 'attribute': 'technology'},
    {'name': _(u'bandwidth'), 'attribute': 'bandwidth'},
])

#AgencyElement(link_agency_equipment_list)

class_permissions(Agency, [
        PERMISSION_EQUIPMENT_CREATE, PERMISSION_EQUIPMENT_DELETE,
        PERMISSION_EQUIPMENT_EDIT, PERMISSION_EQUIPMENT_VIEW
    ]
)

class_permissions(Agency, [
        PERMISSION_CIRCUIT_CREATE, PERMISSION_CIRCUIT_DELETE,
        PERMISSION_CIRCUIT_EDIT, PERMISSION_CIRCUIT_VIEW
    ]
)
