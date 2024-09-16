from apps.account.filters import GenericProfileFilter
from apps.account.models import GenericProfile

def generic_profile_list(*, filters=None): 
    filters = filters or {}

    qs = GenericProfile.objects.all()

    return GenericProfileFilter(filters, qs).qs