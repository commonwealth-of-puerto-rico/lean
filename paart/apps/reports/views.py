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

from projects.models import Project

from permissions.models import Permission

from .permissions import (PERMISSION_PROJECT_VIEW)

from .forms import AgencySearchForm
    
def agency_search_report(request):
    
    error = False
    title = 'Agency project search'
    form = AgencySearchForm()
    
    context = {
                'form': form,
                'title': title,
                'error': error
    }
    
    if 'q' in request.GET:
        q = request.GET['q']

        if not q:
            context['error'] = True
        else:
            context['q'] = q           
            context['projects'] = Project.objects.filter(agency__name__icontains=q).order_by('agency__name')
            context['title'] = title + ' for ' + q
            
            if not context['projects']:
                context['message'] = 'No results'
    
    return render_to_response('agency_search.html', context, context_instance=RequestContext(request))

