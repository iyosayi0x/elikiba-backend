from django.urls import path
from .views import ArticlesView, ArticleLatestView, ArticleRetrieveView

urlpatterns = [
    path("articles", ArticlesView.as_view(), name="articles"),
    path("articles/latest/", ArticleLatestView.as_view(),
         name="articles_latest"),
    path("articles/article/<str:slug>/",
         ArticleRetrieveView.as_view(),
         name="article_retrieve"),
]
