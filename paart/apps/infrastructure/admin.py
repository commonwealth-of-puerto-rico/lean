from __future__ import absolute_import

from django.contrib import admin

from .models import (FiscalYear, Project, ProjectInfo, ProjectBudget)


class FiscalYearAdmin(admin.ModelAdmin):
    model = FiscalYear


class ProjectAdmin(admin.ModelAdmin):
    model = Project


class ProjectProjectInfoAdmin(admin.ModelAdmin):
    model = ProjectInfo


class ProjectProjectBudgetAdmin(admin.ModelAdmin):
    model = ProjectBudget


admin.site.register(FiscalYear, FiscalYearAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectInfo, ProjectProjectInfoAdmin)
admin.site.register(ProjectBudget, ProjectProjectBudgetAdmin)
