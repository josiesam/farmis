from typing import List, Dict, Any

from django.db import transaction

from apps.common.services import model_update
from apps.account.models import GenericProfile



def generic_profile_create(*, user) -> GenericProfile:
    generic_profile = GenericProfile(user=user)
    generic_profile.full_clean()
    generic_profile.save()
    

    return generic_profile


@transaction.atomic
def generic_profile_update(*, generic_profile: GenericProfile, fields: List[str], data: Dict[str, Any]) -> GenericProfile:

    generic_profile.refresh_from_db()
    generic_profile, has_updated = model_update(
        instance=generic_profile, fields=fields, data=data)

    return generic_profile


@transaction.atomic
def generic_profile_delete(*, generic_profile: GenericProfile):

    generic_profile = generic_profile.delete()

    return generic_profile
