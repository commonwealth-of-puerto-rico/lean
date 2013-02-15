from __future__ import absolute_import

from django import forms

from common.forms import DetailForm, ROFormMixin

from .models import Equipment


class EquipmentForm(forms.ModelForm, ROFormMixin):
    readonly_fields = ('agency',)
    
    class Meta:
        model = Equipment


class EquipmentForm_detail(DetailForm):
    class Meta:
        model = Equipment
        #exclude = ('document', 'document_type', 'page_label', 'content')
