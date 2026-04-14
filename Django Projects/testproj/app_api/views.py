
# Create your views here.

from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer

User = get_user_model()


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
