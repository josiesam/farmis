from typing import List, Dict, Any

from django.db import transaction

from apps.common.services import model_update
from apps.account.models import NGOProfile



def ngo_profile_create(*, user) -> NGOProfile:
    ngo_profile = NGOProfile(user=user)
    ngo_profile.full_clean()
    ngo_profile.save()
    

    return ngo_profile


@transaction.atomic
def ngo_profile_update(*, ngo_profile: NGOProfile, fields: List[str], data: Dict[str, Any]) -> NGOProfile:

    ngo_profile.refresh_from_db()
    ngo_profile, has_updated = model_update(
        instance=ngo_profile, fields=fields, data=data)

    return ngo_profile


@transaction.atomic
def ngo_profile_delete(*, ngo_profile: NGOProfile):

    ngo_profile = ngo_profile.delete()

    return ngo_profile
