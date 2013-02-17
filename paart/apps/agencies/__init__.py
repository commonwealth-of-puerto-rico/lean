from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from common.utils import encapsulate
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link

from .links import (link_agency_list, link_agencies, link_agency_edit,
    link_agency_delete, link_agency_details)
from .models import Agency

Link.bind_links([Agency, 'agency_list'], [link_agency_list], menu_name='secondary_menu')
Link.bind_links([Agency], [link_agency_details, link_agency_edit, link_agency_delete])

register_model_list_columns(Agency, [
    {'name': _(u'registration'), 'attribute': 'registration'},
    {'name': _(u'name'), 'attribute': 'name'},
])

register_top_menu(
    'agencies',
    link=link_agencies,
    position=1
)
