from __future__ import absolute_import

from django import forms

from common.forms import DetailForm, ROFormMixin

from .models import ToolsProfile


class ToolsProfileForm(forms.ModelForm, ROFormMixin):
    readonly_fields = ('agency',)

    class Meta:
        model = ToolsProfile


class ToolsProfileForm_detail(DetailForm):
    class Meta:
        model = ToolsProfile
