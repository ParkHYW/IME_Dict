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

class ComputerAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Computer, ComputerAdmin)

class CostAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Cost, CostAdmin)

class DistributionAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Distribution, DistributionAdmin)

class EmployeeAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Employee, EmployeeAdmin)

class EngineeringAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Engineering, EngineeringAdmin)

class FacilityAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Facility, FacilityAdmin)

class HumanAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Human, HumanAdmin)

class ManagementAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Management, ManagementAdmin)

class ManufacturingAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Manufacturing, ManufacturingAdmin)

class MaterialsAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Materials, MaterialsAdmin)

class OccupationalAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Occupational, OccupationalAdmin)

class OperationsAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Operations, OperationsAdmin)

class OrganizationAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Organization, OrganizationAdmin)

class QualityAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Quality, QualityAdmin)

class WorkAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Work, WorkAdmin)