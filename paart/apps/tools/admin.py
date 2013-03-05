from __future__ import absolute_import

from django.contrib import admin

from .models import (Antivirus, Backup, Database, Development, Email, Firewall,
    ToolsProfile)


class ToolsProfileAdmin(admin.ModelAdmin):
    model = ToolsProfile
    #list_display = ('label', 'fiscal_year', 'purpose', 'classification', 'department')
    filter_horizontal = ('backup', 'database', 'development', 'email',
        'firewall', 'antivirus',)


admin.site.register(Antivirus)
admin.site.register(Backup)
admin.site.register(Database)
admin.site.register(Development)
admin.site.register(Email)
admin.site.register(Firewall)
admin.site.register(ToolsProfile, ToolsProfileAdmin)
