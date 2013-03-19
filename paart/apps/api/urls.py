from __future__ import absolute_import

from django.conf.urls import patterns, url, include

from .views import AgencyList, AgencyDetail, StatusList#, StatusDetail


urlpatterns = patterns('api.views',
    url(r'^$', 'api_root'),

    url(r'^v0/$', 'version_0', name='api-version-0'),

    url(r'^v0/agencies/$', AgencyList.as_view(), name='agency-list'),
    url(r'^v0/agencies/(?P<pk>[0-9]+)/$', AgencyDetail.as_view(), name='agency-detail'),

    url(r'^v0/status/$', StatusList.as_view(), name='status-list'),
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
)
