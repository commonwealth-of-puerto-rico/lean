from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Mayan apps
    (r'^', include('main.urls')),
    (r'^common/', include('common.urls')),
    (r'^project_setup/', include('project_setup.urls')),
    (r'^project_tools/', include('project_tools.urls')),
    (r'^acls/', include('acls.urls')),
    (r'^search/', include('dynamic_search.urls')),
    (r'^settings/', include('smart_settings.urls')),
    (r'^permissions/', include('permissions.urls')),
    (r'^user_management/', include('user_management.urls')),

    # Project
    (r'^agencies/', include('agencies.urls')),
    (r'^projects/', include('projects.urls')),
    (r'^telecomm/', include('telecomm.urls')),
    (r'^infrastructure/', include('infrastructure.urls')),
    (r'^tools/', include('tools.urls')),
    (r'^api/', include('api.urls')),
)

if settings.DEVELOPMENT:
    if 'rosetta' in settings.INSTALLED_APPS:
        urlpatterns += patterns('',
            url(r'^rosetta/', include('rosetta.urls'), name='rosetta'),
        )
