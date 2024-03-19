from fastapi_amis_admin.admin.site import AdminSite
from fastapi_amis_admin.admin import ModelAdmin
from fastapi_amis_admin.admin.settings import Settings

from src.config import Config
from .models import Article
from main import app

# admin site
site = AdminSite(
    settings=Settings(
        database_url=Config.DATABASE_URI,
        language="en_US",
        debug=Config.DEBUG,
        site_title="Elikiba Admin",
    )
)


@site.register_admin
class ArticleAdmin(ModelAdmin):
    page_schema = 'Articles'
    model = Article
    list_display = [Article.id, Article.title, Article.slug]
    ordering = Article.created_at

    async def get_select(self, request):
        statement = await super().get_select(request)
        return statement


site.mount_app(app)
