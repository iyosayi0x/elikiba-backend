from django.db import models
from elikiba.models import BaseModel


class CatalogueChoices(models.TextChoices):
    awards = "awards", "awards"
    trophies = "trophies", "trophies"
    medial = "medals", "medals"


class Carousel(BaseModel):
    image = models.ImageField(upload_to="carousels/")
    link = models.URLField(max_length=100)


class Catalogue(BaseModel):
    link = models.URLField(max_length=100)
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=10, choices=CatalogueChoices.choices)
    image = models.ImageField(upload_to="catalogue/")
