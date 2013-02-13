from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from agencies.models import Agency
from common.utils import encapsulate
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link

from .links import link_project_list, link_projects, link_project_edit, link_project_delete, link_agency_project_list
from .models import Project

Link.bind_links([Project, 'project_list', 'agency_project_list'], [link_project_list], menu_name='secondary_menu')
Link.bind_links([Project], [link_project_edit, link_project_delete])

Link.bind_links([Agency], [link_agency_project_list])

#register_model_list_columns(Project, [
#    {'name': _(u'registration'), 'attribute': 'registration'},
#    {'name': _(u'name'), 'attribute': 'name'},
#])

register_top_menu(
    'projects',
    link=link_projects,
    position=1
)
