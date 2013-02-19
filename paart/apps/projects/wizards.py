from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.http import urlencode

from common.wizard import BoundFormWizard

from .icons import icon_wizard_next_step


class ProjectCreateWizard_old(BoundFormWizard):
    def generate_metadata_initial_values(self):
        initial = []
        for metadata_type in self.metadata_types:
            initial.append({
                'metadata_type': metadata_type,
            })

        for metadata_set in self.metadata_sets:
            for metadata_set_item in metadata_set.metadatasetitem_set.all():
                data = {
                    'metadata_type': metadata_set_item.metadata_type,
                }
                if data not in initial:
                    initial.append(data)

        return initial

    def __init__(self, *args, **kwargs):
        self.view_extra_context = kwargs.pop('view_extra_context', None)
        self.query_dict = {}
        self.step_titles = kwargs.pop('step_titles', [
            _(u'step 1 of 4: General information'),
            _(u'step 2 of 4: Budget'),
            _(u'step 3 of 4: Equipment'),
            _(u'step 4 of 4: Timeframe'),
            ])

        super(ProjectCreateWizard, self).__init__(*args, **kwargs)

    def render_template(self, request, form, previous_fields, step, context=None):
        context = {
            'step_title': self.extra_context['step_titles'][step],
            'submit_label': _(u'Next step'),
            'submit_icon': icon_wizard_next_step,
        }
        if self.view_extra_context:
            context.update(self.view_extra_context)

        return super(ProjectCreateWizard, self).render_template(
            request, form, previous_fields, step, context
        )

    def parse_params(self, request, *args, **kwargs):
        self.extra_context = {'step_titles': self.step_titles}

    def process_step(self, request, form, step):
        step_data = self.get_step_data(step)

        #if isinstance(form, DocumentTypeSelectForm):
        #    self.document_type = form.cleaned_data['document_type']
        #    self.initial = {1: {'document_type': self.document_type}}

        #if isinstance(form, MetadataSelectionForm):
        #    self.metadata_sets = form.cleaned_data['metadata_sets']
        #    self.metadata_types = form.cleaned_data['metadata_types']
        #    initial_data = self.generate_metadata_initial_values()
        #    self.initial = {2: initial_data}
        #    if not initial_data:
        #        # If there is no metadata selected, finish wizard
        #        self.form_list = [DocumentTypeSelectForm, MetadataSelectionForm]

        #if isinstance(form, MetadataFormSet):
        #    for identifier, metadata in enumerate(form.cleaned_data):
        #        self.query_dict['metadata%s_id' % identifier] = metadata['id']
        #        self.query_dict['metadata%s_value' % identifier] = metadata['value']

    def get_template(self, step):
        return 'generic_wizard.html'

    def done(self, request, form_list):
        #if self.document_type:
        #    self.query_dict['document_type_id'] = self.document_type.pk
        url = '?'.join(['/', urlencode(self.query_dict, doseq=True)])
        return HttpResponseRedirect(url)


from django.contrib.formtools.wizard.views import SessionWizardView
from django.utils.decorators import classonlymethod

from .forms import ProjectForm_detail


class ProjectCreateWizard(SessionWizardView):
    @classonlymethod
    def as_view(cls, *args, **kwargs):
        cls.view_extra_context = kwargs.pop('view_extra_context', None)
        cls.agency = kwargs.pop('agency', None)
        cls.model = kwargs.pop('model', None)
        cls.step_titles = kwargs.pop('step_titles', None)

        return super(ProjectCreateWizard, cls).as_view(*args, **kwargs)

    def get_context_data(self, form, **kwargs):
        context = super(ProjectCreateWizard, self).get_context_data(form=form, **kwargs)

        context.update({
            'step_title': self.step_titles[int(self.steps.current)],
            'submit_label': _(u'Next step'),
            'submit_icon': icon_wizard_next_step,
        })
        if self.view_extra_context:
            context.update(self.view_extra_context)

        return context

    def get_template_names(self):
        return 'generic_wizard.html'

    def done(self, form_list, **kwargs):
        form_data = {}

        for form in form_list:
            form_data.update(form.cleaned_data)

        print 'form_data', form_data
        instance = self.__class__.model(agency=self.__class__.agency, **form_data)
        instance.save(commit=False)

        #return HttpResponseRedirect('/page-to-redirect-to-when-done/')
