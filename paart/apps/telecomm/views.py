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

from .forms import EquipmentForm, EquipmentForm_detail
from .icons import icon_equipment_delete
from .models import Equipment
from .permissions import (PERMISSION_EQUIPMENT_VIEW, PERMISSION_EQUIPMENT_EDIT,
    PERMISSION_EQUIPMENT_DELETE)


def agency_equipment_list(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    pre_object_list = agency.equipment_set.all()

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_EQUIPMENT_VIEW])
    except PermissionDenied:
        # If user doesn't have global permission, get a list of document
        # for which he/she does hace access use it to filter the
        # provided object_list
        final_object_list = AccessEntry.objects.filter_objects_by_access(PERMISSION_EQUIPMENT_VIEW, request.user, pre_object_list)
    else:
        final_object_list = pre_object_list

    context = {
        'object_list': final_object_list,
        'title': _(u'equipment'),
        'hide_object': True,
        'object': agency,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def equipment_edit(request, equipment_pk):
    equipment = get_object_or_404(Equipment, pk=equipment_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_EQUIPMENT_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_EQUIPMENT_EDIT, request.user, document)

    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Equipment "%s" edited successfully.') % equipment)

            return HttpResponseRedirect(equipment.get_absolute_url())
    else:
        form = EquipmentForm(instance=equipment)

    return render_to_response('generic_form.html', {
        'form': form,
        'equipment': equipment,
        'object': equipment,
        'agency': equipment.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'equipment'},
        ],
    }, context_instance=RequestContext(request))


def equipment_delete(request, equipment_pk):
    equipment = get_object_or_404(Equipment, pk=equipment_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_EQUIPMENT_DELETE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_EQUIPMENT_DELETE, request.user, folder)

    post_action_redirect = reverse('agency_equipment_list', args=[equipment.agency.pk])

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            folder.delete()
            messages.success(request, _(u'Equipment: %s deleted successfully.') % equipment)
        except Exception, e:
            messages.error(request, _(u'Equipment: %(equipment)s delete error: %(error)s') % {
                'equipment': equipment, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'equipment'),
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you with to delete the equipment: %s?') % equipment,
        'form_icon': icon_equipment_delete,
        'equipment': equipment,
        'agency': equipment.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'equipment'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def equipment_view(request, equipment_pk):
    equipment = get_object_or_404(Equipment, pk=equipment_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_EQUIPMENT_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_EQUIPMENT_VIEW, request.user, equipment)

    form = EquipmentForm_detail(instance=equipment)

    return render_to_response('generic_detail.html', {
        'form': form,
        'equipment': equipment,
        'agency': equipment.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'equipment'},
        ],
    }, context_instance=RequestContext(request))
