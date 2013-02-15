from __future__ import absolute_import

from django.contrib import admin

from .models import Provider, Equipment


class ProviderAdmin(admin.ModelAdmin):
    model = Provider


class EquipmentAdmin(admin.ModelAdmin):
    model = Equipment
    #list_display = ('label', 'fiscal_year', 'purpose', 'classification', 'department')
    #filter_horizontal = ('opportunity', 'sharing_benefit')


admin.site.register(Provider, ProviderAdmin)
admin.site.register(Equipment, EquipmentAdmin)
