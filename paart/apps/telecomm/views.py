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

from .forms import (CircuitForm, CircuitForm_detail, CircuitForm_create,
    EquipmentForm, EquipmentForm_detail, EquipmentForm_create)
from .icons import icon_circuit_delete, icon_equipment_delete
from .models import Circuit, Equipment
from .permissions import (PERMISSION_CIRCUIT_CREATE, PERMISSION_CIRCUIT_VIEW,
    PERMISSION_CIRCUIT_EDIT, PERMISSION_CIRCUIT_DELETE, PERMISSION_EQUIPMENT_CREATE,
    PERMISSION_EQUIPMENT_VIEW, PERMISSION_EQUIPMENT_EDIT, PERMISSION_EQUIPMENT_DELETE)


def agency_equipment_list(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    pre_object_list = agency.equipment_set.all()

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_EQUIPMENT_VIEW])
    except PermissionDenied:
        # If user doesn't have global permission, get a list of document
        # for which he/she does hace access use it to filter the
        # provided object_list
        final_object_list = AccessEntry.objects.filter_objects_by_access(PERMISSION_EQUIPMENT_VIEW, request.user, pre_object_list, related='agency')
    else:
        final_object_list = pre_object_list

    context = {
        'object_list': final_object_list,
        'title': _(u'equipment of: %s') % agency,
        'hide_object': True,
        'object': agency,
        'agency': agency,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def equipment_edit(request, equipment_pk):
    equipment = get_object_or_404(Equipment, pk=equipment_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_EQUIPMENT_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_EQUIPMENT_EDIT, request.user, equipment.agency)

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
        AccessEntry.objects.check_access(PERMISSION_EQUIPMENT_DELETE, request.user, equipment.agency)

    post_action_redirect = reverse('agency_equipment_list', args=[equipment.agency.pk])

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            equipment.delete()
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
        'title': _(u'Are you sure you wish to delete the equipment: %s?') % equipment,
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
        AccessEntry.objects.check_access(PERMISSION_EQUIPMENT_VIEW, request.user, equipment.agency)

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


def equipment_create(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_EQUIPMENT_CREATE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_EQUIPMENT_CREATE, request.user, agency)

    if request.method == 'POST':
        form = EquipmentForm_create(request.POST)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.agency = agency
            equipment.save()
            messages.success(request, _(u'Equipment "%s" added successfully.') % equipment)
            return HttpResponseRedirect(reverse('agency_equipment_list', args=[agency.pk]))
    else:
        form = EquipmentForm_create()

    return render_to_response('generic_form.html', {
        'form': form,
        'title': _(u'Add equipment to agency: %s') % agency,
        'object': agency,
        'agency': agency,
    }, context_instance=RequestContext(request))


# Circuits

def agency_circuit_list(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    pre_object_list = agency.circuit_set.all()

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_CIRCUIT_VIEW])
    except PermissionDenied:
        # If user doesn't have global permission, get a list of document
        # for which he/she does hace access use it to filter the
        # provided object_list
        final_object_list = AccessEntry.objects.filter_objects_by_access(PERMISSION_CIRCUIT_VIEW, request.user, pre_object_list, related='agency')
    else:
        final_object_list = pre_object_list

    context = {
        'object_list': final_object_list,
        'title': _(u'circuit of: %s') % agency,
        'hide_object': True,
        'object': agency,
        'agency': agency,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def circuit_edit(request, circuit_pk):
    circuit = get_object_or_404(Circuit, pk=circuit_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_CIRCUIT_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_CIRCUIT_EDIT, request.user, circuit.agency)

    if request.method == 'POST':
        form = CircuitForm(request.POST, instance=circuit)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Circuit "%s" edited successfully.') % circuit)

            return HttpResponseRedirect(circuit.get_absolute_url())
    else:
        form = CircuitForm(instance=circuit)

    return render_to_response('generic_form.html', {
        'form': form,
        'circuit': circuit,
        'object': circuit,
        'agency': circuit.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'circuit'},
        ],
    }, context_instance=RequestContext(request))


def circuit_delete(request, circuit_pk):
    circuit = get_object_or_404(Circuit, pk=circuit_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_CIRCUIT_DELETE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_CIRCUIT_DELETE, request.user, circuit.agency)

    post_action_redirect = reverse('agency_circuit_list', args=[circuit.agency.pk])

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            circuit.delete()
            messages.success(request, _(u'Circuit: %s deleted successfully.') % circuit)
        except Exception, e:
            messages.error(request, _(u'Circuit: %(circuit)s delete error: %(error)s') % {
                'circuit': circuit, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'circuit'),
        'delete_view': True,
        'previous': previous,
        'next': next,
        'title': _(u'Are you sure you wish to delete the circuit: %s?') % circuit,
        'form_icon': icon_circuit_delete,
        'circuit': circuit,
        'agency': circuit.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'circuit'},
        ],
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def circuit_view(request, circuit_pk):
    circuit = get_object_or_404(Circuit, pk=circuit_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_CIRCUIT_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_CIRCUIT_VIEW, request.user, circuit.agency)

    form = CircuitForm_detail(instance=circuit)

    return render_to_response('generic_detail.html', {
        'form': form,
        'circuit': circuit,
        'agency': circuit.agency,
        'navigation_object_list': [
            {'object': 'agency'},
            {'object': 'circuit'},
        ],
    }, context_instance=RequestContext(request))


def circuit_create(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_CIRCUIT_CREATE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_CIRCUIT_CREATE, request.user, agency)

    if request.method == 'POST':
        form = CircuitForm_create(request.POST)
        if form.is_valid():
            circuit = form.save(commit=False)
            circuit.agency = agency
            circuit.save()
            messages.success(request, _(u'Circuit "%s" added successfully.') % circuit)
            return HttpResponseRedirect(reverse('agency_circuit_list', args=[agency.pk]))
    else:
        form = CircuitForm_create()

    return render_to_response('generic_form.html', {
        'form': form,
        'title': _(u'Add circuit to agency: %s') % agency,
        'object': agency,
        'agency': agency,
    }, context_instance=RequestContext(request))
