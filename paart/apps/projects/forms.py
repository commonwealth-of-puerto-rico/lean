from __future__ import absolute_import

from django import forms

from common.forms import DetailForm, ROFormMixin

from .models import Project, ProjectInfo


class ProjectForm_edit(forms.ModelForm, ROFormMixin):
    readonly_fields = ('agency',)

    class Meta:
        model = Project


class ProjectForm_create(forms.ModelForm):
    class Meta:
        exclude = ('agency',)
        model = Project


class ProjectForm_view(DetailForm):
    class Meta:
        model = Project


class ProjectInfoForm_edit(forms.ModelForm, ROFormMixin):
    readonly_fields = ('project',)

    class Meta:
        model = ProjectInfo


class ProjectInfoForm_view(DetailForm):
    class Meta:
        model = ProjectInfo


class ProjectInfoForm_create(forms.ModelForm):
    class Meta:
        exclude = ('project',)
        model = ProjectInfo
