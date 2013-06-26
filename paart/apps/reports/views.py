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

from permissions.models import Permission

from .permissions import (PERMISSION_PROJECT_VIEW)

from .forms import AgencySearchForm

    
def agency_search_form(request):
    return render_to_response('agency_search.html', context_instance=RequestContext(request))
    
def agency_busqueda_report(request):
    
    form = AgencySearchForm()
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        agencies = Agency.objects.filter(name__icontains=q)
            
        return render_to_response('agency_search.html', {
            'form': form,
            'agencies': agencies,
            'query': q
        }, context_instance=RequestContext(request))
    
    else:
        return HttpResponse('Please submit a search.')
