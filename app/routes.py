from fastapi import APIRouter

posts_router = APIRouter()

posts_router.get("/posts")


def list_posts():
    return {
        "posts": "works"
    }
