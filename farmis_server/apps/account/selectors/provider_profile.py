from apps.account.filters import ProviderProfileFilter
from apps.account.models import ProviderProfile

def provider_profile_list(*, filters=None): 
    filters = filters or {}

    qs = ProviderProfile.objects.all()

    return ProviderProfileFilter(filters, qs).qs