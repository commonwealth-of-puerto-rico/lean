from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tools.views',
    url(r'^(?P<agency_pk>\d+)/list/$', 'agency_tools_profile_list', (), 'agency_tools_profile_list'),
    url(r'^(?P<tools_profile_pk>\d+)/edit/$', 'tools_profile_edit', (), 'tools_profile_edit'),
    url(r'^(?P<tools_profile_pk>\d+)/delete/$', 'tools_profile_delete', (), 'tools_profile_delete'),
    url(r'^(?P<tools_profile_pk>\d+)/$', 'tools_profile_view', (), 'tools_profile_view'),
    url(r'^agency/(?P<agency_pk>\d+)/create/$', 'tools_profile_create', (), 'tools_profile_create'),
)
