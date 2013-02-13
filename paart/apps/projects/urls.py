from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('projects.views',
    url(r'^list/$', 'project_list', (), 'project_list'),
    url(r'^(?P<agency_pk>\d+)/list/$', 'agency_project_list', (), 'agency_project_list'),
    url(r'^(?P<project_pk>\d+)/edit/$', 'project_edit', (), 'project_edit'),
    url(r'^(?P<project_pk>\d+)/delete/$', 'project_delete', (), 'project_delete'),
)
