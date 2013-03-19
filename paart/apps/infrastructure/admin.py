from __future__ import absolute_import

from django.contrib import admin

from .models import (FiscalYear, Project, ProjectInfo)


class FiscalYearAdmin(admin.ModelAdmin):
    model = FiscalYear


class ProjectAdmin(admin.ModelAdmin):
    model = Project


class ProjectProjectInfoAdmin(admin.ModelAdmin):
    model = ProjectInfo


admin.site.register(FiscalYear, FiscalYearAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectInfo, ProjectProjectInfoAdmin)
