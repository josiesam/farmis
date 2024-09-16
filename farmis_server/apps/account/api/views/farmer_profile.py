from apps.account.models import FarmerProfile
from apps.account.api.serializers import FarmerProfileSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.account.services.farmer_profile import farmer_profile_create, farmer_profile_delete, farmer_profile_update


class FarmerProfileViewSet(viewsets.ViewSet):
    queryset = FarmerProfile.objects.all()
    serializer_class = FarmerProfileSerializer

    def get_queryset(self):
        return FarmerProfile.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        farmer_profile = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(farmer_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        farmer_profile = farmer_profile_create(**serializer.validated_data)

        serializer = self.serializer_class(farmer_profile)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        farmer_profile = get_object_or_404(self.get_queryset(), pk=pk)

        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        farmer_profile = farmer_profile_update(
            farmer_profile=farmer_profile,
            fields=list(serializer.validated_data.keys()),
            data=serializer.validated_data
        )

        serialized = self.serializer_class(farmer_profile)

        return Response(serialized.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        farmer_profile = get_object_or_404(self.get_queryset(), pk=pk)

        farmer_profile = farmer_profile_delete(
            farmer_profile=farmer_profile)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):
        farmer_profile = get_object_or_404(self.get_queryset(), pk=pk)

        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        farmer_profile = farmer_profile_update(
            farmer_profile=farmer_profile,
            fields=list(serializer.validated_data.keys()),
            data=serializer.validated_data
        )

        serialized = self.serializer_class(farmer_profile)

        return Response(serialized.data, status=status.HTTP_202_ACCEPTED)
