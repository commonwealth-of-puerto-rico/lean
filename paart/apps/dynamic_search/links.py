from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .icons import icon_search, icon_advanced_search, icon_search_again

search = Link(text=_(u'search'), view='search', icon=icon_search, children_view_regex=[r'^search', r'^result'])
search_advanced = Link(text=_(u'advanced search'), view='search_advanced', icon=icon_advanced_search)
search_again = Link(text=_(u'search again'), view='search_again', icon=icon_search_again)
