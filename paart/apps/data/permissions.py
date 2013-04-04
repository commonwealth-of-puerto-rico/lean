from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from permissions.models import PermissionNamespace, Permission

namespace = PermissionNamespace('data', _(u'Data'))

PERMISSION_DATA_CREATE = Permission.objects.register(namespace, 'agency_data_create', _(u'Create agency data'))
PERMISSION_DATA_EDIT = Permission.objects.register(namespace, 'agency_data_edit', _(u'Edit agency data'))
PERMISSION_DATA_DELETE = Permission.objects.register(namespace, 'agency_data_delete', _(u'Delete agency data'))
PERMISSION_DATA_VIEW = Permission.objects.register(namespace, 'agency_data_view', _(u'View agency data'))
