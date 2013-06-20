from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('reports.views',
    url(r'^$', 'project_reports_view', (), 'project_reports_view'),
)
