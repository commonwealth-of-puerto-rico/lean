# -*- coding: utf-8 -*-

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
from django.utils.translation import ugettext_lazy as _, string_concat

from projects.models import Project, ProjectInfo, Agency

from permissions.models import Permission

from .permissions import (PERMISSION_PROJECT_VIEW)

from .forms import AgencySearchForm

def agency_search_report(request):
    title = 'Búsqueda de proyectos por agencia'
    search_results = None
    kwargs = {}
    context = {}

    if request.GET:
        form = AgencySearchForm(data=request.GET)
        if form.is_valid():
            if 'agency_text' in request.GET and request.GET['agency_text']:
                kwargs['agency__name__icontains'] = request.GET['agency_text']

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

            search_results = Project.objects.filter(**kwargs).order_by('agency__name')
            context['results'] = search_results[:100]

            if not context['results']:
                context['message'] = _(u'No results')
            else:
                if len(search_results) <= 100:
                    context['message'] = string_concat(str(len(context['results'])), ' ', _(u'results'))
                else:
                    context['message'] = string_concat(_(u'Presenting'), ' ', str(len(context['results'])), ' ', _(u'of'), ' ', str(len(search_results)), ' ', _(u'results, please use a filter'))

        context['agency_search_form'] = form
    else:
        context.update({
            'agency_search_form': AgencySearchForm(),
            'title': title,
        })

    return render_to_response('agency_search.html', context, context_instance=RequestContext(request))
