from django.contrib import admin

# Register your models here.

from .models import (
    ProviderProfile, GovProfile, NGOProfile, FarmerProfile,
    ResearcherProfile, GenericProfile,InvestorProfile, 
)

@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(GovProfile)
class GovProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(NGOProfile)
class NGOProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(InvestorProfile)
class InvestorProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(ResearcherProfile)
class ResearcherProfileAdmin(admin.ModelAdmin):
    pass   

@admin.register(GenericProfile)
class GenericProfileAdmin(admin.ModelAdmin):
    pass
