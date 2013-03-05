from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('projects.views',
    url(r'^(?P<project_pk>\d+)/edit/$', 'project_edit', (), 'project_edit'),
    url(r'^(?P<project_pk>\d+)/delete/$', 'project_delete', (), 'project_delete'),
    url(r'^(?P<project_pk>\d+)/view/$', 'project_view', (), 'project_view'),
    url(r'^agency/(?P<agency_pk>\d+)/create/$', 'project_create', (), 'project_create'),

    url(r'^(?P<project_info_pk>\d+)/info/edit/$', 'project_info_edit', (), 'project_info_edit'),
    url(r'^(?P<project_info_pk>\d+)/info/delete/$', 'project_info_delete', (), 'project_info_delete'),
    url(r'^(?P<project_pk>\d+)/info/view/$', 'project_info_view', (), 'project_info_view'),
    url(r'^(?P<project_pk>\d+)/info/create/$', 'project_info_create', (), 'project_info_create'),

    url(r'^(?P<project_budget_pk>\d+)/budget/edit/$', 'project_budget_edit', (), 'project_budget_edit'),
    url(r'^(?P<project_budget_pk>\d+)/budget/delete/$', 'project_budget_delete', (), 'project_budget_delete'),
    url(r'^(?P<project_pk>\d+)/budget/view/$', 'project_budget_view', (), 'project_budget_view'),
    url(r'^(?P<project_pk>\d+)/budget/create/$', 'project_budget_create', (), 'project_budget_create'),

    url(r'^(?P<project_details_pk>\d+)/details/edit/$', 'project_details_edit', (), 'project_details_edit'),
    url(r'^(?P<project_details_pk>\d+)/details/delete/$', 'project_details_delete', (), 'project_details_delete'),
    url(r'^(?P<project_pk>\d+)/details/view/$', 'project_details_view', (), 'project_details_view'),
    url(r'^(?P<project_pk>\d+)/details/create/$', 'project_details_create', (), 'project_details_create'),

    url(r'^(?P<project_opportunities_pk>\d+)/opportunities/edit/$', 'project_opportunities_edit', (), 'project_opportunities_edit'),
    url(r'^(?P<project_opportunities_pk>\d+)/opportunities/delete/$', 'project_opportunities_delete', (), 'project_opportunities_delete'),
    url(r'^(?P<project_pk>\d+)/opportunities/view/$', 'project_opportunities_view', (), 'project_opportunities_view'),
    url(r'^(?P<project_pk>\d+)/opportunities/create/$', 'project_opportunities_create', (), 'project_opportunities_create'),

    url(r'^(?P<project_pk>\d+)/files/list/$', 'project_file_list', (), 'project_file_list'),
    url(r'^(?P<project_pk>\d+)/files/upload/$', 'project_file_upload', (), 'project_file_upload'),
    url(r'^file/(?P<project_file_pk>\d+)/delete/$', 'project_file_delete', (), 'project_file_delete'),
    url(r'^file/(?P<project_file_pk>\d+)/download/$', 'project_file_download', (), 'project_file_download'),

    url(r'^(?P<project_pk>\d+)/workflow/instance/list/$', 'project_workflow_instance_list', (), 'project_workflow_instance_list'),
    url(r'^workflow/instance/(?P<workflow_instance_pk>\d+)/history/list/$', 'project_workflow_instance_history_list', (), 'project_workflow_instance_history_list'),
    url(r'^workflow/instance/(?P<workflow_instance_pk>\d+)/action/create/$', 'project_workflow_instance_action_submit', (), 'project_workflow_instance_action_submit'),

    url(r'^agency/(?P<agency_pk>\d+)/list/$', 'agency_project_list', (), 'agency_project_list'),
    #url(r'^agency/(?P<agency_pk>\d+)/create/$', 'project_create_wizard', (), 'project_create_wizard'),
)
