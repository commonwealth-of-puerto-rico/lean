from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from permissions.models import PermissionNamespace, Permission

namespace = PermissionNamespace('tools', _(u'Tools'))

PERMISSION_TOOLS_PROFILE_CREATE = Permission.objects.register(namespace, 'tools_profile_create', _(u'Create tools profiles'))
PERMISSION_TOOLS_PROFILE_EDIT = Permission.objects.register(namespace, 'tools_profile_edit', _(u'Edit tools profiles'))
PERMISSION_TOOLS_PROFILE_DELETE = Permission.objects.register(namespace, 'tools_profile_delete', _(u'Delete tools profiles'))
PERMISSION_TOOLS_PROFILE_VIEW = Permission.objects.register(namespace, 'tools_profile_view', _(u'View tools profiles'))
