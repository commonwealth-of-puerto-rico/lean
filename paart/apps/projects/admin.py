from __future__ import absolute_import

from django.contrib import admin

from .models import FiscalYear, Purpose, Classification, Stage, Benefit, Topic, Opportunity, Project


class FiscalYearAdmin(admin.ModelAdmin):
    model = FiscalYear


class PurposeAdmin(admin.ModelAdmin):
    model = Purpose


class ClassificationAdmin(admin.ModelAdmin):
    model = Classification


class StageAdmin(admin.ModelAdmin):
    model = Stage


class BenefitAdmin(admin.ModelAdmin):
    model = Detail


class TopicAdmin(admin.ModelAdmin):
    model = Topic


class OpportunityAdmin(admin.ModelAdmin):
    model = Opportunity


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('label', 'fiscal_year', 'purpose', 'classification', 'department')






admin.site.register(Purpose, PurposeAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Detail, DetailAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(FiscalYear, FiscalYearAdmin)
