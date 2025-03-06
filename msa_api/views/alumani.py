from rest_framework import viewsets

from msa_api.models.alumany import Alumanai
from msa_api.serializers import AlumanaiSerializer

class AlumanaiViewSet(viewsets.ModelViewSet):
    queryset = Alumanai.objects.all()
    serializer_class = AlumanaiSerializer
