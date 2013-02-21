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

from agencies.models import Agency
from agencies.permissions import PERMISSION_AGENCY_EDIT, PERMISSION_AGENCY_VIEW
from permissions.models import Permission

from .forms import (ProjectForm_edit, ProjectForm_view, ProjectForm_create,
    ProjectInfoForm_view, ProjectInfoForm_edit, ProjectInfoForm_create,
    ProjectBudgetForm_view, ProjectBudgetForm_edit, ProjectBudgetForm_create,
    ProjectDetailsForm_view, ProjectDetailsForm_edit, ProjectDetailsForm_create,
    ProjectOpportunitiesForm_view, ProjectOpportunitiesForm_edit, ProjectOpportunitiesForm_create,
    ProjectFileForm_create)
from .icons import (icon_project_delete, icon_project_info_delete,
    icon_project_budget_delete, icon_project_details_delete, icon_project_opportunities_delete,
    icon_project_file_delete)
from .models import (Project, ProjectInfo, ProjectBudget, ProjectDetails,
    ProjectOpportunities, ProjectFile)
from .permissions import (PERMISSION_PROJECT_EDIT, PERMISSION_PROJECT_DELETE,
    PERMISSION_PROJECT_VIEW, PERMISSION_PROJECT_CREATE)
from .wizards import ProjectCreateWizard


def agency_project_list(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    pre_object_list = agency.project_set.all()

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        # If user doesn't have global permission, get a list of document
        # for which he/she does hace access use it to filter the
        # provided object_list
        final_object_list = AccessEntry.objects.filter_objects_by_access(PERMISSION_PROJECT_VIEW, request.user, pre_object_list)
    else:
        final_object_list = pre_object_list

    context = {
        'object_list': final_object_list,
        'title': _(u'projects'),
        'hide_object': True,
        'object': agency,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def project_edit(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project.agency)

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
        'title': _(u'edit project: %s') % project,
        'agency': project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_delete(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project.agency)

    post_action_redirect = reverse('agency_project_list', args=[project.agency.pk])

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


def project_view(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_VIEW, request.user, project.agency)

    form = ProjectForm_view(instance=project)

    return render_to_response('generic_detail.html', {
        'form': form,
        'agency': project.agency,
        'project': project,
        'title': _(u'project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_create(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, agency)

    if request.method == 'POST':
        form = ProjectForm_create(data=request.POST, initial={'agency': agency})
        if form.is_valid():
            project = form.save(commit=False)
            project.agency=agency
            project.save()
            messages.success(request, _(u'Project "%s" saved successfully.') % project)

            return HttpResponseRedirect(project.get_absolute_url())
    else:
        form = ProjectForm_create(initial={'agency': agency})

    return render_to_response('generic_form.html', {
        'form': form,
        'object': agency,
        'title': _(u'create project for agency: %s') % agency,
    }, context_instance=RequestContext(request))


"""
def project_create_wizard(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_CREATE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_CREATE, request.user, agency)

    wizard = ProjectCreateWizard.as_view(
        form_list=[ProjectForm_step1, ProjectForm_step2, ProjectForm_step3, ProjectForm_step4],
        step_titles=[
            _(u'General information'),
            _(u'Budget'),
            _(u'Equipment'),
            _(u'Timeframe'),
        ],
        view_extra_context={
            'object': agency,
        },
        agency=agency,
        model=Project
    )
    return wizard(request)
"""


def project_info_view(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_VIEW, request.user, project)

    try:
        project_info = project.projectinfo
    except ProjectInfo.DoesNotExist:
        return HttpResponseRedirect(reverse('project_info_create', args=[project.pk]))
    else:
        form = ProjectInfoForm_view(instance=project.projectinfo)

    return render_to_response('generic_detail.html', {
        'form': form,
        'agency': project.agency,
        'project': project,
        'project_info': project_info,
        'title': _(u'information for project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_info'},
        ],
    }, context_instance=RequestContext(request))


def project_info_edit(request, project_info_pk):
    project_info = get_object_or_404(ProjectInfo, pk=project_info_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_info.project.agency)

    if request.method == 'POST':
        form = ProjectInfoForm_edit(request.POST, instance=project_info)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Information for project "%s" edited successfully.') % project_info.project)

            return HttpResponseRedirect(project_info.get_absolute_url())
    else:
        form = ProjectInfoForm_edit(instance=project_info)

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project_info.project,
        'project_info': project_info,
        'agency': project_info.project.agency,
        'title': _('edit information for project: %s') % project_info.project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_info'},
        ],
    }, context_instance=RequestContext(request))


def project_info_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project.agency)

    if request.method == 'POST':
        form = ProjectInfoForm_create(request.POST, initial={'project': project})
        if form.is_valid():
            project_info = form.save(commit=False)
            project_info.project = project
            project_info.save()
            messages.success(request, _(u'Details for project "%s" saved successfully.') % project)

            return HttpResponseRedirect(project_info.get_absolute_url())
    else:
        form = ProjectInfoForm_create(initial={'project': project})

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project,
        'agency': project.agency,
        'title': _(u'enter information for project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_info_delete(request, project_info_pk):
    project_info = get_object_or_404(ProjectInfo, pk=project_info_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_info.project.agency)

    post_action_redirect = project_info.project.get_absolute_url()

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            project_info.delete()
            messages.success(request, _(u'Information for project: %s, deleted successfully.') % project_info.project)
        except Exception, e:
            messages.error(request, _(u'Information for project: %(project)s delete error: %(error)s') % {
                'project': project_info.project, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you with to delete the information for project: %s?') % project_info.project,
        'form_icon': icon_project_info_delete,
        'project': project_info.project,
        'project_info': project_info,
        'agency': project_info.project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_info'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))

### Budget

def project_budget_view(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_VIEW, request.user, project)

    try:
        project_budget = project.projectbudget
    except ProjectBudget.DoesNotExist:
        return HttpResponseRedirect(reverse('project_budget_create', args=[project.pk]))
    else:
        form = ProjectBudgetForm_view(instance=project.projectbudget)

    return render_to_response('generic_detail.html', {
        'form': form,
        'agency': project.agency,
        'project': project,
        'project_budget': project_budget,
        'title': _(u'budget for project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_budget'},
        ],
    }, context_instance=RequestContext(request))


def project_budget_edit(request, project_budget_pk):
    project_budget = get_object_or_404(ProjectBudget, pk=project_budget_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_budget.project.agency)

    if request.method == 'POST':
        form = ProjectBudgetForm_edit(request.POST, instance=project_budget)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Budget for project "%s" edited successfully.') % project_budget.project)

            return HttpResponseRedirect(project_budget.get_absolute_url())
    else:
        form = ProjectBudgetForm_edit(instance=project_budget)

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project_budget.project,
        'project_budget': project_budget,
        'agency': project_budget.project.agency,
        'title': _('edit budget for project: %s') % project_budget.project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_budget'},
        ],
    }, context_instance=RequestContext(request))


