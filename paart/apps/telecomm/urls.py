from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('telecomm.views',
    url(r'^agency/(?P<agency_pk>\d+)/list/$', 'agency_equipment_list', (), 'agency_equipment_list'),
    url(r'^(?P<equipment_pk>\d+)/edit/$', 'equipment_edit', (), 'equipment_edit'),
    url(r'^(?P<equipment_pk>\d+)/delete/$', 'equipment_delete', (), 'equipment_delete'),
    url(r'^(?P<equipment_pk>\d+)/$', 'equipment_view', (), 'equipment_view'),
    url(r'^agency/(?P<agency_pk>\d+)/create/$', 'equipment_create', (), 'equipment_create'),
)
