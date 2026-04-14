from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserReadSerializer(serializers.ModelSerializer):
    """
    Read serializer: returns the stored (hashed) password as required by the assignment.
    """

    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "age"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "age"]

    def create(self, validated_data):
        raw_password = validated_data.pop("password")
        user = User(**validated_data)
        user.password = make_password(raw_password)
        user.save()
        return user


class UserUpdateSerializer(serializers.Serializer):
    """
    Update payload:
    - `password` is the CURRENT password used for validation (it will NOT be stored as-is)
    - name/email/age are the fields to update
    """

    name = serializers.CharField(max_length=255, required=False)
    email = serializers.EmailField(required=False)
    age = serializers.IntegerField(required=False, min_value=0)
    password = serializers.CharField(required=True)

