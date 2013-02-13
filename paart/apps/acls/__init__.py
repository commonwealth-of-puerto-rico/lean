from __future__ import absolute_import

from navigation.api import register_multi_item_links
from navigation.classes import Link
from project_setup.api import register_setup

from .classes import (AccessHolder, AccessObjectClass, ClassAccessHolder,
    AccessObject)
from .links import (acl_detail, acl_grant, acl_revoke, acl_holder_new,
    acl_setup_valid_classes, acl_class_list, acl_class_acl_list, acl_class_acl_detail,
    acl_class_new_holder_for, acl_class_grant, acl_class_revoke)


Link.bind_links([AccessHolder], [acl_detail])
register_multi_item_links(['acl_detail'], [acl_grant, acl_revoke])

Link.bind_links([AccessObject], [acl_holder_new], menu_name='sidebar')

register_setup(acl_setup_valid_classes)
Link.bind_links(['acl_setup_valid_classes', 'acl_class_acl_list', 'acl_class_new_holder_for', 'acl_class_acl_detail', 'acl_class_multiple_grant', 'acl_class_multiple_revoke'], [acl_class_list], menu_name='secondary_menu')

Link.bind_links([ClassAccessHolder], [acl_class_acl_detail])

Link.bind_links([AccessObjectClass], [acl_class_acl_list, acl_class_new_holder_for])
register_multi_item_links(['acl_class_acl_detail'], [acl_class_grant, acl_class_revoke])
