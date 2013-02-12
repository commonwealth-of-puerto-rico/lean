from __future__ import absolute_import

from django.contrib import admin

from .models import Agency


class AgencyAdmin(admin.ModelAdmin):
    model = Agency
    #list_display = ('user', 'document', 'datetime_accessed')
    #readonly_fields = ('user', 'document', 'datetime_accessed')
    #list_filter = ('user',)
    #date_hierarchy = 'datetime_accessed'


admin.site.register(Agency, AgencyAdmin)
