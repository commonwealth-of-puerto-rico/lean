from __future__ import absolute_import

from django import forms

from common.forms import DetailForm, ROFormMixin, Select2FormMixin

from .models import Equipment


class EquipmentForm(Select2FormMixin, forms.ModelForm, ROFormMixin):
    readonly_fields = ('agency',)

    class Meta:
        model = Equipment


class EquipmentForm_detail(DetailForm):
    class Meta:
        model = Equipment


class EquipmentForm_create(Select2FormMixin, forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = ('agency',)
