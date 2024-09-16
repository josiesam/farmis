import django_filters

from apps.account.models import (
    GenericProfile, ResearcherProfile, FarmerProfile,
    NGOProfile, GovProfile, InvestorProfile, ProviderProfile
)


class GenericProfileFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name="user__phone_number", lookup_expr="iexact")
    class Meta:
        model = GenericProfile

class FarmerProfileFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name="user__phone_number", lookup_expr="iexact")
    class Meta:
        model = FarmerProfile

class ResearcherProfileFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name="user__phone_number", lookup_expr="iexact")
    class Meta:
        model = ResearcherProfile

class InvestorProfileFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name="user__phone_number", lookup_expr="iexact")
    class Meta:
        model = InvestorProfile

class NGOProfileFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name="user__phone_number", lookup_expr="iexact")
    class Meta:
        model = NGOProfile

class GovProfileFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name="user__phone_number", lookup_expr="iexact")
    class Meta:
        model = GovProfile

class ProviderProfileFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name="user__phone_number", lookup_expr="iexact")
    class Meta:
        model = ProviderProfile

