from .models import Catalogue, Carousel
from rest_framework.serializers import ModelSerializer


class CatalogueSerializer(ModelSerializer):
    class Meta:
        model = Catalogue
        fields = "__all__"


class CarouselSerializer(ModelSerializer):
    class Meta:
        model = Carousel
        fields = "__all__"
