from __future__ import absolute_import

from xml.etree.ElementTree import Element, SubElement

multi_object_navigation = {}
model_list_columns = {}
sidebar_templates = {}
main_menu = Element('root')


def register_top_menu(name, link, position=None):
    """
    Register a new menu entry for the main menu displayed at the top
    of the page
    """
    new_menu = SubElement(main_menu, name, link=link, position=position)

    sorted_menus = sorted(main_menu.getchildren(), key=lambda k: (k.get('position') < 0, k.get('position')))
    main_menu.clear()

    for menu in sorted_menus:
        main_menu.append(menu)

    return new_menu


def register_model_list_columns(model, columns):
    """
    Define which columns will be displayed in the generic list template
    for a given model
    """

    model_list_columns.setdefault(model, [])
    model_list_columns[model].extend(columns)


def register_sidebar_template(source_list, template_name):
    for source in source_list:
        sidebar_templates.setdefault(source, [])
        sidebar_templates[source].append(template_name)


def register_multi_item_links(sources, links, menu_name=None):
    """
    Register a multiple item action action to be displayed in the
    generic list template
    """
    multi_object_navigation.setdefault(menu_name, {})
    for source in sources:
        multi_object_navigation[menu_name].setdefault(source, {'links': []})
        multi_object_navigation[menu_name][source]['links'].extend(links)
