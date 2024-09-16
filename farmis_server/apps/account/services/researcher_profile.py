from typing import List, Dict, Any

from django.db import transaction

from apps.common.services import model_update
from apps.account.models import ResearcherProfile



def researcher_profile_create(*, user) -> ResearcherProfile:
    researcher_profile = ResearcherProfile(user=user)
    researcher_profile.full_clean()
    researcher_profile.save()
    

    return researcher_profile


@transaction.atomic
def researcher_profile_update(*, researcher_profile: ResearcherProfile, fields: List[str], data: Dict[str, Any]) -> ResearcherProfile:

    researcher_profile.refresh_from_db()
    researcher_profile, has_updated = model_update(
        instance=researcher_profile, fields=fields, data=data)

    return researcher_profile


@transaction.atomic
def researcher_profile_delete(*, researcher_profile: ResearcherProfile):

    researcher_profile = researcher_profile.delete()

    return researcher_profile
