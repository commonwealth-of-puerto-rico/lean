from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from permissions.models import PermissionNamespace, Permission

namespace = PermissionNamespace('tools', _(u'Tools'))

PERMISSION_TOOL_PROFILE_CREATE = Permission.objects.register(namespace, 'tool_profile_create', _(u'Create tool_profiles'))
PERMISSION_TOOL_PROFILE_EDIT = Permission.objects.register(namespace, 'tool_profile_edit', _(u'Edit tool_profiles'))
PERMISSION_TOOL_PROFILE_DELETE = Permission.objects.register(namespace, 'tool_profile_delete', _(u'Delete tool_profiles'))
PERMISSION_TOOL_PROFILE_VIEW = Permission.objects.register(namespace, 'tool_profile_view', _(u'View tool_profiles'))
