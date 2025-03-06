from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from ..models import CustomUser
from ..serializers import CustomUserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all users and creating a new user.
    Only authenticated users can view the list of users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific user.
    Only authenticated users can access this endpoint.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
