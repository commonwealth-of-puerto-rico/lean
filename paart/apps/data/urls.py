from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('data.views',
    url(r'^agency/(?P<agency_pk>\d+)/data/list/$', 'agency_data_list', (), 'agency_data_list'),
    url(r'^(?P<data_pk>\d+)/edit/$', 'data_edit', (), 'data_edit'),
    url(r'^(?P<data_pk>\d+)/delete/$', 'data_delete', (), 'data_delete'),
    url(r'^(?P<data_pk>\d+)/$', 'data_view', (), 'data_view'),
    url(r'^agency/(?P<agency_pk>\d+)/data/create/$', 'data_create', (), 'data_create'),
)
