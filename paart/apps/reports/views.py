# -*- coding: utf-8 -*-

from __future__ import absolute_import

import datetime
import pytz

from django.conf import global_settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import PermissionDenied

from projects.models import Project, ProjectInfo, Agency

from acls.models import AccessEntry
from permissions.models import Permission
from .permissions import PERMISSION_PROJECT_VIEW

from .forms import AgencySearchForm


def agency_search_report(request):
    kwargs = {}
    context = {}
    localtz = pytz.timezone(global_settings.TIME_ZONE)

    if request.GET:
        form = AgencySearchForm(data=request.GET)
        if form.is_valid():
            if 'agency_text' in request.GET and request.GET['agency_text']:
                kwargs['agency__name__icontains'] = request.GET['agency_text']

            if 'project_text'in request.GET and request.GET['project_text']:
                kwargs['label__icontains'] = request.GET['project_text']

            if 'fiscal_year' in request.GET and request.GET['fiscal_year']:
                kwargs['projectinfo__fiscal_year'] = request.GET['fiscal_year']

            if 'purpose' in request.GET and request.GET['purpose']:
                kwargs['projectinfo__purpose'] = request.GET['purpose']

            if 'classification' in request.GET and request.GET['classification']:
                kwargs['projectinfo__classification'] = request.GET['classification']

            if 'secondary_classification' in request.GET and request.GET['secondary_classification']:
                kwargs['projectinfo__classification_secondary'] = request.GET['secondary_classification']

            if 'methodology' in request.GET and request.GET['methodology']:
                kwargs['projectinfo__methodology'] = request.GET['methodology']

            if 'goal' in request.GET and request.GET['goal']:
                kwargs['projectinfo__goals__in'] = request.GET['goal']

            if 'department' in request.GET and request.GET['department']:
                kwargs['projectinfo__department'] = request.GET['department']

            if 'date_from' in request.GET and request.GET['date_from']:
                date_from = datetime.datetime.strptime(request.GET['date_from'], '%m/%d/%Y')
                kwargs['datetime_created__gte'] = date_from.replace(tzinfo=localtz)

            if 'date_to' in request.GET and request.GET['date_to']:
                date_to = datetime.datetime.strptime(request.GET['date_to'], '%m/%d/%Y')
                kwargs['datetime_created__lte'] = date_to.replace(tzinfo=localtz)

            try:
                Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
            except PermissionDenied:
                # If user doesn't have global permission, get a list of document
                # for which he/she does have access use it to filter the
                # provided object_list
                search_results = AccessEntry.objects.filter_objects_by_access(PERMISSION_PROJECT_VIEW, request.user,
                                                                              Project.objects.filter(**kwargs).order_by('agency__name'),
                                                                              related='agency')
            else:
                search_results = Project.objects.filter(**kwargs).order_by('agency__name')

            if not search_results:
                context['message'] = _(u'No results')
            else:
                paginator = Paginator(search_results, 25)
                page = request.GET.get('page')
                try:
                    context['results'] = paginator.page(page)
                except PageNotAnInteger:
                    context['results'] = paginator.page(1)
                except EmptyPage:
                    context['results'] = paginator.page(paginator.num_pages)

        context['agency_search_form'] = form
    else:
        context.update({
            'agency_search_form': AgencySearchForm(),
        })

    return render_to_response('agency_search.html', context, context_instance=RequestContext(request))
