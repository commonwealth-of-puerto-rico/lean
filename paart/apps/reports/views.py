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

from permissions.models import Permission

from .permissions import (PERMISSION_PROJECT_VIEW)

def project_reports_view(request):
    
    try:
        Permission.objects.check_permissions(request.user, [PERMISSION_PROJECT_VIEW])
    except PermissionDenied:
        AccessEntry.objects.check_access(PERMISSION_PROJECT_VIEW, request.user, project.agency)
    
    response = HttpResponse('Test')
    return response
