from __future__ import absolute_import

from django import forms

from agencies.models import Agency
    
class AgencySearchForm(forms.Form):
    agency_text = forms.CharField()
    
