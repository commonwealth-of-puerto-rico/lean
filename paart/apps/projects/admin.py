from __future__ import absolute_import

from django.contrib import admin

from .models import (FiscalYear, Purpose, Classification, Stage, Benefit,
    Topic, Opportunity, Project, ProjectInfo)


class FiscalYearAdmin(admin.ModelAdmin):
    model = FiscalYear


class PurposeAdmin(admin.ModelAdmin):
    model = Purpose


class ClassificationAdmin(admin.ModelAdmin):
    model = Classification


class StageAdmin(admin.ModelAdmin):
    model = Stage


class BenefitAdmin(admin.ModelAdmin):
    model = Benefit


class TopicAdmin(admin.ModelAdmin):
    model = Topic


class OpportunityAdmin(admin.ModelAdmin):
    model = Opportunity


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    #list_display = ('label', 'fiscal_year', 'purpose', 'classification', 'department')
    #filter_horizontal = ('opportunity', 'sharing_benefit')


class ProjectProjectInfoAdmin(admin.ModelAdmin):
    model = ProjectInfo
    #list_display = ('fiscal_year', 'purpose', 'classification', 'department')
    #filter_horizontal = ('opportunity', 'sharing_benefit')


admin.site.register(FiscalYear, FiscalYearAdmin)
admin.site.register(Purpose, PurposeAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Benefit, BenefitAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectInfo, ProjectProjectInfoAdmin)
