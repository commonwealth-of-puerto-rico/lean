from __future__ import absolute_import

from django import forms

from common.forms import DetailForm, ROFormMixin

from .models import ToolsProfile


class ToolsProfileForm_edit(forms.ModelForm, ROFormMixin):
    readonly_fields = ('agency',)

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['antivirus'].help_text = ''
        self.fields['backup'].help_text = ''
        self.fields['database'].help_text = ''
        self.fields['development'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['firewall'].help_text = ''

    class Meta:
        model = ToolsProfile
        widgets = {
            'antivirus': forms.widgets.CheckboxSelectMultiple,
            'backup': forms.widgets.CheckboxSelectMultiple,
            'database': forms.widgets.CheckboxSelectMultiple,
            'development': forms.widgets.CheckboxSelectMultiple,
            'email': forms.widgets.CheckboxSelectMultiple,
            'firewall': forms.widgets.CheckboxSelectMultiple,
            }


class ToolsProfileForm_detail(DetailForm):
    class Meta:
        model = ToolsProfile
        widgets = {
            'antivirus': forms.widgets.CheckboxSelectMultiple,
            'backup': forms.widgets.CheckboxSelectMultiple,
            'database': forms.widgets.CheckboxSelectMultiple,
            'development': forms.widgets.CheckboxSelectMultiple,
            'email': forms.widgets.CheckboxSelectMultiple,
            'firewall': forms.widgets.CheckboxSelectMultiple,
            }


class ToolsProfileForm_create(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['antivirus'].help_text = ''
        self.fields['backup'].help_text = ''
        self.fields['database'].help_text = ''
        self.fields['development'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['firewall'].help_text = ''

    class Meta:
        model = ToolsProfile
        exclude = ('agency',)
        widgets = {
            'antivirus': forms.widgets.CheckboxSelectMultiple,
            'backup': forms.widgets.CheckboxSelectMultiple,
            'database': forms.widgets.CheckboxSelectMultiple,
            'development': forms.widgets.CheckboxSelectMultiple,
            'email': forms.widgets.CheckboxSelectMultiple,
            'firewall': forms.widgets.CheckboxSelectMultiple,
            }
