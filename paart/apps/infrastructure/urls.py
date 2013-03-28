from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('infrastructure.views',
    url(r'^agency/(?P<agency_pk>\d+)/create/$', 'project_create', (), 'infrastructure_project_create'),
    url(r'^(?P<project_pk>\d+)/edit/$', 'project_edit', (), 'infrastructure_project_edit'),
    url(r'^(?P<project_pk>\d+)/delete/$', 'project_delete', (), 'infrastructure_project_delete'),
    url(r'^(?P<project_pk>\d+)/view/$', 'project_view', (), 'infrastructure_project_view'),

    #url(r'^(?P<project_info_pk>\d+)/info/edit/$', 'project_info_edit', (), 'infrastructure_project_info_edit'),
    #url(r'^(?P<project_info_pk>\d+)/info/delete/$', 'project_info_delete', (), 'infrastructure_project_info_delete'),
    #url(r'^(?P<project_pk>\d+)/info/view/$', 'project_info_view', (), 'infrastructure_project_info_view'),
    #url(r'^(?P<project_pk>\d+)/info/create/$', 'project_info_create', (), 'infrastructure_project_info_create'),

    #url(r'^(?P<project_budget_pk>\d+)/budget/edit/$', 'project_budget_edit', (), 'infrastructure_project_budget_edit'),
    #url(r'^(?P<project_budget_pk>\d+)/budget/delete/$', 'project_budget_delete', (), 'infrastructure_project_budget_delete'),
    #url(r'^(?P<project_pk>\d+)/budget/view/$', 'project_budget_view', (), 'infrastructure_project_budget_view'),
    #url(r'^(?P<project_pk>\d+)/budget/create/$', 'project_budget_create', (), 'infrastructure_project_budget_create'),

    url(r'^(?P<project_pk>\d+)/files/list/$', 'project_file_list', (), 'infrastructure_project_file_list'),
    url(r'^(?P<project_pk>\d+)/files/upload/$', 'project_file_upload', (), 'infrastructure_project_file_upload'),
    url(r'^file/(?P<project_file_pk>\d+)/delete/$', 'project_file_delete', (), 'infrastructure_project_file_delete'),
    url(r'^file/(?P<project_file_pk>\d+)/download/$', 'project_file_download', (), 'infrastructure_project_file_download'),

    url(r'^agency/(?P<agency_pk>\d+)/list/$', 'agency_project_list', (), 'agency_infrastructure_project_list'),
)
