from apps.account.filters import ResearcherProfileFilter
from apps.account.models import ResearcherProfile

def researcher_profile_list(*, filters=None): 
    filters = filters or {}

    qs = ResearcherProfile.objects.all()

    return ResearcherProfileFilter(filters, qs).qs