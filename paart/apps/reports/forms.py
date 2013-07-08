# -*- coding: utf-8 -*- 

from __future__ import absolute_import

from django import forms

from agencies.models import Agency
from projects.models import (ProjectInfo, FiscalYear, Purpose, Classification, 
Methodology, Department, Goal)
    
class AgencySearchForm(forms.Form):
    agency_text = forms.CharField(label='Agencia') 
    fiscal_year = forms.ModelChoiceField(queryset=FiscalYear.objects.all(), label= 'Año Fiscal')
    purpose = forms.ModelChoiceField(queryset=Purpose.objects.all(), label= 'Proposito')
    classification = forms.ModelChoiceField(queryset=Classification.objects.all(), label= 'Clasificacíon')
    secondary_classification = forms.ModelChoiceField(queryset=Classification.objects.all(), label= 'Clasificación Secundaria')
    methodology = forms.ModelChoiceField(queryset=Methodology.objects.all(), label= 'Metodología')
    department = forms.ModelChoiceField(queryset=Department.objects.all(), label= 'Departamento')
    goal = forms.ModelChoiceField(queryset=Goal.objects.all(), label= 'Meta')
