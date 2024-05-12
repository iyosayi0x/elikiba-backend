from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Catalogue, Carousel


class CatalogueAdmin(ModelAdmin):
    list_display = ("id", 'title', "created_at")


class CarouselAdmin(ModelAdmin):
    list_display = ("id", "link", "created_at")


admin.site.register(Catalogue, CatalogueAdmin)
admin.site.register(Carousel, CarouselAdmin)
