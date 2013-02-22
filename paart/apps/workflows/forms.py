from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _


class WorkflowActionSubmitForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.workflow_instance = kwargs.pop('workflow_instance')
        super(WorkflowActionSubmitForm, self).__init__(*args, **kwargs)
        self.fields['action'] = forms.ModelChoiceField(label=_(u'Action'), queryset=self.workflow_instance.get_actions())
        self.fields['comments'] = forms.CharField(widget=forms.widgets.Textarea(), label=_(u'Comments'), required=False)
