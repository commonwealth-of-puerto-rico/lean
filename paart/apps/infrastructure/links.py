from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from agencies.permissions import PERMISSION_AGENCY_EDIT, PERMISSION_AGENCY_VIEW
from navigation.classes import Link

from .icons import (icon_projects, icon_project_edit, icon_project_delete,
    icon_project_view, icon_agency_projects, icon_project_create,
    icon_project_info_edit, icon_project_info_view, icon_project_info_delete,
    icon_project_budget_edit, icon_project_budget_view, icon_project_budget_delete,
    icon_project_details_edit, icon_project_details_view, icon_project_details_delete,
    icon_project_file_list, icon_project_file_upload, icon_project_file_delete,
    icon_project_file_download)
from .permissions import (PERMISSION_PROJECT_EDIT, PERMISSION_PROJECT_DELETE,
    PERMISSION_PROJECT_VIEW)

link_projects = Link(text=_(u'projects'), view='infrastructure_project_list', icon=icon_projects)

link_project_edit = Link(text=_(u'edit'), view='infrastructure_project_edit', args='resolved_object.pk', icon=icon_project_edit)
link_project_delete = Link(text=_(u'delete'), view='infrastructure_project_delete', args='resolved_object.pk', icon=icon_project_delete)
link_project_view = Link(text=_(u'view'), view='infrastructure_project_view', args='resolved_object.pk', icon=icon_project_view)
link_project_view_basic = Link(text=_(u'basic'), view='infrastructure_project_view', args='resolved_object.pk', icon=icon_project_view)
link_project_create = Link(text=_(u'add project'), view='infrastructure_project_create', args='agency.pk', icon=icon_project_create)

link_project_info_edit = Link(text=_(u'edit'), view='project_info_edit', args='resolved_object.pk', icon=icon_project_info_edit)
link_project_info_delete = Link(text=_(u'delete'), view='project_info_delete', args='resolved_object.pk', icon=icon_project_info_delete)
link_project_info_view = Link(text=_(u'information'), view='project_info_view', args='resolved_object.pk', icon=icon_project_info_view, children_view_regex=['project_info'])

link_project_budget_edit = Link(text=_(u'edit'), view='project_budget_edit', args='resolved_object.pk', icon=icon_project_budget_edit)
link_project_budget_delete = Link(text=_(u'delete'), view='project_budget_delete', args='resolved_object.pk', icon=icon_project_budget_delete)
link_project_budget_view = Link(text=_(u'budget'), view='project_budget_view', args='resolved_object.pk', icon=icon_project_budget_view, children_view_regex=['project_budget'])

link_project_details_edit = Link(text=_(u'edit'), view='project_details_edit', args='resolved_object.pk', icon=icon_project_details_edit)
link_project_details_delete = Link(text=_(u'delete'), view='project_details_delete', args='resolved_object.pk', icon=icon_project_details_delete)
link_project_details_view = Link(text=_(u'details'), view='project_details_view', args='resolved_object.pk', icon=icon_project_details_view, children_view_regex=['project_details'])

link_project_file_list = Link(text=_(u'files'), view='infrastructure_project_file_list', args='project.pk', icon=icon_project_file_list, children_view_regex=['project_file'])
link_project_file_upload = Link(text=_(u'upload file'), view='infrastructure_project_file_upload', args='project.pk', icon=icon_project_file_upload)
link_project_file_delete = Link(text=_(u'delete'), view='infrastructure_project_file_delete', args='resolved_object.pk', icon=icon_project_file_delete)
link_project_file_download = Link(text=_(u'download'), view='infrastructure_project_file_download', args='resolved_object.pk', icon=icon_project_file_download)

link_agency_project_list = Link(text=_(u'infrastructure'), view='agency_infrastructure_project_list', args='resolved_object.pk', icon=icon_agency_projects)
