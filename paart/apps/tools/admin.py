from __future__ import absolute_import

from django.contrib import admin

from .models import Development, Backup, Firewall, Antivirus, ToolsProfile


class ToolsProfileAdmin(admin.ModelAdmin):
    model = ToolsProfile
    #list_display = ('label', 'fiscal_year', 'purpose', 'classification', 'department')
    filter_horizontal = ('development', 'backup', 'firewall', 'antivirus',)


admin.site.register(Development)
admin.site.register(Backup)
admin.site.register(Firewall)
admin.site.register(Antivirus)
admin.site.register(ToolsProfile, ToolsProfileAdmin)
