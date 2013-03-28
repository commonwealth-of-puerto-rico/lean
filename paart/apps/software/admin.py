from __future__ import absolute_import

from django.contrib import admin

from .models import AgencySoftware, Software, SoftwareType


class AgencySoftwareAdmin(admin.ModelAdmin):
    model = AgencySoftware
    list_display = ('agency', 'software', 'amount')


class SoftwareAdmin(admin.ModelAdmin):
    model = Software
    list_display = ('label', 'software_type')


admin.site.register(AgencySoftware, AgencySoftwareAdmin)
admin.site.register(SoftwareType)
admin.site.register(Software, SoftwareAdmin)

