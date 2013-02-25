from __future__ import absolute_import

from django.contrib import admin

from .models import Agency


class AgencyAdmin(admin.ModelAdmin):
    model = Agency
    list_display = ('enabled', 'registration', 'name')


admin.site.register(Agency, AgencyAdmin)
