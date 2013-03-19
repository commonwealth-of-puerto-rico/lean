from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('telecomm.views',
    url(r'^agency/(?P<agency_pk>\d+)/circuit/list/$', 'agency_circuit_list', (), 'agency_circuit_list'),
    url(r'^(?P<circuit_pk>\d+)/edit/$', 'circuit_edit', (), 'circuit_edit'),
    url(r'^(?P<circuit_pk>\d+)/delete/$', 'circuit_delete', (), 'circuit_delete'),
    url(r'^(?P<circuit_pk>\d+)/$', 'circuit_view', (), 'circuit_view'),
    url(r'^agency/(?P<agency_pk>\d+)/circuit/create/$', 'circuit_create', (), 'circuit_create'),

    url(r'^agency/(?P<agency_pk>\d+)/equipment/list/$', 'agency_equipment_list', (), 'agency_equipment_list'),
    url(r'^(?P<equipment_pk>\d+)/edit/$', 'equipment_edit', (), 'equipment_edit'),
    url(r'^(?P<equipment_pk>\d+)/delete/$', 'equipment_delete', (), 'equipment_delete'),
    url(r'^(?P<equipment_pk>\d+)/$', 'equipment_view', (), 'equipment_view'),
    url(r'^agency/(?P<agency_pk>\d+)/equipment/create/$', 'equipment_create', (), 'equipment_create'),
)
