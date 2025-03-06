from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers import LoginSerializer
from rest_framework.permissions import AllowAny

class LoginView(GenericAPIView):
    """Handles user login using GenericAPIView."""
    
    # Specify the serializer class for the view
    serializer_class = LoginSerializer
    
    # Allow any user (authenticated or not) to access the endpoint
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Handle user login via POST request."""
        serializer = self.get_serializer(data=request.data)
        
        # Validate the input
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            
            # Return tokens and user details
            return Response(
                {
                    "message": "Login successful!",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "name": user.name,
                        "is_staff": user.is_staff,
                    },
                },
                status=status.HTTP_200_OK,
            )
        
        # Return validation errors if input is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
