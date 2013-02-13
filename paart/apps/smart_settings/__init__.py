from __future__ import absolute_import

from project_setup.api import register_setup

from .links import link_check_settings

register_setup(link_check_settings)
