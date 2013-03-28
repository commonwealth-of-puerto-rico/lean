from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from permissions.models import PermissionNamespace, Permission

namespace = PermissionNamespace('software', _(u'Software'))

PERMISSION_AGENCY_SOFTWARE_CREATE = Permission.objects.register(namespace, 'agency_software_create', _(u'Create agency software'))
PERMISSION_AGENCY_SOFTWARE_EDIT = Permission.objects.register(namespace, 'agency_software_edit', _(u'Edit agency software'))
PERMISSION_AGENCY_SOFTWARE_DELETE = Permission.objects.register(namespace, 'agency_software_delete', _(u'Delete agency software'))
PERMISSION_AGENCY_SOFTWARE_VIEW = Permission.objects.register(namespace, 'agency_software_view', _(u'View agency software'))
