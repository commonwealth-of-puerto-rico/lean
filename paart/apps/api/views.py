from __future__ import absolute_import

import logging

from django.conf import settings
from django.contrib.auth.models import User, Group

try:
    import ldap
except ImportError:
    pass

from rest_framework import generics
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from agencies.models import Agency
#from proyect.models import Proyect

from .serializers import AgencySerializer

logger = logging.getLogger(__name__)
LDAP_TIMEOUT = 2

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'v0': reverse('api-version-0', request=request),
    })


@api_view(('GET',))
def version_0(request, format=None):
    return Response({
        'agencies': reverse('agency-list', request=request),
        'status': reverse('status-list', request=request),
    })


class AgencyList(generics.ListAPIView):
    model = Agency
    serializer_class = AgencySerializer


class AgencyDetail(generics.RetrieveAPIView):
    model = Agency
    serializer_class = AgencySerializer


class StatusList(APIView):
    def get(self, request, format=None):
        elements = {
            'framework.settings.AUTHENTICATION_BACKENDS.list': settings.AUTHENTICATION_BACKENDS,
        }
        if 'django_auth_ldap.backend.LDAPBackend' in settings.AUTHENTICATION_BACKENDS:
            elements.update(
                {
                    'framework.settings.AUTH_LDAP_SERVER_URI.string': settings.AUTH_LDAP_SERVER_URI,
                    'framework.settings.AUTH_LDAP_BIND_DN.string': settings.AUTH_LDAP_BIND_DN,
                    'framework.settings.AUTH_LDAP_BIND_PASSWORD.string': settings.AUTH_LDAP_BIND_PASSWORD,
                }
            )
            try:
                connection = ldap.initialize(settings.AUTH_LDAP_SERVER_URI)
                connection.set_option(ldap.OPT_NETWORK_TIMEOUT, LDAP_TIMEOUT)
                connection.simple_bind_s(settings.AUTH_LDAP_BIND_DN, settings.AUTH_LDAP_BIND_PASSWORD)
            except ldap.LDAPError as exception:
                result = unicode(exception)
            else:
                result = True
                connection.unbind_s()

            elements['framework.backends.LDAP.simple_bind.timeout.number'] = LDAP_TIMEOUT
            elements['framework.backends.LDAP.simple_bind.status.hybrid'] = result

        return Response(elements)
