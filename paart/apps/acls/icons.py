from __future__ import absolute_import

from icons.literals import (KEY, KEY_GO, KEY_ADD, KEY_DELETE, LOCK, USER_ADD,
    PACKAGE, LOCK_GO, USER, GROUP, PAGE, THEATER, FOLDER, TAG_BLUE, PAGE_LINK,
    HELP)
from icons import Icon

icon_acl_app = Icon(LOCK)

icon_acls = Icon(KEY)
icon_acl_detail = Icon(KEY_GO)
icon_acl_grant = Icon(KEY_ADD)
icon_acl_revoke = Icon(KEY_DELETE)
icon_acl_holder_new = Icon(USER_ADD)

icon_acl_class_list = Icon(PACKAGE)
icon_acl_class_acl_list = Icon(LOCK_GO)
icon_acl_class_acl_detail = Icon(KEY_GO)
icon_acl_class_new_holder_for = Icon(USER_ADD)
icon_acl_class_grant = Icon(KEY_ADD)
icon_acl_class_revoke = Icon(KEY_DELETE)

icon_content_type_user = Icon(USER)
icon_content_type_group = Icon(GROUP)
icon_content_type_document = Icon(PAGE)
icon_content_type_role = Icon(THEATER)
icon_content_type_folder = Icon(FOLDER)
icon_content_type_tag = Icon(TAG_BLUE)
icon_content_type_smart_link = Icon(PAGE_LINK)
icon_content_type_anonymous = Icon(USER)
icon_content_type_creator = Icon(USER)
icon_content_type_unknown = Icon(HELP)
