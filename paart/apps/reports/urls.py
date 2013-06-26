from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('reports.views',
    url(r'^$', 'agency_search_form', (), 'agency_search_form'),
    url(r'^agency-busqueda-report/$', 'agency_busqueda_report', (), 'agency_busqueda_report'),
)
