from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .icons import (icon_projects, icon_project_edit, icon_project_delete,
    icon_agency_projects, icon_project_create_wizard)
from .permissions import PERMISSION_PROJECT_EDIT, PERMISSION_PROJECT_DELETE

#from .permissions import (PERMISSION_DOCUMENT_CREATE,

link_project_list = Link(text=_(u'all projects'), view='project_list', icon=icon_projects)
link_projects = Link(text=_(u'projects'), view='project_list', icon=icon_projects)
link_project_edit = Link(text=_(u'edit'), view='project_edit', args='resolved_object.pk', icon=icon_project_edit, permissions=[PERMISSION_PROJECT_EDIT])
link_project_delete = Link(text=_(u'delete'), view='project_delete', args='resolved_object.pk', icon=icon_project_delete, permissions=[PERMISSION_PROJECT_DELETE])
link_agency_project_list = Link(text=_(u'projects'), view='agency_project_list', args='resolved_object.pk', icon=icon_agency_projects)
link_project_create_wizard = Link(text=_(u'create project'), view='project_create_wizard', args='resolved_object.pk', icon=icon_project_create_wizard)
