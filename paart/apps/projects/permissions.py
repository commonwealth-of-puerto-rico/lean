from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from permissions.models import PermissionNamespace, Permission

namespace = PermissionNamespace('projects', _(u'Project'))

PERMISSION_PROJECT_CREATE = Permission.objects.register(namespace, 'project_create', _(u'Create projects'))
PERMISSION_PROJECT_EDIT = Permission.objects.register(namespace, 'project_edit', _(u'Edit projects'))
PERMISSION_PROJECT_DELETE = Permission.objects.register(namespace, 'project_delete', _(u'Delete projects'))
