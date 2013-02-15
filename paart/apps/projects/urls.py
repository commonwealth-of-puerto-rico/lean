from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('projects.views',
    url(r'^(?P<project_pk>\d+)/edit/$', 'project_edit', (), 'project_edit'),
    url(r'^(?P<project_pk>\d+)/delete/$', 'project_delete', (), 'project_delete'),
    url(r'^(?P<project_pk>\d+)/view/$', 'project_view', (), 'project_view'),
    url(r'^agency/(?P<agency_pk>\d+)/list/$', 'agency_project_list', (), 'agency_project_list'),
    url(r'^agency/(?P<agency_pk>\d+)/create/$', 'project_create_wizard', (), 'project_create_wizard'),
)
