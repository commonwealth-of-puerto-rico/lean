from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('software.views',
    url(r'^agency/(?P<agency_pk>\d+)/software/list/$', 'agency_software_list', (), 'agency_software_list'),
#    url(r'^agency/software/(?P<software_pk>\d+)/edit/$', 'agency_software_edit', (), 'agency_software_edit'),
#    url(r'^agency/software/(?P<software_pk>\d+)/delete/$', 'agency_software_delete', (), 'agency_software_delete'),
#    url(r'^agency/software/(?P<software_pk>\d+)/$', 'agency_software_view', (), 'agency_software_view'),
#    url(r'^agency/(?P<agency_pk>\d+)/software/create/$', 'agency_software_create', (), 'agency_software_create'),
)
