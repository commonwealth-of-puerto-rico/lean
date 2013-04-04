from __future__ import absolute_import

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, resolve
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from acls.models import AccessEntry
from agencies.models import Agency
from permissions.models import Permission

from .forms import AgencySoftwareForm_create, AgencySoftwareForm_edit, AgencySoftwareForm_detail
from .icons import icon_agency_software_delete
from .models import AgencySoftware
from .permissions import (PERMISSION_AGENCY_SOFTWARE_CREATE, PERMISSION_AGENCY_SOFTWARE_DELETE,
    PERMISSION_AGENCY_SOFTWARE_EDIT, PERMISSION_AGENCY_SOFTWARE_VIEW)


def agency_software_list(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    pre_object_list = AgencySoftware.objects.filter(agency=agency)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_SOFTWARE_VIEW])
    except PermissionDenied:
        # If user doesn't have global permission, get a list of document
        # for which he/she does hace access use it to filter the
        # provided object_list
        final_object_list = AccessEntry.objects.filter_objects_by_access(PERMISSION_AGENCY_SOFTWARE_VIEW, request.user, pre_object_list, related='agency')
    else:
        final_object_list = pre_object_list

    context = {
        'object_list': final_object_list,
        'title': _(u'software products of: %s') % agency,
        'hide_object': True,
        'object': agency,
        'agency': agency,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def agency_software_edit(request, agency_software_pk):
    agency_software = get_object_or_404(AgencySoftware, pk=agency_software_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_SOFTWARE_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_SOFTWARE_EDIT, request.user, document)

    if request.method == 'POST':
        form = AgencySoftwareForm_edit(request.POST, instance=agency_software)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'AgencySoftware "%s" edited successfully.') % agency_software)

            return HttpResponseRedirect(agency_software.get_absolute_url())
    else:
        form = AgencySoftwareForm_edit(instance=agency_software)

    return render_to_response('generic_form.html', {
        'form': form,
        'agency_software': agency_software,
        'object': agency_software,
        'agency': agency_software.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'agency_software'},
        ],
    }, context_instance=RequestContext(request))


def agency_software_delete(request, agency_software_pk):
    agency_software = get_object_or_404(AgencySoftware, pk=agency_software_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_SOFTWARE_DELETE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_SOFTWARE_DELETE, request.user, folder)

    post_action_redirect = reverse('agency_software_list', args=[agency_software.agency.pk])

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            agency_software.delete()
            messages.success(request, _(u'Agency software: %s deleted successfully.') % agency_software)
        except Exception, e:
            messages.error(request, _(u'Agency software: %(agency_software)s delete error: %(error)s') % {
                'agency_software': agency_software, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'agency_software'),
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you with to delete the agency software: %s?') % agency_software,
        'form_icon': icon_agency_software_delete,
        'agency_software': agency_software,
        'agency': agency_software.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'agency_software'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def agency_software_view(request, agency_software_pk):
    agency_software = get_object_or_404(AgencySoftware, pk=agency_software_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_SOFTWARE_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_SOFTWARE_VIEW, request.user, agency_software)

    form = AgencySoftwareForm_detail(instance=agency_software)

    return render_to_response('generic_detail.html', {
        'form': form,
        'agency_software': agency_software,
        'object': agency_software,
        'agency': agency_software.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'agency_software'},
        ],
    }, context_instance=RequestContext(request))


def agency_software_create(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_SOFTWARE_CREATE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_SOFTWARE_CREATE, request.user, agency)

    if request.method == 'POST':
        form = AgencySoftwareForm_create(request.POST)
        if form.is_valid():
            agency_software = form.save(commit=False)
            agency_software.agency = agency
            agency_software.save()
            form.save_m2m()
            messages.success(request, _(u'Agency software "%s" edited successfully.') % agency_software)

            return HttpResponseRedirect(reverse('agency_software_list', args=[agency.pk]))
    else:
        form = AgencySoftwareForm_create()

    return render_to_response('generic_form.html', {
        'form': form,
        'agency': agency,
        'navigation_object_list': [
            {'object': 'agency'},
        ],
        'title': _(u'Add software for agency: %s') % agency,
    }, context_instance=RequestContext(request))
