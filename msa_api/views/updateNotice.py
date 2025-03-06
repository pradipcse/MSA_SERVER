# views.py
from rest_framework import viewsets

from msa_api.models.updateAndnotice import UpdateAndNotice
from msa_api.serializers import UpdateAndNoticeSerializer

class UpdateAndNoticeViewSet(viewsets.ModelViewSet):
    queryset = UpdateAndNotice.objects.all()
    serializer_class = UpdateAndNoticeSerializer
