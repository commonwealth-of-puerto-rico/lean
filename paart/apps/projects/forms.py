from __future__ import absolute_import

from django import forms

from common.forms import DetailForm, ROFormMixin

from .models import Project


class ProjectForm(forms.ModelForm, ROFormMixin):
    readonly_fields = ('agency',)

    class Meta:
        model = Project


class ProjectForm_step1(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('label', 'fiscal_year', 'purpose', 'purpose_other', 'classification', 'classification_other', 'department', 'sponsor', 'email', 'phone_number', 'goals', 'needs', 'expected_results', 'methodology', 'milestones')


class ProjectForm_step2(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('infrastructure', 'requirements', 'presumptions', 'limitations', 'risks', 'benefits')


class ProjectForm_detail(DetailForm):
    class Meta:
        model = Project
