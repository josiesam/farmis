from rest_framework import serializers
from apps.auths.models import (
    CustomUser
)

from djoser.serializers import UserCreateSerializer

from apps.account.services import (
    generic_profile_create, farmer_profile_create,
    researcher_profile_create, investor_profile_create,
    gov_profile_create, ngo_profile_create, provider_profile_create
)

from apps.account.api.serializers import (
    FarmerProfileSerializer, ResearcherProfileSerializer, GenericProfileSerializer,
    GovProfileSerializer, InvestorProfileSerializer, NGOProfileSerializer, ProviderProfileSerializer
)


class CustomUserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number',
                  'user_type', 'avatar', 'profile'
                  ]
        
    def get_profile(self, obj:CustomUser):
        _profile = {
            'generic': generic_profile_create,
            'farmer': farmer_profile_create,
            'researcher': researcher_profile_create,
            'investor': investor_profile_create,
            'gov': gov_profile_create,
            'ngo': ngo_profile_create,
            'provider': provider_profile_create,
        }
        _profile_serializer = {
            'generic': GenericProfileSerializer,
            'farmer': FarmerProfileSerializer,
            'researcher': ResearcherProfileSerializer,
            'investor': InvestorProfileSerializer,
            'gov': GovProfileSerializer,
            'ngo': NGOProfileSerializer,
            'provider': ProviderProfileSerializer,
        }
        profile = _profile[obj.user_type]
        profile_serializer = _profile_serializer[obj.user_type]

        return profile_serializer(profile).data
        


class CustomUserCreateSerializer(UserCreateSerializer):
    def create(self, validated_data):
        customuser = super().create(validated_data)
        print(f'User: {customuser}')

        profile = {
            'generic': generic_profile_create,
            'farmer': farmer_profile_create,
            'researcher': researcher_profile_create,
            'investor': investor_profile_create,
            'gov': gov_profile_create,
            'ngo': ngo_profile_create,
            'provider': provider_profile_create,
        }

        profile[customuser.user_type](user=customuser)

        return customuser
