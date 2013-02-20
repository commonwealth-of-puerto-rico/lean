from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('agencies.views',
    url(r'^list/$', 'agency_list', (), 'agency_list'),
    url(r'^(?P<agency_pk>\d+)/edit/$', 'agency_edit', (), 'agency_edit'),
    url(r'^(?P<agency_pk>\d+)/delete/$', 'agency_delete', (), 'agency_delete'),
    url(r'^(?P<agency_pk>\d+)/details/$', 'agency_details', (), 'agency_details'),
    url(r'^(?P<agency_pk>\d+)/view/$', 'agency_view', (), 'agency_view'),
)
