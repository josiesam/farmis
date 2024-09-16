from typing import List, Dict, Any

from django.db import transaction

from apps.common.services import model_update
from apps.auths.models import CustomUser

from apps.account.services import (
    generic_profile_create, farmer_profile_create,
    researcher_profile_create, investor_profile_create,
    gov_profile_create, ngo_profile_create, provider_profile_create
)


def customuser_create(*, phone_number, password, user_type) -> CustomUser:
    customuser = CustomUser(phone_number=phone_number, password=password, user_type=user_type)
    customuser.full_clean()
    customuser = customuser.save()

    profile = {
        'generic': generic_profile_create,
        'farmer': farmer_profile_create,
        'researcher': researcher_profile_create,
        'investor': investor_profile_create,
        'gov': gov_profile_create,
        'ngo': ngo_profile_create,
        'provider': provider_profile_create,
    }
    print(customuser)

    profile[user_type](user=customuser)
    

    return customuser


@transaction.atomic
def customuser_update(*, customuser: CustomUser, fields: List[str], data: Dict[str, Any]) -> CustomUser:

    customuser.refresh_from_db()
    customuser, has_updated = model_update(
        instance=customuser, fields=fields, data=data)

    return customuser


@transaction.atomic
def customuser_delete(*, customuser: CustomUser):

    customuser = customuser.delete()

    return customuser
