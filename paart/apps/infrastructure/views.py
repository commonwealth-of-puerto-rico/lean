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

from .forms import (ProjectFileForm_create, ProjectForm_edit, ProjectForm_view, ProjectForm_create)
    #ProjectInfoForm_view, ProjectInfoForm_edit, ProjectInfoForm_create,
    #ProjectBudgetForm_view, ProjectBudgetForm_edit, ProjectBudgetForm_create,
    #ProjectDetailsForm_view, ProjectDetailsForm_edit, ProjectDetailsForm_create,
    #ProjectFileForm_create)
from .icons import (icon_project_delete, icon_project_info_delete,
    icon_project_budget_delete, icon_project_file_delete)
from .models import (Project, ProjectInfo, ProjectBudget, ProjectFile)
from .permissions import (PERMISSION_PROJECT_EDIT, PERMISSION_PROJECT_DELETE,
    PERMISSION_PROJECT_VIEW, PERMISSION_PROJECT_CREATE)


def agency_project_list(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    pre_object_list = Project.objects.filter(agency=agency)

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
        'title': _(u'infrastructure projects of: %s') % agency,
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

                return HttpResponseRedirect(reverse('infrastructure_project_info_view', args=[project.pk]))
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
        'title': _(u'create infrastructure project for agency: %s') % agency,
    }, context_instance=RequestContext(request))


def project_view(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_VIEW, request.user, project.agency)

    form = ProjectForm_view(instance=project)

    return render_to_response('generic_detail.html', {
        'form': form,
        'agency': project.agency,
        'project': project,
        'title': _(u'infrastructure project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_edit(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_EDIT, request.user, project.agency)

    if request.method == 'POST':
        form = ProjectForm_edit(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Project "%s" edited successfully.') % project)

            return HttpResponseRedirect(project.get_absolute_url())
    else:
        form = ProjectForm_edit(instance=project)

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project,
        'title': _(u'edit infrastructure project: %s') % project,
        'agency': project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_delete(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_DELETE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_DELETE, request.user, project.agency)

    post_action_redirect = reverse('agency_infrastructure_project_list', args=[project.agency.pk])

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            project.delete()
            messages.success(request, _(u'Project: %s deleted successfully.') % project)
        except Exception, e:
            messages.error(request, _(u'Project: %(project)s delete error: %(error)s') % {
                'project': project, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'infrastructure project'),
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you wish to delete the infrastructure project: %s?') % project,
        'form_icon': icon_project_delete,
        'project': project,
        'agency': project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


# Project files


def project_file_list(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_VIEW, request.user, project.agency)

    context = {
        'object_list': project.projectfile_set.all(),
        'title': _(u'infrastructure project files'),
        'project': project,
        'hide_object': True,
        'agency': project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def project_file_upload(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_EDIT, request.user, project.agency)

    if request.method == 'POST':
        form = ProjectFileForm_create(data=request.POST, files=request.FILES, initial={'project': project})
        if form.is_valid():
            project_file = form.save(commit=False)
            project_file.project = project
            project_file.save()
            messages.success(request, _(u'File for project "%s" uploaded successfully.') % project)

            return HttpResponseRedirect(project_file.get_absolute_url())
    else:
        form = ProjectFileForm_create(initial={'project': project})

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project,
        'agency': project.agency,
        'title': _(u'upload file for infrastructure project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_file_delete(request, project_file_pk):
    project_file = get_object_or_404(ProjectFile, pk=project_file_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_EDIT, request.user, project_file.project.agency)

    post_action_redirect = reverse('infrastructure_project_file_list', args=[project_file.project.pk])

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            project_file.file.delete()
            project_file.delete()
            messages.success(request, _(u'Project file: %s, deleted successfully.') % project_file)
        except Exception, e:
            messages.error(request, _(u'Project file: %(project)s delete error: %(error)s') % {
                'project': project_file, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you wish to delete the infrastructure project file: %s?') % project_file,
        'form_icon': icon_project_file_delete,
        'project': project_file.project,
        'project_file': project_file,
        'agency': project_file.project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_file'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def project_file_download(request, project_file_pk):
    project_file = get_object_or_404(ProjectFile, pk=project_file_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_VIEW, request.user, project_file.project.agency)

    filename = project_file.file.name
    wrapper = FileWrapper(project_file.file)
    mime_type, encoding = mimetypes.guess_type(filename)
    if mime_type is None:
        mime_type = 'application/octet-stream'

    response = HttpResponse(wrapper, content_type=mime_type)
    response['Content-Length'] = project_file.file.size
    if encoding is not None:
        response['Content-Encoding'] = encoding

    # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
    if u'WebKit' in request.META['HTTP_USER_AGENT']:
        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
        filename_header = 'filename=%s' % filename.encode('utf-8')
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        # IE does not support internationalized filename at all.
        # It can only recognize internationalized URL, so we do the trick via routing rules.
        filename_header = ''
    else:
        # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
        filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(filename.encode('utf-8'))
    response['Content-Disposition'] = 'attachment; ' + filename_header

    return response
