from __future__ import absolute_import

import mimetypes
import urllib

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.servers.basehttp import FileWrapper
from django.core.urlresolvers import reverse, resolve
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from acls.models import AccessEntry
from agencies.models import Agency
from permissions.models import Permission

from .forms import (ProjectForm_edit, ProjectForm_view, ProjectForm_create)
    #ProjectInfoForm_view, ProjectInfoForm_edit, ProjectInfoForm_create,
    #ProjectBudgetForm_view, ProjectBudgetForm_edit, ProjectBudgetForm_create,
    #ProjectDetailsForm_view, ProjectDetailsForm_edit, ProjectDetailsForm_create,
    #ProjectFileForm_create)
from .icons import (icon_project_delete, icon_project_info_delete,
    icon_project_budget_delete, icon_project_file_delete)
from .models import (Project, ProjectInfo, ProjectBudget, ProjectDetails, ProjectFile)
from .permissions import (PERMISSION_PROJECT_EDIT, PERMISSION_PROJECT_DELETE,
    PERMISSION_PROJECT_VIEW, PERMISSION_PROJECT_CREATE)


def agency_project_list(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    pre_object_list = agency.project_set.all()

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        # If user doesn't have global permission, get a list of document
        # for which he/she does hace access use it to filter the
        # provided object_list
        final_object_list = AccessEntry.objects.filter_objects_by_access(PERMISSION_PROJECT_VIEW, request.user, pre_object_list, related='agency')
    else:
        final_object_list = pre_object_list

    context = {
        'object_list': final_object_list,
        'title': _(u'projects of: %s') % agency,
        'hide_object': True,
        'object': agency,
        'agency': agency,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def project_create(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_CREATE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_CREATE, request.user, agency)

    if request.method == 'POST':
        form = ProjectForm_create(data=request.POST, initial={'agency': agency})
        if form.is_valid():
            try:
                project = form.save(commit=False)
                project.agency=agency
                project.save()
                messages.success(request, _(u'Project "%s" saved successfully.') % project)

                return HttpResponseRedirect(reverse('project_info_view', args=[project.pk]))
            except Exception as exception:
                messages.error(request, _(u'Unable to create project "%(project)s"; error: %(error)s.') % {
                    'project': project, 'error': exception}
                )
    else:
        form = ProjectForm_create(initial={'agency': agency})

    return render_to_response('generic_form.html', {
        'form': form,
        'object': agency,
        'agency': agency,
        'title': _(u'create project for agency: %s') % agency,
    }, context_instance=RequestContext(request))
