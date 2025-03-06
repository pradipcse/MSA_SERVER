from rest_framework import viewsets

from msa_api.models.history import History
from msa_api.serializers import HistorySerializer
class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer