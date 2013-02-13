from __future__ import absolute_import

from django.contrib import admin

from .models import Purpose, Classification, Project, Detail, Stage, FiscalYear


class PurposeAdmin(admin.ModelAdmin):
    model = Purpose


class ClassificationAdmin(admin.ModelAdmin):
    model = Classification


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('label', 'fiscal_year', 'purpose', 'classification', 'department')


class DetailAdmin(admin.ModelAdmin):
    model = Detail
    list_display = ('project', 'start_period', 'end_period', 'stage')


class StageAdmin(admin.ModelAdmin):
    model = Stage


class FiscalYearAdmin(admin.ModelAdmin):
    model = FiscalYear


admin.site.register(Purpose, PurposeAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Detail, DetailAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(FiscalYear, FiscalYearAdmin)
