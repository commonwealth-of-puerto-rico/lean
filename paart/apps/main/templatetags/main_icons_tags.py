from django.template import Library

from ..icons import (icon_home_page, icon_documentation, icon_source_code,
    icon_issue_tracker)

register = Library()


@register.simple_tag(takes_context=True)
def get_main_icons(context):
    context['icon_home_page'] = icon_home_page
    context['icon_documentation'] = icon_documentation
    context['icon_source_code'] = icon_source_code
    context['icon_issue_tracker'] = icon_issue_tracker
    return u''
