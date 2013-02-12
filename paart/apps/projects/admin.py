from __future__ import absolute_import

from django.contrib import admin

from .models import Purpose, Classification, Project, Detail


class PurposeAdmin(admin.ModelAdmin):
    model = Purpose


class ClassificationAdmin(admin.ModelAdmin):
    model = Classification


class ProjectAdmin(admin.ModelAdmin):
    model = Project


class DetailAdmin(admin.ModelAdmin):
    model = Detail


admin.site.register(Purpose, PurposeAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Detail, DetailAdmin)
