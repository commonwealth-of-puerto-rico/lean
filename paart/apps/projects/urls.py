from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('projects.views',
    url(r'^(?P<project_pk>\d+)/edit/$', 'project_edit', (), 'project_edit'),
    url(r'^(?P<project_pk>\d+)/delete/$', 'project_delete', (), 'project_delete'),
    url(r'^(?P<project_pk>\d+)/view/$', 'project_view', (), 'project_view'),
    url(r'^(?P<agency_pk>\d+)/create/$', 'project_create', (), 'project_create'),

    url(r'^(?P<project_info_pk>\d+)/info/edit/$', 'project_info_edit', (), 'project_info_edit'),
    url(r'^(?P<project_info_pk>\d+)/info/delete/$', 'project_info_delete', (), 'project_info_delete'),
    url(r'^(?P<project_pk>\d+)/info/view/$', 'project_info_view', (), 'project_info_view'),
    url(r'^(?P<project_pk>\d+)/info/create/$', 'project_info_create', (), 'project_info_create'),

    url(r'^(?P<project_budget_pk>\d+)/budget/edit/$', 'project_budget_edit', (), 'project_budget_edit'),
    url(r'^(?P<project_budget_pk>\d+)/budget/delete/$', 'project_budget_delete', (), 'project_budget_delete'),
    url(r'^(?P<project_pk>\d+)/budget/view/$', 'project_budget_view', (), 'project_budget_view'),
    url(r'^(?P<project_pk>\d+)/budget/create/$', 'project_budget_create', (), 'project_budget_create'),

    url(r'^agency/(?P<agency_pk>\d+)/list/$', 'agency_project_list', (), 'agency_project_list'),
    #url(r'^agency/(?P<agency_pk>\d+)/create/$', 'project_create_wizard', (), 'project_create_wizard'),
)
