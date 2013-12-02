from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from permissions.models import PermissionNamespace, Permission

namespace = PermissionNamespace('projects', _(u'Project'))

PERMISSION_PROJECT_VIEW = Permission.objects.register(namespace, 'project_view', _(u'View projects'))
