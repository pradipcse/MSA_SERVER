from rest_framework import viewsets
from msa_api.models.speech import Speech
from msa_api.serializers import SpeechSerializer


class SpeechViewset(viewsets.ModelViewSet):
    queryset = Speech.objects.all()
    serializer_class = SpeechSerializer

