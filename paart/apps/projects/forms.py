from __future__ import absolute_import

import datetime

from django import forms

from django.utils.translation import ugettext_lazy as _


from common.forms import DetailForm, ROFormMixin, Select2FormMixin

from .models import (Project, ProjectInfo, ProjectBudget, ProjectDetails,
    ProjectOpportunities, ProjectFile)


class ProjectForm_edit(forms.ModelForm, ROFormMixin):
    readonly_fields = ('agency', )

    class Meta:
        exclude = ('datetime_created',)
        model = Project


class ProjectForm_create(forms.ModelForm):
    class Meta:
        exclude = ('agency', 'datetime_created',)
        model = Project


class ProjectForm_view(DetailForm):
    class Meta:
        model = Project
        fields = ('agency', 'label', 'datetime_created', 'description', )


class ProjectInfoForm_edit(Select2FormMixin, forms.ModelForm, ROFormMixin):
    readonly_fields = ('project',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['purpose'].queryset = self.fields['purpose'].queryset.active()
        self.fields['classification'].queryset = self.fields['classification'].queryset.active()
        self.fields['classification_secondary'].queryset = self.fields['classification_secondary'].queryset.active()
        self.fields['department'].queryset = self.fields['department'].queryset.active()
        self.fields['methodology'].queryset = self.fields['methodology'].queryset.active()
        self.fields['goals'].queryset = self.fields['goals'].queryset.active()

        if not user.is_staff:
            self.fields['state'].widget.attrs['readonly'] = True
            self.fields['state_note'].widget.attrs['readonly'] = True
        else:
            self.fields['state'].queryset = self.fields['state'].queryset.active()

    class Meta:
        model = ProjectInfo


class ProjectInfoForm_view(DetailForm):
    readonly_fields = ('state', 'state_note')

    class Meta:
        model = ProjectInfo


class ProjectInfoForm_create(Select2FormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['purpose'].queryset = self.fields['purpose'].queryset.active()
        self.fields['classification'].queryset = self.fields['classification'].queryset.active()
        self.fields['classification_secondary'].queryset = self.fields['classification_secondary'].queryset.active()
        self.fields['department'].queryset = self.fields['department'].queryset.active()
        self.fields['methodology'].queryset = self.fields['methodology'].queryset.active()
        self.fields['goals'].queryset = self.fields['goals'].queryset.active()

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

        # Project Initial State
        try:
            project_state = self.fields['state'].queryset.get(default=True)
        except self.fields['state'].queryset.model.DoesNotExist:
            pass
        else:
            self.fields['state'].initial = project_state

        if not user.is_staff:
            self.fields['state'].widget.attrs['readonly'] = True
            del self.fields['state_note']

    class Meta:
        exclude = ('project', )

        model = ProjectInfo

## Budget

class ProjectBudgetForm_edit(forms.ModelForm, ROFormMixin):
    readonly_fields = ('project',)

    class Meta:
        model = ProjectBudget
        widgets = {'infrastructure': forms.widgets.RadioSelect}


class ProjectBudgetForm_view(DetailForm):
    class Meta:
        model = ProjectBudget
        widgets = {'infrastructure': forms.widgets.RadioSelect}


class ProjectBudgetForm_create(forms.ModelForm):
    class Meta:
        exclude = ('project',)
        model = ProjectBudget
        widgets = {'infrastructure': forms.widgets.RadioSelect}


## Details

class ProjectDetailsForm_edit(Select2FormMixin, forms.ModelForm, ROFormMixin):
    readonly_fields = ('project',)

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['stage'].queryset = self.fields['stage'].queryset.active()
        self.fields['priority'].queryset = self.fields['priority'].queryset.active()
        # self.fields['benefit'].queryset = self.fields['benefit'].queryset.active()
        # self.fields['topic'].queryset = self.fields['topic'].queryset.active()

    class Meta:
        model = ProjectDetails


class ProjectDetailsForm_view(DetailForm):
    class Meta:
        model = ProjectDetails


class ProjectDetailsForm_create(Select2FormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['stage'].queryset = self.fields['stage'].queryset.active()
        self.fields['priority'].queryset = self.fields['priority'].queryset.active()
        # self.fields['benefit'].queryset = self.fields['benefit'].queryset.active()
        # self.fields['topic'].queryset = self.fields['topic'].queryset.active()

    class Meta:
        exclude = ('project',)
        model = ProjectDetails

## Opportunities

class ProjectOpportunitiesForm_edit(Select2FormMixin, forms.ModelForm, ROFormMixin):
    readonly_fields = ('project',)

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['other_agencies'].queryset = self.fields['other_agencies'].queryset.active()

    class Meta:
        model = ProjectOpportunities


class ProjectOpportunitiesForm_view(DetailForm):
    class Meta:
        model = ProjectOpportunities


class ProjectOpportunitiesForm_create(Select2FormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['other_agencies'].queryset = self.fields['other_agencies'].queryset.active()

    class Meta:
        exclude = ('project',)
        model = ProjectOpportunities


## Project files

class ProjectFileForm_create(forms.ModelForm):
    class Meta:
        exclude = ('project',)
        #widgets = {'project': forms.widgets.HiddenInput}
        model = ProjectFile

