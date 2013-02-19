from __future__ import absolute_import

from django import forms

from common.forms import DetailForm, ROFormMixin

from .models import Project, ProjectInfo, ProjectBudget, ProjectDetails, ProjectOpportunities


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

## Budget

class ProjectBudgetForm_edit(forms.ModelForm, ROFormMixin):
    readonly_fields = ('project',)

    class Meta:
        model = ProjectBudget


class ProjectBudgetForm_view(DetailForm):
    class Meta:
        model = ProjectBudget


class ProjectBudgetForm_create(forms.ModelForm):
    class Meta:
        exclude = ('project',)
        model = ProjectBudget


## Details

class ProjectDetailsForm_edit(forms.ModelForm, ROFormMixin):
    readonly_fields = ('project',)

    class Meta:
        model = ProjectDetails


class ProjectDetailsForm_view(DetailForm):
    class Meta:
        model = ProjectDetails


class ProjectDetailsForm_create(forms.ModelForm):
    class Meta:
        exclude = ('project',)
        model = ProjectDetails


## Opportunities

class ProjectOpportunitiesForm_edit(forms.ModelForm, ROFormMixin):
    readonly_fields = ('project',)

    class Meta:
        model = ProjectOpportunities
        #widgets = {'opportunity': forms.widgets.CheckboxSelectMultiple}

    def __init__(self, *args, **kwargs):
        super(ProjectOpportunitiesForm_edit, self).__init__(*args, **kwargs)
        #self.fields['opportunity'].help_text = ''

class ProjectOpportunitiesForm_view(DetailForm):
    class Meta:
        model = ProjectOpportunities


class ProjectOpportunitiesForm_create(forms.ModelForm):
    class Meta:
        exclude = ('project',)
        model = ProjectOpportunities
