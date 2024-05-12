from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Article, Tag, Author
# Register your models here.


class ArticleAdmin(ModelAdmin):
    list_display = ('id', 'title', 'author', "created_at")


class TagAdmin(ModelAdmin):
    list_display = ('id', 'name', "created_at")


class AuthorAdmin(ModelAdmin):
    list_display = ('id', 'name', "created_at")


class SocialChannelAdmin(ModelAdmin):
    list_display = ("id", 'name', 'created_at')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
