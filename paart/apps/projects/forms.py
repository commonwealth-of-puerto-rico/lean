from __future__ import absolute_import

import datetime

from django import forms

from common.forms import DetailForm, ROFormMixin

from .models import (Project, ProjectInfo, ProjectBudget, ProjectDetails,
    ProjectOpportunities, ProjectFile)


class ProjectForm_edit(forms.ModelForm, ROFormMixin):
    readonly_fields = ('agency',)

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['agency'].queryset = self.fields['agency'].queryset.active()

    class Meta:
        model = Project


class ProjectForm_create(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['agency'].queryset = self.fields['agency'].queryset.active()

    class Meta:
        exclude = ('agency',)
        model = Project


class ProjectForm_view(DetailForm):
    class Meta:
        model = Project


class ProjectInfoForm_edit(forms.ModelForm, ROFormMixin):
    readonly_fields = ('project',)

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['purpose'].queryset = self.fields['purpose'].queryset.active()
        self.fields['classification'].queryset = self.fields['classification'].queryset.active()

    class Meta:
        model = ProjectInfo


class ProjectInfoForm_view(DetailForm):
    class Meta:
        model = ProjectInfo


class ProjectInfoForm_create(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['purpose'].queryset = self.fields['purpose'].queryset.active()
        self.fields['classification'].queryset = self.fields['classification'].queryset.active()

        # Determine the current fiscal year in string form
        init_year = datetime.datetime.now().year
        if datetime.datetime.now().month < 7:
            init_year -= 1
        
        try:
            # do a lookup for the fiscal year label
            fiscal_year = self.fields['fiscal_year'].queryset.get(label='%s-%s' % (init_year + 1, init_year + 2))
        except self.fields['fiscal_year'].queryset.model.DoesNotExist:
            pass
        else:
            self.fields['fiscal_year'].initial = fiscal_year

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

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['stage'].queryset = self.fields['stage'].queryset.active()
        # self.fields['benefit'].queryset = self.fields['benefit'].queryset.active()
        # self.fields['topic'].queryset = self.fields['topic'].queryset.active()

    class Meta:
        model = ProjectDetails


class ProjectDetailsForm_view(DetailForm):
    class Meta:
        model = ProjectDetails


class ProjectDetailsForm_create(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['stage'].queryset = self.fields['stage'].queryset.active()
        # self.fields['benefit'].queryset = self.fields['benefit'].queryset.active()
        # self.fields['topic'].queryset = self.fields['topic'].queryset.active()

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
        super(self.__class__, self).__init__(*args, **kwargs)
        #self.fields['opportunity'].help_text = ''
        self.fields['other_agencies'].queryset = self.fields['other_agencies'].queryset.active()


class ProjectOpportunitiesForm_view(DetailForm):
    class Meta:
        model = ProjectOpportunities


class ProjectOpportunitiesForm_create(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        #self.fields['opportunity'].help_text = ''
        self.fields['other_agencies'].queryset = self.fields['other_agencies'].queryset.active()

    class Meta:
        exclude = ('project',)
        model = ProjectOpportunities
        #widgets = {'other_agencies': forms.widgets.CheckboxSelect}


## Project files

class ProjectFileForm_create(forms.ModelForm):
    class Meta:
        exclude = ('project',)
        #widgets = {'project': forms.widgets.HiddenInput}
        model = ProjectFile

