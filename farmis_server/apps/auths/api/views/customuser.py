from apps.auths.models import CustomUser
from apps.auths.api.serializers import (
    CustomUserSerializer, 
)
from rest_framework import viewsets,status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.auths.services.customuser import customuser_delete, customuser_update



class CustomUserViewSet(viewsets.ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        customuser = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(customuser, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        customuser = get_object_or_404(self.get_queryset(), pk=pk)

        serializer = self.serializer_class(data=request.data, context={"request":request})

        serializer.is_valid(raise_exception=True)

        customuser = customuser_update(
            customuser=customuser,
            fields=list(serializer.validated_data.keys()),
            data=serializer.validated_data
        )

        serialized = self.serializer_class(customuser, context={"request":request})

        return Response(serialized.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        customuser = get_object_or_404(self.get_queryset(), pk=pk)

        customuser = customuser_delete(
            customuser=customuser)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):
        customuser = get_object_or_404(self.get_queryset(), pk=pk)

        serializer = self.serializer_class(data=request.data, context={"request":request})

        serializer.is_valid(raise_exception=True)

        customuser = customuser_update(
            customuser=customuser,
            fields=list(serializer.validated_data.keys()),
            data=serializer.validated_data
        )

        serialized = self.serializer_class(customuser, context={"request":request})

        return Response(serialized.data, status=status.HTTP_202_ACCEPTED)

