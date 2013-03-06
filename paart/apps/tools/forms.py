from __future__ import absolute_import

from django import forms

from common.forms import DetailForm, ROFormMixin, Select2FormMixin

from .models import ToolsProfile


class ToolsProfileForm_edit(Select2FormMixin, forms.ModelForm, ROFormMixin):
    readonly_fields = ('agency',)

    class Meta:
        model = ToolsProfile


class ToolsProfileForm_detail(DetailForm):
    class Meta:
        model = ToolsProfile


class ToolsProfileForm_create(Select2FormMixin, forms.ModelForm):
    class Meta:
        model = ToolsProfile
        exclude = ('agency',)
