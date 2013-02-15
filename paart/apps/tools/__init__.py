from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from agencies.models import Agency
from common.utils import encapsulate
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link
"""
from .links import (link_equipment_edit, link_equipment_delete, link_equipment_view,
    link_agency_equipment_list)
from .models import Equipment

#Link.bind_links(['equipment_list'], [link_equipment_list], menu_name='secondary_menu')
Link.bind_links([Equipment], [link_equipment_view, link_equipment_edit, link_equipment_delete])

Link.bind_links([Agency], [link_agency_equipment_list])

register_model_list_columns(Equipment, [
    {'name': _(u'name'), 'attribute': 'label'},
])

#register_model_list_columns(Agency, [
#    {'name': _(u'equipment'), 'attribute': encapsulate(lambda x: x.equipment_set.all().count())},
#])
"""
