from fastapi_amis_admin.admin.site import AdminSite
from fastapi_amis_admin.admin import ModelAdmin
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin import i18n

from src.config import Config
from .models import Article
from main import app


# admin site
i18n.set_language(language='en_US')
site = AdminSite(
    settings=Settings(
        database_url=Config.DATABASE_URI,
        debug=Config.DEBUG,
        site_title="Elikiba Admin",
    )
)


@site.register_admin
class ArticleAdmin(ModelAdmin):
    page_schema = 'Articles'
    model = Article
    page_path = "/articles"
    bind_model = True
    update_fields = [
        Article.title,
        Article.is_headline,
        Article.type,
        Article.author,
        Article.content,
        Article.excerpt,
        Article.read_minutes,
        Article.tags,
    ]
    list_display = [
        Article.id,
        Article.title,
        Article.slug,
        Article.created_at,
    ]
    ordering = "created_at"
    list_per_page = 20


site.mount_app(app)
