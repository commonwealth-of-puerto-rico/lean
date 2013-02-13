from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from agencies.models import Agency
from common.utils import encapsulate
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link

from .links import link_project_list, link_projects, link_project_edit, link_project_delete, link_agency_project_list
from .models import Project

Link.bind_links(['project_list'], [link_project_list], menu_name='secondary_menu')
#Link.bind_links([Project, 'project_list', 'agency_project_list'], [link_project_list], menu_name='secondary_menu')
Link.bind_links([Project], [link_project_edit, link_project_delete])

Link.bind_links([Agency], [link_agency_project_list])

register_model_list_columns(Project, [
    {'name': _(u'name'), 'attribute': 'label'},
    {'name': _(u'fiscal year'), 'attribute': 'fiscal_year'},
    {'name': _(u'purpose'), 'attribute': 'purpose'},
    {'name': _(u'classification'), 'attribute': 'classification'},
])

register_model_list_columns(Agency, [
    {'name': _(u'projects'), 'attribute': encapsulate(lambda x: x.project_set.all().count())},
])

register_top_menu(
    'projects',
    link=link_projects,
    position=1
)
