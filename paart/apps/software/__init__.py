from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from acls.api import class_permissions
#from agencies.classes import AgencyElement
from agencies.models import Agency
from common.utils import encapsulate
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link

from .links import (link_agency_software_list, link_agency_software_create,
    link_agency_software_delete, link_agency_software_edit, link_agency_software_view)
from .models import Agency, AgencySoftware
from .permissions import (PERMISSION_AGENCY_SOFTWARE_CREATE, PERMISSION_AGENCY_SOFTWARE_DELETE,
    PERMISSION_AGENCY_SOFTWARE_EDIT, PERMISSION_AGENCY_SOFTWARE_VIEW)

Link.bind_links(['agency_software_list', 'data_create', AgencySoftware], [link_agency_software_create], menu_name='secondary_menu')
Link.bind_links([Agency], [link_agency_software_list])
Link.bind_links([AgencySoftware], [link_agency_software_view, link_agency_software_edit, link_agency_software_delete])

register_model_list_columns(AgencySoftware, [
    {'name': _(u'type'), 'attribute': 'software.software_type'},
    {'name': _(u'label'), 'attribute': 'software.label'},
    {'name': _(u'amount'), 'attribute': 'amount'},
])

#AgencyElement(link_agency_tools_profile_list)
class_permissions(Agency, [
        PERMISSION_AGENCY_SOFTWARE_CREATE, PERMISSION_AGENCY_SOFTWARE_DELETE,
        PERMISSION_AGENCY_SOFTWARE_EDIT, PERMISSION_AGENCY_SOFTWARE_VIEW
    ]
)
