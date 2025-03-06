from rest_framework import viewsets
from msa_api.models.events import Event
from msa_api.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer