from apps.account.filters import GovProfileFilter
from apps.account.models import GovProfile

def gov_profile_list(*, filters=None): 
    filters = filters or {}

    qs = GovProfile.objects.all()

    return GovProfileFilter(filters, qs).qs