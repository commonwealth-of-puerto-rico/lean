from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from acls.api import class_permissions
#from agencies.classes import AgencyElement
from common.utils import encapsulate
from dynamic_search.classes import SearchModel
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link

from .links import (link_project_reports_view)
# prime workflow permissions
from .permissions import (PERMISSION_PROJECT_VIEW)

#Link.bind_links(['project_reports_view'], [link_project_reports_view], menu_name='secondary_menu')

register_top_menu('link_project_reports_view',link=link_project_reports_view)
