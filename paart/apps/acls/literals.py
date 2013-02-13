from __future__ import absolute_import

from .icons import (icon_content_type_user, icon_content_type_group,
    icon_content_type_document, icon_content_type_role, icon_content_type_folder,
    icon_content_type_tag, icon_content_type_smart_link, icon_content_type_anonymous,
    icon_content_type_creator)

# Content type <-> icon mapping
CONTENT_TYPE_ICON_MAP = {
    'auth.user': icon_content_type_user,
    'auth.group': icon_content_type_group,
    'documents.document': icon_content_type_document,
    'permissions.role': icon_content_type_role,
    'folders.folder': icon_content_type_folder,
    'taggit.tag': icon_content_type_tag,
    'linking.smartlink': icon_content_type_smart_link,
    'common.anonymoususersingleton': icon_content_type_anonymous,
    'acls.creatorsingleton': icon_content_type_creator,
}
