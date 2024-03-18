from fastapi import FastAPI
from src.routes import posts_router
from fastapi_amis_admin.admin.site import AdminSite
from fastapi_amis_admin.admin.settings import Settings

from src.config import Config

app = FastAPI()

# admin site
site = AdminSite(settings=Settings(database_url_async=Config.DATABASE_URI))
site.mount_app(app)


@app.get("/")
def ping():
    return "PONG"


app.include_router(posts_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
