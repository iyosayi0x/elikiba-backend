from django.db import models
from elikiba.models import BaseModel

# Create your models here.


class Tag(BaseModel):
    name = models.CharField(max_length=20, unique=True)


class Author(BaseModel):
    name = models.CharField(max_length=40)


class Article(BaseModel):
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL)
    content = models.TextField()
    exert = models.CharField(max_length=200)
    read_minutes = models.PositiveIntegerField()
    tags = models.ManyToManyField(Tag, related_name="tags")
