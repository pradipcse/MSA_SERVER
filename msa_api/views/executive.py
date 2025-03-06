from rest_framework import viewsets
from msa_api.models.executive import ExecutiveCommittee
from msa_api.serializers import ExecutiveCommitteeSerializer

class ExecutiveCommitteeViewSet(viewsets.ModelViewSet):
    queryset = ExecutiveCommittee.objects.all()
    serializer_class = ExecutiveCommitteeSerializer
