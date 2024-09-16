from typing import List, Dict, Any

from django.db import transaction

from apps.common.services import model_update
from apps.account.models import ProviderProfile



def provider_profile_create(*, user) -> ProviderProfile:
    provider_profile = ProviderProfile(user=user)
    provider_profile.full_clean()
    provider_profile.save()
    

    return provider_profile


@transaction.atomic
def provider_profile_update(*, provider_profile: ProviderProfile, fields: List[str], data: Dict[str, Any]) -> ProviderProfile:

    provider_profile.refresh_from_db()
    provider_profile, has_updated = model_update(
        instance=provider_profile, fields=fields, data=data)

    return provider_profile


@transaction.atomic
def provider_profile_delete(*, provider_profile: ProviderProfile):

    provider_profile = provider_profile.delete()

    return provider_profile
