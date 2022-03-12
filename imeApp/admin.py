from django.contrib import admin 
from .models import *
from import_export.admin import ImportExportMixin

# 엑셀 연결

class CompanyAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Company, CompanyAdmin)


class AnalyticsAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Analytics, CompanyAdmin)

class AnthropometryAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Anthropometry, AnthropometryAdmin)