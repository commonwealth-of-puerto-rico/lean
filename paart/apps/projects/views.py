from __future__ import absolute_import

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, resolve
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from agencies.models import Agency
from permissions.models import Permission

from .forms import ProjectForm, ProjectForm_step1, ProjectForm_step2
from .icons import icon_project_delete
from .models import Project
from .permissions import PERMISSION_PROJECT_EDIT, PERMISSION_PROJECT_DELETE
from .wizards import ProjectCreateWizard


def project_list(request):
    #try:
    #    Permission.objects.check_permissions(request.user, [PERMISSION_DOCUMENT_VIEW])
    #except PermissionDenied:
    #    # If user doesn't have global permission, get a list of document
    #    # for which he/she does hace access use it to filter the
    #    # provided object_list
    #    final_object_list = AccessEntry.objects.filter_objects_by_access(PERMISSION_DOCUMENT_VIEW, request.user, pre_object_list)
    #else:
    #    final_object_list = pre_object_list

    context = {
        'object_list': Project.objects.all(),
        'title': _(u'projects'),
        'hide_object': True,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def agency_project_list(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    #try:
    #    Permission.objects.check_permissions(request.user, [PERMISSION_DOCUMENT_VIEW])
    #except PermissionDenied:
    #    # If user doesn't have global permission, get a list of document
    #    # for which he/she does hace access use it to filter the
    #    # provided object_list
    #    final_object_list = AccessEntry.objects.filter_objects_by_access(PERMISSION_DOCUMENT_VIEW, request.user, pre_object_list)
    #else:
    #    final_object_list = pre_object_list

    context = {
        'object_list': agency.project_set.all(),
        'title': _(u'projects'),
        'hide_object': True,
        'object': agency,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def project_edit(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_EDIT, request.user, document)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Project "%s" edited successfully.') % project)

            return HttpResponseRedirect(reverse('project_list'))
    else:
        form = ProjectForm(instance=project)

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project,
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
        AccessEntry.objects.check_access(PERMISSION_PROJECT_DELETE, request.user, folder)

    #TODO: fix redirect
    post_action_redirect = reverse('project_list')

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            folder.delete()
            messages.success(request, _(u'Project: %s deleted successfully.') % project)
        except Exception, e:
            messages.error(request, _(u'Project: %(project)s delete error: %(error)s') % {
                'project': project, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'project'),
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you with to delete the project: %s?') % project,
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


def project_create_wizard(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    #Permission.objects.check_permissions(request.user, [PERMISSION_DOCUMENT_CREATE])

    wizard = ProjectCreateWizard(form_list=[ProjectForm_step1, ProjectForm_step2])

    return wizard(request)
