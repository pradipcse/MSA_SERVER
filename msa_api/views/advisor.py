from rest_framework import viewsets

from msa_api.models.advisor import Advisor
from msa_api.serializers import AdvisorSerializer


class AdvisorViewSet(viewsets.ModelViewSet):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
