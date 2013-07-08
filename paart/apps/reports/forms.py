# -*- coding: utf-8 -*- 

from __future__ import absolute_import

from django import forms

from agencies.models import Agency
from projects.models import (ProjectInfo, FiscalYear, Purpose, Classification, 
Methodology, Department, Goal)
    
class AgencySearchForm(forms.Form):
    agency_text = forms.CharField(required=False, label='Agencia') 
    fiscal_year = forms.ModelChoiceField(required=False, queryset=FiscalYear.objects.all(), label= 'Año Fiscal')
    purpose = forms.ModelChoiceField(required=False, queryset=Purpose.objects.all(), label= 'Proposito')
    classification = forms.ModelChoiceField(required=False, queryset=Classification.objects.all(), label= 'Clasificacíon')
    secondary_classification = forms.ModelChoiceField(required=False, queryset=Classification.objects.all(), label= 'Clasificación Secundaria')
    methodology = forms.ModelChoiceField(required=False, queryset=Methodology.objects.all(), label= 'Metodología')
    department = forms.ModelChoiceField(required=False, queryset=Department.objects.all(), label= 'Departamento')
    goal = forms.ModelChoiceField(required=False, queryset=Goal.objects.all(), label= 'Meta')
