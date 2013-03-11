from __future__ import absolute_import

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _

from .models import Agency


class InitialListFilter(SimpleListFilter):
    title = _(u'initial')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'name'

    def lookups(self, request, model_admin):
        return [(l, l) for l in set([a[0] for a in model_admin.model.objects.all().values_list('name', flat=True)])]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            return queryset.filter(name__startswith=self.value())
        else:
            return queryset.all()


class AgencyAdmin(admin.ModelAdmin):
    model = Agency
    list_display = ('prifas', 'registration', 'name', 'enabled')
    list_display_links = ('prifas', 'registration', 'name')
    list_filter = (InitialListFilter, )

admin.site.register(Agency, AgencyAdmin)
