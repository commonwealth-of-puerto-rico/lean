from __future__ import absolute_import

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save

from navigation.api import register_multi_item_links
from navigation.classes import Link
from project_setup.api import register_setup

from .links import (role_list, role_create, role_edit, role_members,
    role_permissions, role_delete, permission_grant, permission_revoke)
from .models import Role
from .settings import DEFAULT_ROLES

Link.bind_links([Role], [role_edit, role_delete, role_permissions, role_members])
Link.bind_links([Role, 'role_list', 'role_create'], [role_list, role_create], menu_name='secondary_menu')
register_multi_item_links(['role_permissions'], [permission_grant, permission_revoke])

permission_views = ['role_list', 'role_create', 'role_edit', 'role_members', 'role_permissions', 'role_delete']


def user_post_save(sender, instance, **kwargs):
    if kwargs.get('created', False):
        for default_role in DEFAULT_ROLES:
            if isinstance(default_role, Role):
                #If a model is passed, execute method
                default_role.add_member(instance)
            else:
                #If a role name is passed, lookup the corresponding model
                try:
                    role = Role.objects.get(name=default_role)
                    role.add_member(instance)
                except ObjectDoesNotExist:
                    pass

post_save.connect(user_post_save, sender=User)

register_setup(role_list)
