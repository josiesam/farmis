from typing import List, Dict, Any

from django.db import transaction

from apps.common.services import model_update
from apps.account.models import InvestorProfile



def investor_profile_create(*, user) -> InvestorProfile:
    investor_profile = InvestorProfile(user=user)
    investor_profile.full_clean()
    investor_profile.save()
    

    return investor_profile


@transaction.atomic
def investor_profile_update(*, investor_profile: InvestorProfile, fields: List[str], data: Dict[str, Any]) -> InvestorProfile:

    investor_profile.refresh_from_db()
    investor_profile, has_updated = model_update(
        instance=investor_profile, fields=fields, data=data)

    return investor_profile


@transaction.atomic
def investor_profile_delete(*, investor_profile: InvestorProfile):

    investor_profile = investor_profile.delete()

    return investor_profile
