from apps.account.models import InvestorProfile
from apps.account.api.serializers import InvestorProfileSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.account.services.investor_profile import investor_profile_create, investor_profile_delete, investor_profile_update


class InvestorProfileViewSet(viewsets.ViewSet):
    queryset = InvestorProfile.objects.all()
    serializer_class = InvestorProfileSerializer

    def get_queryset(self):
        return InvestorProfile.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        investor_profile = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(investor_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        investor_profile = investor_profile_create(**serializer.validated_data)

        serializer = self.serializer_class(investor_profile)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        investor_profile = get_object_or_404(self.get_queryset(), pk=pk)

        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        investor_profile = investor_profile_update(
            investor_profile=investor_profile,
            fields=list(serializer.validated_data.keys()),
            data=serializer.validated_data
        )

        serialized = self.serializer_class(investor_profile)

        return Response(serialized.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        investor_profile = get_object_or_404(self.get_queryset(), pk=pk)

        investor_profile = investor_profile_delete(
            investor_profile=investor_profile)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):
        investor_profile = get_object_or_404(self.get_queryset(), pk=pk)

        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        investor_profile = investor_profile_update(
            investor_profile=investor_profile,
            fields=list(serializer.validated_data.keys()),
            data=serializer.validated_data
        )

        serialized = self.serializer_class(investor_profile)

        return Response(serialized.data, status=status.HTTP_202_ACCEPTED)
