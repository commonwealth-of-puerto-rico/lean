from __future__ import absolute_import

from django import forms

from agencies.models import Agency
from projects.models import ProjectInfo, FiscalYear
    
class AgencySearchForm(forms.Form):
    agency_text = forms.CharField()
    fiscal_year = forms.ModelChoiceField(queryset=FiscalYear.objects.all(), label= 'Fiscal Year')
