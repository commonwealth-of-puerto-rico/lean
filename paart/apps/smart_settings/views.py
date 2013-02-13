from __future__ import absolute_import

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from common.utils import return_type, encapsulate
from common.widgets import exists_with_icon

from .api import get_settings


def setting_list(request):

    context = {
        'title': _(u'settings'),
        'object_list': get_settings(),
        'hide_link': True,
        'hide_object': True,
        'extra_columns': [
            {'name': _(u'name'), 'attribute': encapsulate(lambda x: mark_safe(u'<span style="font-weight: bold;">%s</span><br />%s' % (x.global_name, x.description)))},
            {'name': _(u'default'), 'attribute': encapsulate(lambda x: return_type(x.default))},
            {'name': _(u'value'), 'attribute': encapsulate(lambda x: mark_safe(u'<div class="nowrap">%s&nbsp;%s</div>' % (
                    return_type(getattr(x.module, x.name)),
                    exists_with_icon(getattr(x.module, x.name)).display_small() if x.exists else ''
                )))
            },
        ]
    }

    return render_to_response('generic_list.html', context,
        context_instance=RequestContext(request))
