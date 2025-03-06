from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CheckAdminStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Check if the logged-in user is a superuser
        return Response({'is_superuser': request.user.is_superuser})
