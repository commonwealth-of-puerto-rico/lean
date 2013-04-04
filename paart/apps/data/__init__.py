from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from acls.api import class_permissions
#from agencies.classes import AgencyElement
from agencies.models import Agency
from common.utils import encapsulate
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link

from .links import (link_data_create, link_data_delete, link_data_edit,
    link_data_view, link_agency_data_list)
from .models import AgencyData
from .permissions import (PERMISSION_DATA_CREATE, PERMISSION_DATA_DELETE,
    PERMISSION_DATA_EDIT, PERMISSION_DATA_VIEW)

#Link.bind_links(['data_list'], [link_data_list], menu_name='secondary_menu')
Link.bind_links(['agency_data_list', 'data_create', AgencyData], [link_data_create], menu_name='secondary_menu')
Link.bind_links([Agency], [link_agency_data_list])
Link.bind_links([AgencyData], [link_data_view, link_data_edit, link_data_delete])

register_model_list_columns(AgencyData, [
    {'name': _(u'name'), 'attribute': 'label'},
    {'name': _(u'data type'), 'attribute': 'data_type'},
    {'name': _(u'description'), 'attribute': 'description'},
])

#AgencyElement(link_agency_data_list)
class_permissions(Agency, [
        PERMISSION_DATA_CREATE, PERMISSION_DATA_DELETE,
        PERMISSION_DATA_EDIT, PERMISSION_DATA_VIEW
    ]
)
