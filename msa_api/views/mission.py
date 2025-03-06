from rest_framework import viewsets

from msa_api.models.mission import Mission
from msa_api.serializers import MissionSerializer

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer