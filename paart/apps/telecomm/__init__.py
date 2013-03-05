from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

#from agencies.classes import AgencyElement
from agencies.models import Agency
from common.utils import encapsulate
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link

from .links import (link_equipment_create, link_equipment_delete, link_equipment_edit,
    link_equipment_view, link_agency_equipment_list)
from .models import Equipment

#Link.bind_links(['equipment_list'], [link_equipment_list], menu_name='secondary_menu')
Link.bind_links(['agency_equipment_list', 'equipment_create', Equipment], [link_equipment_create], menu_name='sidebar')
Link.bind_links([Agency], [link_agency_equipment_list])
Link.bind_links([Equipment], [link_equipment_view, link_equipment_edit, link_equipment_delete])

register_model_list_columns(Equipment, [
    {'name': _(u'name'), 'attribute': 'label'},
])

#AgencyElement(link_agency_equipment_list)
