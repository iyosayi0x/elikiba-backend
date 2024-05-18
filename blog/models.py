from django.db import models
from elikiba.models import BaseModel
from django.utils.text import slugify
# Create your models here.


class Tag(BaseModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Article(BaseModel):
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    display_image = models.ImageField(upload_to="articles/")
    exert = models.CharField(max_length=200)
    content = models.TextField()
    read_minutes = models.PositiveIntegerField()
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate unique slug based on title
        self.slug = slugify(self.title)

        # Handle potential slug conflicts
        i = 1
        while Article.objects.filter(slug=self.slug).exists():
            self.slug = f"{slugify(self.title)}-{i}"
            i += 1

        super().save(*args, **kwargs)  # Save the instance after generating slug
