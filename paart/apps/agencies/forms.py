from __future__ import absolute_import

from django import forms

from common.forms import DetailForm

from .models import Agency


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency


class AgencyForm_view(DetailForm):
    class Meta:
        model = Agency
