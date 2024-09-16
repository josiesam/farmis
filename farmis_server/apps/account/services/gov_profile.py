from typing import List, Dict, Any

from django.db import transaction

from apps.common.services import model_update
from apps.account.models import GovProfile



def gov_profile_create(*, user) -> GovProfile:
    gov_profile = GovProfile(user=user)
    gov_profile.full_clean()
    gov_profile.save()
    

    return gov_profile


@transaction.atomic
def gov_profile_update(*, gov_profile: GovProfile, fields: List[str], data: Dict[str, Any]) -> GovProfile:

    gov_profile.refresh_from_db()
    gov_profile, has_updated = model_update(
        instance=gov_profile, fields=fields, data=data)

    return gov_profile


@transaction.atomic
def gov_profile_delete(*, gov_profile: GovProfile):

    gov_profile = gov_profile.delete()

    return gov_profile
