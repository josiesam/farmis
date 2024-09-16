from typing import List, Dict, Any

from django.db import transaction

from apps.common.services import model_update
from apps.account.models import FarmerProfile



def farmer_profile_create(*, user) -> FarmerProfile:
    farmer_profile = FarmerProfile(user=user)
    farmer_profile.full_clean()
    farmer_profile.save()
    

    return farmer_profile


@transaction.atomic
def farmer_profile_update(*, farmer_profile: FarmerProfile, fields: List[str], data: Dict[str, Any]) -> FarmerProfile:

    farmer_profile.refresh_from_db()
    farmer_profile, has_updated = model_update(
        instance=farmer_profile, fields=fields, data=data)

    return farmer_profile


@transaction.atomic
def farmer_profile_delete(*, farmer_profile: FarmerProfile):

    farmer_profile = farmer_profile.delete()

    return farmer_profile
