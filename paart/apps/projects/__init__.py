from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from agencies.classes import AgencyElement
from common.utils import encapsulate
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link

from .links import (link_projects, link_project_edit, link_project_view,
    link_project_delete, link_project_create, link_agency_project_list,
    link_project_info_view, link_project_info_edit, link_project_info_delete)
from .models import Project, ProjectInfo

Link.bind_links(['agency_project_list', 'project_create'], [link_project_create], menu_name='sidebar')
Link.bind_links([Project], [link_project_edit, link_project_delete])
Link.bind_links([Project], [link_project_view], menu_name='form_header')
Link.bind_links([Project], [link_project_info_view], menu_name='form_header')

Link.bind_links([ProjectInfo], [link_project_info_edit, link_project_info_delete])

#register_model_list_columns(Project, [
#    {'name': _(u'name'), 'attribute': 'label'},
#    {'name': _(u'fiscal year'), 'attribute': 'fiscal_year'},
#    {'name': _(u'purpose'), 'attribute': 'purpose'},
#    {'name': _(u'classification'), 'attribute': 'classification'},
#])

AgencyElement(link_agency_project_list)
