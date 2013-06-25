from __future__ import absolute_import

from django import forms

from agencies.models import Agency

class SelectAgencyForm(forms.Form):
    readonly_fields = ('name','id',)
    
    class Meta:
        model = Agency
        fields = ('name', 'id',)
        
    form = forms.ModelChoiceField(queryset=Agency.objects.all())
    
