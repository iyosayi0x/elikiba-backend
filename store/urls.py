from django.urls import path
from .views import CatalogueListView, CarouselListView

urlpatterns = [
    path("catalogue/", CatalogueListView.as_view(), name="catalogue_list"),
    path("carousel/", CarouselListView.as_view(), name="carousel_list"),
]
