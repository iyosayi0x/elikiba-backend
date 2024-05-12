from django.db import models
from elikiba.models import BaseModel
from ckeditor.fields import RichTextField

# Create your models here.


class Tag(BaseModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Article(BaseModel):
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL)
    content = RichTextField()
    display_image = models.ImageField(upload_to="/articles")
    exert = models.CharField(max_length=200)
    read_minutes = models.PositiveIntegerField()
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return self.title


class SocialChannel(BaseModel):
    name = models.CharField(max_length=20, unique=True)
    link = models.URLField(max_length=100)
    icon = models.ImageField(upload_to="/socials")
