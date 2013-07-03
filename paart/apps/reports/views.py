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

from projects.models import Project, ProjectInfo

from permissions.models import Permission

from .permissions import (PERMISSION_PROJECT_VIEW)

from .forms import AgencySearchForm
    
def agency_search_report(request):
    
    error = False
    title = 'Agency project search'
    search_results = None
    agency_search_form = AgencySearchForm()
    
    context = {
                'agency_search_form': agency_search_form,
                'title': title,
                'error': error
    }
    
    if 'agency_text' in request.GET:

        agency_text = request.GET['agency_text']

        if not agency_text:
            context['error'] = True
        else:
            context['agency_text'] = agency_text           
            search_results = Project.objects.filter(agency__name__icontains=agency_text).order_by('agency__name')
            context['title'] = title + ' for ' + agency_text
            
            if 'fiscal_year' in request.GET and request.GET['fiscal_year']:
                fiscal_year = request.GET['fiscal_year']
                
                search_results = search_results.filter(projectinfo__fiscal_year=fiscal_year)
                    
            context['results'] = search_results
            
            if not context['results']:
                context['message'] = 'No results'
            else:
                context['message'] = str(len(context['results'])) + ' results for ' + context['agency_text']
    
    return render_to_response('agency_search.html', context, context_instance=RequestContext(request))

