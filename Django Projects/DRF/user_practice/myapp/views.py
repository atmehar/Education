from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserCreateSerializer, UserReadSerializer, UserUpdateSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    """
    GET /api/users/  -> list all users (password returned as hashed)
    POST /api/users/ -> create a user (password is hashed before storing)
    """

    queryset = User.objects.all().order_by("id")
    serializer_class = UserReadSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCreateSerializer
        return UserReadSerializer


class UserDetailAPIView(APIView):
    """
    GET /api/users/<id>/     -> retrieve a user (password returned as hashed)
    PUT /api/users/<id>/     -> update user fields (requires current password validation)
    DELETE /api/users/<id>/  -> delete user (requires current password validation)
    """

    def get(self, request, pk: int):
        user = get_object_or_404(User, pk=pk)
        return Response(UserReadSerializer(user).data)

    def put(self, request, pk: int):
        user = get_object_or_404(User, pk=pk)

        payload_serializer = UserUpdateSerializer(data=request.data)
        payload_serializer.is_valid(raise_exception=True)
        current_password = payload_serializer.validated_data.pop("password")

        if not user.check_password(current_password):
            return Response(
                {"detail": "Invalid password."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Update only the allowed fields (password is not updated here).
        for field, value in payload_serializer.validated_data.items():
            setattr(user, field, value)
        user.save()
        return Response(UserReadSerializer(user).data)

    def delete(self, request, pk: int):
        user = get_object_or_404(User, pk=pk)

        payload_serializer = UserUpdateSerializer(data=request.data)
        payload_serializer.is_valid(raise_exception=True)
        current_password = payload_serializer.validated_data.get("password")

        if not user.check_password(current_password):
            return Response(
                {"detail": "Invalid password."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
