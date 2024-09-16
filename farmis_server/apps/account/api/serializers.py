from rest_framework import serializers
from apps.account.models import (
    FarmerProfile, GenericProfile, GovProfile, NGOProfile,
    ResearcherProfile, InvestorProfile,ProviderProfile
)

class FarmerProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = FarmerProfile
        fields = '__all__'

class GenericProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = GenericProfile
        fields = '__all__'

class NGOProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = NGOProfile
        fields = '__all__'

class ProviderProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ProviderProfile
        fields = '__all__'

class GovProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = GovProfile
        fields = '__all__'

class ResearcherProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ResearcherProfile
        fields = '__all__'

class InvestorProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = InvestorProfile
        fields = '__all__'