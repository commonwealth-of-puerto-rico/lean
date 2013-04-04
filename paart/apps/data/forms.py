from __future__ import absolute_import

from django import forms

from common.forms import DetailForm, ROFormMixin, Select2FormMixin

from .models import AgencyData


class AgencyDataForm(Select2FormMixin, forms.ModelForm, ROFormMixin):
    class Meta:
        model = AgencyData
        exclude = ('agency',)


class AgencyDataForm_detail(DetailForm):
    class Meta:
        model = AgencyData
        exclude = ('agency',)


class AgencyDataForm_create(Select2FormMixin, forms.ModelForm):
    class Meta:
        model = AgencyData
        exclude = ('agency',)
