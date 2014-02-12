from __future__ import absolute_import

from navigation.api import register_sidebar_template, register_top_menu
from navigation.classes import Link

from .links import search, search_advanced, search_again

register_sidebar_template(['search', 'search_advanced'], 'search_help.html')

#Link.bind_links(['search', 'search_advanced', 'results'], [search, search_advanced], menu_name='form_header')
Link.bind_links(['search', 'search_advanced', 'results'], [search], menu_name='form_header')
Link.bind_links(['results'], [search_again], menu_name='sidebar')

register_sidebar_template(['search', 'search_advanced', 'results'], 'recent_searches.html')

#register_top_menu('search', link=search)