def project_budget_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project.agency)

    if request.method == 'POST':
        form = ProjectBudgetForm_create(request.POST, initial={'project': project})
        if form.is_valid():
            project_budget = form.save(commit=False)
            project_budget.project = project
            project_budget.save()
            messages.success(request, _(u'Details for project "%s" saved successfully.') % project)

            return HttpResponseRedirect(project_budget.get_absolute_url())
    else:
        form = ProjectBudgetForm_create(initial={'project': project})

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project,
        'agency': project.agency,
        'title': _(u'enter budget for project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_budget_delete(request, project_budget_pk):
    project_budget = get_object_or_404(ProjectBudget, pk=project_budget_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_budget.project.agency)

    post_action_redirect = project_budget.project.get_absolute_url()

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            project_budget.delete()
            messages.success(request, _(u'Budget for project: %s, deleted successfully.') % project_budget.project)
        except Exception, e:
            messages.error(request, _(u'Budget for project: %(project)s delete error: %(error)s') % {
                'project': project_budget.project, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you with to delete the budget for project: %s?') % project_budget.project,
        'form_icon': icon_project_budget_delete,
        'project': project_budget.project,
        'project_budget': project_budget,
        'agency': project_budget.project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_budget'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


### Details

def project_details_view(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_VIEW, request.user, project)

    try:
        project_details = project.projectdetails
    except ProjectDetails.DoesNotExist:
        return HttpResponseRedirect(reverse('project_details_create', args=[project.pk]))
    else:
        form = ProjectDetailsForm_view(instance=project.projectdetails)

    return render_to_response('generic_detail.html', {
        'form': form,
        'agency': project.agency,
        'project': project,
        'project_details': project_details,
        'title': _(u'details for project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_details'},
        ],
    }, context_instance=RequestContext(request))


def project_details_edit(request, project_details_pk):
    project_details = get_object_or_404(ProjectDetails, pk=project_details_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_details.project.agency)

    if request.method == 'POST':
        form = ProjectDetailsForm_edit(request.POST, instance=project_details)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Details for project "%s" edited successfully.') % project_details.project)

            return HttpResponseRedirect(project_details.get_absolute_url())
    else:
        form = ProjectDetailsForm_edit(instance=project_details)

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project_details.project,
        'project_details': project_details,
        'agency': project_details.project.agency,
        'title': _('edit details for project: %s') % project_details.project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_details'},
        ],
    }, context_instance=RequestContext(request))


