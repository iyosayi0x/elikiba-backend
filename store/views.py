from .models import Catalogue, Carousel
from .serializers import CatalogueSerializer, CarouselSerializer
from rest_framework.generics import ListAPIView


class CatalogueListView(ListAPIView):
    pagination_class = None
    serializer_class = CatalogueSerializer

    def get_queryset(self):
        type = self.request.query_params.get("type", "awards")
        return Catalogue.objects.filter(type=type)


class CarouselListView(ListAPIView):
    pagination_class = None
    serializer_class = CarouselSerializer

    def get_queryset(self):
        return Carousel.objects.all()
