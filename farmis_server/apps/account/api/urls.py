from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    FarmerProfileViewSet, GenericProfileViewSet,
    ResearcherProfileViewSet,ProviderProfileViewSet,
    GovProfileViewSet, InvestorProfileViewSet, NGOProfileViewSet,
)


# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'farmer_profile', FarmerProfileViewSet)
router.register(r'researcher_profile', ResearcherProfileViewSet)
router.register(r'generic_profile', GenericProfileViewSet)
router.register(r'investor_profile', InvestorProfileViewSet)
router.register(r'ngo_profile', NGOProfileViewSet)
router.register(r'gov_profile', GovProfileViewSet)




# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