def project_details_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project.agency)

    if request.method == 'POST':
        form = ProjectDetailsForm_create(request.POST, initial={'project': project})
        if form.is_valid():
            project_details = form.save(commit=False)
            project_details.project = project
            project_details.save()
            messages.success(request, _(u'Details for project "%s" saved successfully.') % project)

            return HttpResponseRedirect(project_details.get_absolute_url())
    else:
        form = ProjectDetailsForm_create(initial={'project': project})

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project,
        'agency': project.agency,
        'title': _(u'enter details for project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_details_delete(request, project_details_pk):
    project_details = get_object_or_404(ProjectDetails, pk=project_details_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_details.project.agency)

    post_action_redirect = project_details.project.get_absolute_url()

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            project_details.delete()
            messages.success(request, _(u'Details for project: %s, deleted successfully.') % project_details.project)
        except Exception, e:
            messages.error(request, _(u'Details for project: %(project)s delete error: %(error)s') % {
                'project': project_details.project, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you with to delete the details for project: %s?') % project_details.project,
        'form_icon': icon_project_details_delete,
        'project': project_details.project,
        'project_details': project_details,
        'agency': project_details.project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_details'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


## Opportunities

def project_opportunities_view(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_VIEW, request.user, project)

    try:
        project_opportunities = project.projectopportunities
    except ProjectOpportunities.DoesNotExist:
        return HttpResponseRedirect(reverse('project_opportunities_create', args=[project.pk]))
    else:
        form = ProjectOpportunitiesForm_view(instance=project.projectopportunities)

    return render_to_response('generic_detail.html', {
        'form': form,
        'agency': project.agency,
        'project': project,
        'project_opportunities': project_opportunities,
        'title': _(u'opportunities for project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_opportunities'},
        ],
    }, context_instance=RequestContext(request))


def project_opportunities_edit(request, project_opportunities_pk):
    project_opportunities = get_object_or_404(ProjectOpportunities, pk=project_opportunities_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_opportunities.project.agency)

    if request.method == 'POST':
        form = ProjectOpportunitiesForm_edit(request.POST, instance=project_opportunities)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Opportunities for project "%s" edited successfully.') % project_opportunities.project)

            return HttpResponseRedirect(project_opportunities.get_absolute_url())
    else:
        form = ProjectOpportunitiesForm_edit(instance=project_opportunities)

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project_opportunities.project,
        'project_opportunities': project_opportunities,
        'agency': project_opportunities.project.agency,
        'title': _('edit opportunities for project: %s') % project_opportunities.project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_opportunities'},
        ],
    }, context_instance=RequestContext(request))


def project_opportunities_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project.agency)

    if request.method == 'POST':
        form = ProjectOpportunitiesForm_create(request.POST, initial={'project': project})
        if form.is_valid():
            project_opportunities = form.save(commit=False)
            project_opportunities.project = project
            project_opportunities.save()
            messages.success(request, _(u'Opportunities for project "%s" saved successfully.') % project)

            return HttpResponseRedirect(project_opportunities.get_absolute_url())
    else:
        form = ProjectOpportunitiesForm_create(initial={'project': project})

    return render_to_response('generic_form.html', {
        'form': form,
        'project': project,
        'agency': project.agency,
        'title': _(u'enter opportunities for project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_opportunities_delete(request, project_opportunities_pk):
    project_opportunities = get_object_or_404(ProjectOpportunities, pk=project_opportunities_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_opportunities.project.agency)

    post_action_redirect = project_opportunities.project.get_absolute_url()

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            project_opportunities.delete()
            messages.success(request, _(u'Opportunities for project: %s, deleted successfully.') % project_opportunities.project)
        except Exception, e:
            messages.error(request, _(u'Opportunities for project: %(project)s delete error: %(error)s') % {
                'project': project_opportunities.project, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you with to delete the opportunities for project: %s?') % project_opportunities.project,
        'form_icon': icon_project_opportunities_delete,
        'project': project_opportunities.project,
        'project_opportunities': project_opportunities,
        'agency': project_opportunities.project.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
            {'object': 'project_opportunities'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def project_file_list(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_VIEW, request.user, project.agency)

    context = {
        'object_list': project.projectfile_set.all(),
        'title': _(u'project files'),
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
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project.agency)

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
        'title': _(u'upload file for project: %s') % project,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'project'},
        ],
    }, context_instance=RequestContext(request))


def project_file_delete(request, project_file_pk):
    project_file = get_object_or_404(ProjectFile, pk=project_file_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_file.project.agency)

    post_action_redirect = reverse('project_file_list', args=[project_file.project.pk])

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
        'title': _(u'Are you sure you with to delete the project file: %s?') % project_file,
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
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, project_file.project.agency)

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
