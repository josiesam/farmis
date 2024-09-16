from apps.account.models import ResearcherProfile
from apps.account.api.serializers import ResearcherProfileSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.account.services.researcher_profile import researcher_profile_create, researcher_profile_delete, researcher_profile_update


class ResearcherProfileViewSet(viewsets.ViewSet):
    queryset = ResearcherProfile.objects.all()
    serializer_class = ResearcherProfileSerializer

    def get_queryset(self):
        return ResearcherProfile.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        researcher_profile = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(researcher_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        researcher_profile = researcher_profile_create(**serializer.validated_data)

        serializer = self.serializer_class(researcher_profile)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        researcher_profile = get_object_or_404(self.get_queryset(), pk=pk)

        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        researcher_profile = researcher_profile_update(
            researcher_profile=researcher_profile,
            fields=list(serializer.validated_data.keys()),
            data=serializer.validated_data
        )

        serialized = self.serializer_class(researcher_profile)

        return Response(serialized.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        researcher_profile = get_object_or_404(self.get_queryset(), pk=pk)

        researcher_profile = researcher_profile_delete(
            researcher_profile=researcher_profile)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):
        researcher_profile = get_object_or_404(self.get_queryset(), pk=pk)

        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        researcher_profile = researcher_profile_update(
            researcher_profile=researcher_profile,
            fields=list(serializer.validated_data.keys()),
            data=serializer.validated_data
        )

        serialized = self.serializer_class(researcher_profile)

        return Response(serialized.data, status=status.HTTP_202_ACCEPTED)
