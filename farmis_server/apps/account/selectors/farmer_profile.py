from apps.account.filters import FarmerProfileFilter
from apps.account.models import FarmerProfile

def farmer_profile_list(*, filters=None): 
    filters = filters or {}

    qs = FarmerProfile.objects.all()

    return FarmerProfileFilter(filters, qs).qs