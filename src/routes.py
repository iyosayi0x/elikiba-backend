from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import Article, engine


posts_router = APIRouter(prefix="/posts")


@posts_router.get("/")
def list_posts():
    with Session(engine) as session:
        statement = select(Article)
        rows = session.execute(statement).all()
        print(rows)
    return {
        "posts": "works"
    }
