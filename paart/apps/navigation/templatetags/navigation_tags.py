from __future__ import absolute_import

import copy
import logging
import re

from django.core.urlresolvers import resolve, reverse
from django.template import (TemplateSyntaxError, Library,
    Node, Variable, VariableDoesNotExist)
from django.utils.translation import ugettext as _

from ..api import main_menu, multi_object_navigation, sidebar_templates
from ..classes import Link
from ..forms import MultiItemForm

logger = logging.getLogger(__name__)
register = Library()


class TopMenuNavigationNode(Node):
    def render(self, context):
        request = Variable('request').resolve(context)
        current_path = request.META['PATH_INFO']
        current_view = resolve(current_path).url_name

        context['menu_links'] = [menu.get('link').resolve(context, request=request, current_path=current_path, current_view=current_view) for menu in main_menu.getchildren()]
        return ''


@register.tag
def get_top_menu_links(parser, token):
    return TopMenuNavigationNode()


class GetNavigationLinks(Node):
    def __init__(self, menu_name=None, links_dict=Link.bound_links, var_name='object_navigation_links'):
        self.menu_name = menu_name
        self.links_dict = links_dict
        self.var_name = var_name
        logger.debug('menu_name: %s' % menu_name)

    def render(self, context):
        menu_name = Link.resolve_template_variable(context, self.menu_name)
        context[self.var_name] = Link.get_context_navigation_links(context, menu_name, links_dict=self.links_dict)
        return ''


@register.tag(name='get_object_navigation_links')
def get_context_navigation_links_tag(parser, token):
    logger.debug('getting links')
    tag_name, arg = token.contents.split(None, 1)

    m = re.search(r'("?\w+"?)?.?as (\w+)', arg)
    if not m:
        raise TemplateSyntaxError("%r tag had invalid arguments" % tag_name)

    menu_name, var_name = m.groups()
    return GetNavigationLinks(menu_name=menu_name, var_name=var_name)


@register.inclusion_tag('generic_navigation.html', takes_context=True)
def object_navigation_template(context):
    # Used by list subtemplate to display list item links
    new_context = copy.copy(context)

    try:
        object_reference = Variable('object').resolve(context)
    except VariableDoesNotExist:
        pass
    else:
        new_context.update({
            'horizontal': True,
            'links': Link.get_context_navigation_links(context).get(object_reference)
        })

    return new_context


@register.tag
def get_multi_item_links(parser, token):
    tag_name, arg = token.contents.split(None, 1)
    m = re.search(r'("?\w+"?)?.?as (\w+)', arg)
    if not m:
        raise TemplateSyntaxError("%r tag had invalid arguments" % tag_name)

    menu_name, var_name = m.groups()
    return GetNavigationLinks(menu_name=menu_name, links_dict=multi_object_navigation, var_name=var_name)


# TODO: Fix flake8 warning apps/navigation/templatetags/navigation_tags.py:98: W802 undefined name 'get_context_object_navigation_links'
@register.inclusion_tag('generic_form_instance.html', takes_context=True)
def get_multi_item_links_form(context):
    logger.debug('starting')
    links = []
    for object_reference, object_links in get_context_object_navigation_links(context, links_dict=multi_object_navigation).items():
        links.extend(object_links)

    new_context = copy.copy(context)
    new_context.update({
        'form': MultiItemForm(actions=[(link.url, link.text) for link in links]),
        'title': _(u'Selected item actions:'),
        'form_action': reverse('multi_object_action_view'),
        'submit_method': 'get',
    })
    return new_context


class GetSidebarTemplatesNone(Node):
    def __init__(self, var_name='sidebar_templates'):
        self.var_name = var_name

    def render(self, context):
        request = Variable('request').resolve(context)
        view_name = resolve(request.META['PATH_INFO']).url_name
        context[self.var_name] = sidebar_templates.get(view_name, [])
        return ''


@register.tag
def get_sidebar_templates(parser, token):
    tag_name, arg = token.contents.split(None, 1)

    m = re.search(r'("?\w+"?)?.?as (\w+)', arg)
    if not m:
        raise TemplateSyntaxError("%r tag had invalid arguments" % tag_name)

    menu_name, var_name = m.groups()
    return GetSidebarTemplatesNone(var_name=var_name)
