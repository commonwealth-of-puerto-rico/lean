from __future__ import absolute_import

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, resolve
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from permissions.models import Permission

from .forms import AgencyForm
from .icons import icon_agency_delete
from .models import Agency
from .permissions import PERMISSION_AGENCY_EDIT, PERMISSION_AGENCY_DELETE


def agency_list(request):
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
        'object_list': Agency.objects.all(),
        'title': _(u'agencies'),
        'hide_object': True,
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))


def agency_edit(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_EDIT, request.user, document)

    if request.method == 'POST':
        form = AgencyForm(request.POST, instance=agency)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Agency "%s" edited successfully.') % agency)

            return HttpResponseRedirect(reverse('agency_list'))
    else:
        form = AgencyForm(instance=agency)

    return render_to_response('generic_form.html', {
        'form': form,
        'object': agency,
    }, context_instance=RequestContext(request))


def agency_delete(request, agency_pk):
    agency = get_object_or_404(Agency, pk=agency_pk)

    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_DELETE])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_AGENCY_DELETE, request.user, folder)

    post_action_redirect = reverse('agency_list')

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        try:
            folder.delete()
            messages.success(request, _(u'Agency: %s deleted successfully.') % agency)
        except Exception, e:
            messages.error(request, _(u'Agency: %(agency)s delete error: %(error)s') % {
                'agency': agency, 'error': e})

        return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'agency'),
        'delete_view': True,
        'previous': previous,
        'next': next,
        'object': agency,
        'title': _(u'Are you sure you with to delete the agency: %s?') % agency,
        'form_icon': icon_agency_delete,
    }

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))
