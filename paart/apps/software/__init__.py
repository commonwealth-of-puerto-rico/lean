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

#Link.bind_links([ToolsProfile, 'agency_tools_profile_list', 'tools_profile_create'], [link_tools_profile_create], menu_name='secondary_menu')
Link.bind_links([Agency], [link_agency_software_list])

#Link.bind_links([ToolsProfile], [link_tools_profile_view, link_tools_profile_edit, link_tools_profile_delete])

#register_model_list_columns(ToolsProfile, [
#    {'name': _(u'creation date and time'), 'attribute': encapsulate(lambda x: x.datetime_created)},
#])

#AgencyElement(link_agency_tools_profile_list)
class_permissions(Agency, [
        PERMISSION_AGENCY_SOFTWARE_CREATE, PERMISSION_AGENCY_SOFTWARE_DELETE,
        PERMISSION_AGENCY_SOFTWARE_EDIT, PERMISSION_AGENCY_SOFTWARE_VIEW
    ]
)
