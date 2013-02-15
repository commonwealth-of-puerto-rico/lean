from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from permissions.models import PermissionNamespace, Permission

namespace = PermissionNamespace('telecomm', _(u'Telecomm'))

PERMISSION_EQUIPMENT_CREATE = Permission.objects.register(namespace, 'equipment_create', _(u'Create equipments'))
PERMISSION_EQUIPMENT_EDIT = Permission.objects.register(namespace, 'equipment_edit', _(u'Edit equipments'))
PERMISSION_EQUIPMENT_DELETE = Permission.objects.register(namespace, 'equipment_delete', _(u'Delete equipments'))
PERMISSION_EQUIPMENT_VIEW = Permission.objects.register(namespace, 'equipment_view', _(u'View equipments'))

PERMISSION_PROVIDER_CREATE = Permission.objects.register(namespace, 'provider_create', _(u'Create providers'))
PERMISSION_PROVIDER_EDIT = Permission.objects.register(namespace, 'provider_edit', _(u'Edit providers'))
PERMISSION_PROVIDER_DELETE = Permission.objects.register(namespace, 'provider_delete', _(u'Delete providers'))
PERMISSION_PROVIDER_VIEW = Permission.objects.register(namespace, 'provider_view', _(u'View providers'))
