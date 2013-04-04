from __future__ import absolute_import

from django import forms

from common.forms import DetailForm, ROFormMixin, Select2FormMixin

from .models import AgencySoftware


class AgencySoftwareForm_edit(Select2FormMixin, forms.ModelForm, ROFormMixin):
    class Meta:
        model = AgencySoftware
        exclude = ('agency',)


class AgencySoftwareForm_detail(DetailForm):
    class Meta:
        model = AgencySoftware


class AgencySoftwareForm_create(Select2FormMixin, forms.ModelForm):
    class Meta:
        model = AgencySoftware
        exclude = ('agency',)
