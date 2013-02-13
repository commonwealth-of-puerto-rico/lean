from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .icons import icon_home

home_link = Link(text=_(u'home'), view='home', icon=icon_home)
