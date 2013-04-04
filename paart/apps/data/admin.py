from __future__ import absolute_import

from django.contrib import admin

from .models import DataType, AgencyData


class AgencyDataAdmin(admin.ModelAdmin):
    model = AgencyData
    list_display = ('label', 'data_type', 'description')


admin.site.register(DataType)
admin.site.register(AgencyData, AgencyDataAdmin)
