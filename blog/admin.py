from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article, Tag, Author
# Register your models here.


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title', 'author', "created_at")
    exclude = ("slug",)


class TagAdmin(ModelAdmin):
    list_display = ('id', 'name', "created_at")


class AuthorAdmin(ModelAdmin):
    list_display = ('id', 'name', "created_at")


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
