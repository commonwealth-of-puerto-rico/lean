from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .permissions import (ACLS_EDIT_ACL, ACLS_VIEW_ACL,
    ACLS_CLASS_EDIT_ACL, ACLS_CLASS_VIEW_ACL)
from .icons import (icon_acls, icon_acl_detail, icon_acl_grant, icon_acl_revoke,
    icon_acl_holder_new, icon_acl_class_list, icon_acl_class_acl_list,
    icon_acl_class_acl_list, icon_acl_class_acl_detail, icon_acl_class_new_holder_for,
    icon_acl_class_grant, icon_acl_class_revoke)

acl_list = Link(text=_(u'ACLs'), view='acl_list', icon=icon_acls, permissions=[ACLS_VIEW_ACL])
acl_detail = Link(text=_(u'details'), view='acl_detail', args=['access_object.gid', 'object.gid'], icon=icon_acl_detail, permissions=[ACLS_VIEW_ACL])
acl_grant = Link(text=_(u'grant'), view='acl_multiple_grant', icon=icon_acl_grant, permissions=[ACLS_EDIT_ACL])
acl_revoke = Link(text=_(u'revoke'), view='acl_multiple_revoke', icon=icon_acl_revoke, permissions=[ACLS_EDIT_ACL])
acl_holder_new = Link(text=_(u'new holder'), view='acl_holder_new', args='access_object.gid', icon=icon_acl_holder_new, permissions=[ACLS_EDIT_ACL])

acl_setup_valid_classes = Link(text=_(u'Default ACLs'), view='acl_setup_valid_classes', icon=icon_acl_class_list, permissions=[ACLS_CLASS_VIEW_ACL], children_view_regex=[r'^acl_class', r'^acl_setup'])
acl_class_list = Link(text=_(u'List of classes'), view='acl_setup_valid_classes', icon=icon_acl_class_list, permissions=[ACLS_CLASS_VIEW_ACL])
acl_class_acl_list = Link(text=_(u'ACLs for class'), view='acl_class_acl_list', args='object.gid', icon=icon_acl_class_acl_list, permissions=[ACLS_CLASS_VIEW_ACL])
acl_class_acl_detail = Link(text=_(u'details'), view='acl_class_acl_detail', args=['access_object_class.gid', 'object.gid'], icon=icon_acl_class_acl_detail, permissions=[ACLS_CLASS_VIEW_ACL])
acl_class_new_holder_for = Link(text=_(u'New holder'), view='acl_class_new_holder_for', args='object.gid', icon=icon_acl_class_new_holder_for, permissions=[ACLS_CLASS_EDIT_ACL])
acl_class_grant = Link(text=_(u'grant'), view='acl_class_multiple_grant', icon=icon_acl_class_grant, permissions=[ACLS_CLASS_EDIT_ACL])
acl_class_revoke = Link(text=_(u'revoke'), view='acl_class_multiple_revoke', icon=icon_acl_class_revoke, permissions=[ACLS_CLASS_EDIT_ACL])




def get_app_label(context):
    try:
        return context['source_object']._meta.app_label
    except KeyError:
        return context['resolved_object']._meta.app_label        


def get_module_name(context):
    try:
        return context['source_object']._meta.module_name
    except KeyError:
        return context['resolved_object']._meta.module_name        


def get_pk(context):
    try:
        return context['source_object'].pk
    except KeyError:
        return context['resolved_object'].pk



link_acl_list = Link(text=_(u'ACLs'), view='acl_list', args=[get_app_label, get_module_name, get_pk], permissions=[ACLS_VIEW_ACL], icon=icon_acls)
link_acl_detail = Link(text=_(u'details'), view='acl_detail', args=['resolved_object.pk', get_app_label, get_module_name, get_pk], icon=icon_acl_detail, permissions=[ACLS_VIEW_ACL])

link_acl_holder_new = Link(text=_(u'new holder'), view='acl_holder_new', args=[get_app_label, get_module_name, get_pk], permissions=[ACLS_EDIT_ACL], icon=icon_acl_holder_new)
#link_acl_grant = Link(text=_(u'grant'), view='acl_multiple_grant', args='object.pk', permissions=[ACLS_EDIT_ACL], icon=icon_acl_grant)
#link_transformation_delete = Link(text=_(u'delete'), view='transformation_delete', args='object.pk', permissions=[PERMISSION_TRANSFORMATION_DELETE], icon=icon_transformation_delete)

#acl_grant = Link(text=_(u'grant'), view='acl_multiple_grant', icon=icon_acl_grant, permissions=[ACLS_EDIT_ACL])
#acl_revoke = Link(text=_(u'revoke'), view='acl_multiple_revoke', icon=icon_acl_revoke, permissions=[ACLS_EDIT_ACL])
#acl_holder_new = Link(text=_(u'new holder'), view='acl_holder_new', args='access_object.gid', icon=icon_acl_holder_new, permissions=[ACLS_EDIT_ACL])

