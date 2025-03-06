# views.py
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import uuid

from msa_api.serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            verification_token = uuid.uuid4()
            user.verification_token = verification_token
            user.save()

            # Create verification URL
            domain = get_current_site(request).domain
            verification_url = f"http://{domain}{reverse('verify_email', kwargs={'token': verification_token})}"

            # Send email with verification URL
            send_mail(
                "Verify your email address",
                f"Please click the following link to verify your email: {verification_url}",
                "no-reply@example.com",
                [user.email],
                fail_silently=False,
            )

            return Response(
                {
                    "message": "User registered successfully! Please check your email to verify your account.",
                    "user": RegisterSerializer(user).data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
