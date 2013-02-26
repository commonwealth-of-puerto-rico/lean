from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from acls.api import class_permissions
#from agencies.classes import AgencyElement
from agencies.models import Agency
from common.utils import encapsulate
from dynamic_search.classes import SearchModel
from navigation.api import register_top_menu, register_model_list_columns
from navigation.classes import Link
from workflows.models import WorkflowInstance

from .links import (link_projects, link_project_edit, link_project_view,
    link_project_delete, link_project_create, link_agency_project_list,
    link_project_info_view, link_project_info_edit, link_project_info_delete,
    link_project_budget_view, link_project_view_basic, link_project_budget_edit, link_project_budget_delete,
    link_project_details_view, link_project_details_edit, link_project_details_delete,
    link_project_opportunities_view, link_project_opportunities_edit, link_project_opportunities_delete,
    link_project_file_list, link_project_file_upload, link_project_file_delete, link_project_file_download,
    link_project_workflow_instance_list, link_project_workflow_instance_history_list,
    link_project_workflow_instance_action_submit)
from .models import (Project, ProjectInfo, ProjectBudget, ProjectDetails,
    ProjectOpportunities, ProjectFile)
# prime workflow permissions
from .permissions import PERMISSION_PROJECT_SUBMIT
from .permissions import (PERMISSION_PROJECT_EDIT, PERMISSION_PROJECT_DELETE,
        PERMISSION_PROJECT_VIEW, PERMISSION_PROJECT_CREATE)

Link.bind_links([Agency], [link_agency_project_list])

Link.bind_links(['agency_project_list', 'project_create'], [link_project_create], menu_name='sidebar')
Link.bind_links([Project], [link_project_view, link_project_edit, link_project_delete])
Link.bind_links([Project], [link_project_view_basic, link_project_info_view, link_project_budget_view, link_project_details_view, link_project_opportunities_view, link_project_file_list, link_project_workflow_instance_list], menu_name='form_header')

Link.bind_links([ProjectInfo], [link_project_info_edit, link_project_info_delete])
Link.bind_links([ProjectBudget], [link_project_budget_edit, link_project_budget_delete])
Link.bind_links([ProjectDetails], [link_project_details_edit, link_project_details_delete])
Link.bind_links([ProjectOpportunities], [link_project_opportunities_edit, link_project_opportunities_delete])
Link.bind_links([ProjectFile, 'project_file_upload', 'project_file_list'], [link_project_file_upload], menu_name='sidebar')
Link.bind_links([ProjectFile], [link_project_file_download, link_project_file_delete])

Link.bind_links([WorkflowInstance], [link_project_workflow_instance_history_list, link_project_workflow_instance_action_submit])

register_model_list_columns(Project, [
    {'name': _(u'name'), 'attribute': 'label'},
#    {'name': _(u'fiscal year'), 'attribute': 'fiscal_year'},
#    {'name': _(u'purpose'), 'attribute': 'purpose'},
#    {'name': _(u'classification'), 'attribute': 'classification'},
])

register_model_list_columns(ProjectFile, [
    {'name': _(u'label'), 'attribute': 'label'},
    {'name': _(u'file'), 'attribute': 'get_base_filename'},
])

#AgencyElement(link_agency_project_list)

class_permissions(Agency, [
        PERMISSION_PROJECT_EDIT, PERMISSION_PROJECT_DELETE,
        PERMISSION_PROJECT_VIEW, PERMISSION_PROJECT_CREATE
    ]
)

project_search = SearchModel('projects', 'Project')

project_search.add_model_field('label', label=_(u'label'))
project_search.add_model_field('agency__name', label=_(u'agency'))

project_search.add_model_field('projectinfo__fiscal_year__label', label=_(u'fiscal year'))
project_search.add_model_field('projectinfo__purpose__label', label=_(u'purpose'))
project_search.add_model_field('projectinfo__purpose_other', label=_(u'purpose other'))
project_search.add_model_field('projectinfo__classification__label', label=_(u'classification'))
project_search.add_model_field('projectinfo__classification_other', label=_(u'classification other'))
project_search.add_model_field('projectinfo__department__label', label=_(u'department'))
project_search.add_model_field('projectinfo__sponsor', label=_(u'sponsor'))
project_search.add_model_field('projectinfo__phone_number', label=_(u'phone number'))
project_search.add_model_field('projectinfo__goals', label=_(u'goals'))
project_search.add_model_field('projectinfo__needs', label=_(u'needs'))
project_search.add_model_field('projectinfo__expected_results', label=_(u'expected results'))
project_search.add_model_field('projectinfo__methodology', label=_(u'methodology'))
project_search.add_model_field('projectinfo__milestones', label=_(u'milestones'))

project_search.add_model_field('projectbudget__infrastructure', label=_(u'infrastructure'))
project_search.add_model_field('projectbudget__requirements', label=_(u'requirements'))
project_search.add_model_field('projectbudget__presumptions', label=_(u'presumptions'))
project_search.add_model_field('projectbudget__limitations', label=_(u'limitations'))
project_search.add_model_field('projectbudget__risks', label=_(u'risks'))
project_search.add_model_field('projectbudget__director', label=_(u'director'))

project_search.add_model_field('projectdetails__start_period__label', label=_(u'start period'))
project_search.add_model_field('projectdetails__end_period__label', label=_(u'end period'))
project_search.add_model_field('projectdetails__stage__label', label=_(u'stage'))
project_search.add_model_field('projectdetails__priority__label', label=_(u'priority'))

project_search.add_model_field('projectopportunities__opportunity__label', label=_(u'opportunity'))
project_search.add_model_field('projectopportunities__sharing_benefit__label', label=_(u'sharing benefit'))
project_search.add_model_field('projectopportunities__explanation', label=_(u'explanation'))
project_search.add_model_field('projectopportunities__other_agencies__name', label=_(u'other agencies'))

project_search.add_model_field('projectfile__label', label=_(u'project file label'))
project_search.add_model_field('projectfile__file', label=_(u'project file name'))
