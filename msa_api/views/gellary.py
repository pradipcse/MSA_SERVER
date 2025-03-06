# views.py

# views.py
from rest_framework import viewsets

from msa_api.models.gellary import Gallery
from msa_api.serializers import GallerySerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

