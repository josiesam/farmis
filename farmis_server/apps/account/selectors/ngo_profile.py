from apps.account.filters import NGOProfileFilter
from apps.account.models import NGOProfile

def ngo_profile_list(*, filters=None): 
    filters = filters or {}

    qs = NGOProfile.objects.all()

    return NGOProfileFilter(filters, qs).qs