from __future__ import absolute_import

from navigation.api import register_top_menu

from .links import home_link
from .settings import DISABLE_HOME_VIEW

__author__ = 'Roberto Rosario'
__copyright__ = 'Copyright 2013 Roberto Rosario'
__credits__ = ['Roberto Rosario',]
__license__ = 'GPL'
__maintainer__ = 'Roberto Rosario'
__email__ = 'roberto.rosario.gonzalez@gmail.com'
__status__ = 'Unstable'

__version_info__ = {
    'major': 1,
    'minor': 0,
    'micro': 0,
    'releaselevel': 'alpha',
    'serial': 0
}

if not DISABLE_HOME_VIEW:
    register_top_menu('home', link=home_link, position=0)


def get_version():
    """
    Return the formatted version information
    """
    vers = ['%(major)i.%(minor)i' % __version_info__, ]

    if __version_info__['micro']:
        vers.append('.%(micro)i' % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s%(serial)i' % __version_info__)
    return ''.join(vers)


__version__ = get_version()
