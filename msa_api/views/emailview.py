# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from msa_api.models.accounts import CustomUser

class VerifyEmailView(APIView):
    def get(self, request, token):
        user = get_object_or_404(CustomUser, verification_token=token)
        
        if user.is_verified:
            return Response({"message": "Your email is already verified."}, status=status.HTTP_200_OK)
        
        # Mark the user as verified
        user.is_verified = True
        user.verification_token = None  # Token should not be reusable
        user.save()

        return Response({"message": "Email verified successfully!"}, status=status.HTTP_200_OK)
