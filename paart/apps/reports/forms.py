# -*- coding: utf-8 -*- 

from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from agencies.models import Agency
from projects.models import (ProjectInfo, FiscalYear, Purpose, Classification, 
Methodology, Department, Goal)


class AgencySearchForm(forms.Form):
    agency_text = forms.CharField(required=False, label=_('Agency'))
    project_text = forms.CharField(required=False, label=_('Project'))
    fiscal_year = forms.ModelChoiceField(required=False, queryset=FiscalYear.objects.all(), label=_('Fiscal Year'))
    purpose = forms.ModelChoiceField(required=False, queryset=Purpose.objects.all(), label=_('Purpose'))
    classification = forms.ModelChoiceField(required=False, queryset=Classification.objects.all(), label=_('Classification'))
    secondary_classification = forms.ModelChoiceField(required=False, queryset=Classification.objects.all(), label=_('Secondary Classification'))
    methodology = forms.ModelChoiceField(required=False, queryset=Methodology.objects.all(), label=_('Methodology'))
    department = forms.ModelChoiceField(required=False, queryset=Department.objects.all(), label=_('Department'))
    goal = forms.ModelChoiceField(required=False, queryset=Goal.objects.all(), label=_('Goals'))
    date_from = forms.DateField(required=False, input_formats=['%m/%d/%Y'],  widget=forms.TextInput(attrs={'class': 'datepicker'}), label=_('Date From'))
    date_to = forms.DateField(required=False, input_formats=['%m/%d/%Y'], widget=forms.TextInput(attrs={'class': 'datepicker'}), label=_('Date to'))