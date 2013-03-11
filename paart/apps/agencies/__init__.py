from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from acls.api import class_permissions
from acls.permissions import ACLS_EDIT_ACL, ACLS_VIEW_ACL
from common.utils import encapsulate
from dynamic_search.classes import SearchModel
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link

from .links import (link_agency_list, link_agencies, link_agency_edit,
    link_agency_delete, link_agency_details, link_agency_view,
    link_agency_acl_details)
from .models import Agency
from .permissions import PERMISSION_AGENCY_VIEW, PERMISSION_AGENCY_EDIT


Link.bind_links([Agency, 'agency_list'], [link_agency_list], menu_name='secondary_menu')
#Link.bind_links([Agency], [link_agency_details, link_agency_view, link_agency_edit, link_agency_delete])
Link.bind_links([Agency], [link_agency_acl_details])#, link_agency_view, link_agency_edit])#, link_agency_delete])

register_model_list_columns(Agency, [
    #{'name': _(u'registration'), 'attribute': 'registration'},
    {'name': _(u'name'), 'attribute': 'name'},
])

register_top_menu(
    'agencies',
    link=link_agencies,
    position=1
)

class_permissions(Agency, [
    PERMISSION_AGENCY_VIEW, PERMISSION_AGENCY_EDIT,
    ACLS_VIEW_ACL, ACLS_EDIT_ACL,
    ]
)

agency_search = SearchModel('agencies', 'Agency')

agency_search.add_model_field('prifas', label=_(u'Prifas number'))
agency_search.add_model_field('registration', label=_(u'Registration'))
agency_search.add_model_field('name', label=_(u'Name'))
agency_search.add_model_field('director', label=_(u'Director'))
agency_search.add_model_field('physical_address', label=_(u'Physical address'))
agency_search.add_model_field('postal_address', label=_(u'Postal address'))
