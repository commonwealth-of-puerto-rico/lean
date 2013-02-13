from __future__ import absolute_import

from django.conf import settings as django_settings
from django.utils.importlib import import_module

from .classes import Setting

settings = {}


def register_setting(namespace, module, name, global_name, default, exists=False, description=u'', hidden=False):
    # Create namespace if it doesn't exists
    settings.setdefault(namespace, [])

    # If passed a string and not a module, import it
    if isinstance(module, basestring):
        module = import_module(module)

    setting = {
        'module': module,
        'name': name,
        'global_name': global_name,
        'exists': exists,
        'description': description,
        'default': default,
        'hidden': hidden,
    }

    # Avoid multiple appends
    if setting not in settings[namespace]:
        settings[namespace].append(setting)

    # Get the global value
    value = getattr(django_settings, global_name, default)

    # Create the local entity
    setattr(module, name, value)
    return value


def register_settings(namespace, module, settings):
    for setting in settings:
        register_setting(
            namespace,
            module,
            setting['name'],
            setting['global_name'],
            setting['default'],
            setting.get('exists', False),
            setting.get('description', u''),
            setting.get('hidden', False),
        )


def get_settings():
    new_settings = []
    for namespace, sub_settings in settings.items():
        for sub_setting in sub_settings:
            if not sub_setting.get('hidden', False):
                new_settings.append(
                    Setting(
                        module=sub_setting['module'],
                        name=sub_setting['name'],
                        global_name=sub_setting['global_name'],
                        description=sub_setting.get('description', None),
                        exists=sub_setting.get('exists', False),
                        default=sub_setting['default'],
                    )
                )
                
    return new_settings
