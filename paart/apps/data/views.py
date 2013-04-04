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

from .forms import AgencyDataForm, AgencyDataForm_detail, AgencyDataForm_create
from .icons import icon_data_delete
from .models import AgencyData
from .permissions import (PERMISSION_DATA_CREATE, PERMISSION_DATA_VIEW,
    PERMISSION_DATA_EDIT, PERMISSION_DATA_DELETE)


def agency_data_list(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    pre_object_list = AgencyData.objects.filter(agency=agency)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_DATA_VIEW])
    except PermissionDenied:
        # If user doesn't have global permission, get a list of document
        # for which he/she does hace access use it to filter the
        # provided object_list
        final_object_list = AccessEntry.objects.filter_objects_by_access(PERMISSION_DATA_VIEW, request.user, pre_object_list, related='agency')
    else:
        final_object_list = pre_object_list

    context = {
        'object_list': final_object_list,
        'title': _(u'data of: %s') % agency,
        'hide_object': True,
        'object': agency,
        'agency': agency,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def data_edit(request, data_pk):
    data = get_object_or_404(AgencyData, pk=data_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_DATA_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_DATA_EDIT, request.user, data.agency)

    if request.method == 'POST':
        form = AgencyDataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Agency data "%s" edited successfully.') % data)

            return HttpResponseRedirect(data.get_absolute_url())
    else:
        form = AgencyDataForm(instance=data)

    return render_to_response('generic_form.html', {
        'form': form,
        'data': data,
        'object': data,
        'agency': data.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'data'},
        ],
    }, context_instance=RequestContext(request))


def data_delete(request, data_pk):
    data = get_object_or_404(AgencyData, pk=data_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_DATA_DELETE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_DATA_DELETE, request.user, data.agency)

    post_action_redirect = reverse('agency_data_list', args=[data.agency.pk])

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            data.delete()
            messages.success(request, _(u'Agency data: %s deleted successfully.') % data)
        except Exception, e:
            messages.error(request, _(u'Agency data: %(data)s delete error: %(error)s') % {
                'data': data, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'data'),
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you wish to delete the data: %s?') % data,
        'form_icon': icon_data_delete,
        'data': data,
        'agency': data.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'data'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def data_view(request, data_pk):
    data = get_object_or_404(AgencyData, pk=data_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_DATA_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_DATA_VIEW, request.user, data.agency)

    form = AgencyDataForm_detail(instance=data)

    return render_to_response('generic_detail.html', {
        'form': form,
        'data': data,
        'agency': data.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'data'},
        ],
    }, context_instance=RequestContext(request))


def data_create(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_DATA_CREATE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_DATA_CREATE, request.user, agency)

    if request.method == 'POST':
        form = AgencyDataForm_create(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.agency = agency
            data.save()
            messages.success(request, _(u'Agency data "%s" added successfully.') % data)
            return HttpResponseRedirect(reverse('agency_data_list', args=[agency.pk]))
    else:
        form = AgencyDataForm_create()

    return render_to_response('generic_form.html', {
        'form': form,
        'title': _(u'Add data to agency: %s') % agency,
        'object': agency,
        'agency': agency,
    }, context_instance=RequestContext(request))
