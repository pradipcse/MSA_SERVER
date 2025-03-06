from rest_framework import viewsets

from msa_api.models.overview import Overview
from msa_api.serializers import OverviewSerializer


class OverviewViewSet(viewsets.ModelViewSet):
    queryset = Overview.objects.all()
    serializer_class = OverviewSerializer