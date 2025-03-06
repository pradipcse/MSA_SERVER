from rest_framework import viewsets
from msa_api.models.banner import Banner
from msa_api.serializers import BannerSerializer

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
