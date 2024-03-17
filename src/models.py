from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Text, Column, UUID, TIMESTAMP
from sqlalchemy import create_engine
import uuid
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import event
from sqlalchemy.orm import Session

from src.config import Config

engine = create_engine(Config.DATABASE_URI, echo=True)


class Base(DeclarativeBase):
    id = Column(UUID, primary_key=True, default=uuid.uuid4)


class Article(Base):
    __tablename__ = "articles"
    is_headline: Mapped[bool] = mapped_column(default=False)
    title: Mapped[str] = mapped_column(String(30))
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    type: Mapped[str] = mapped_column(String(100))
    author: Mapped[str] = mapped_column(String(60))
    content: Mapped[str] = mapped_column(Text)
    excerpt: Mapped[str] = mapped_column(String(255))
    read_minutes: Mapped[int] = mapped_column()
    tags: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=datetime.utcnow)
    last_updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return f"<Article {self.title}>"  # Optional for better debugging


# events
@event.listens_for(Article, "before_insert")
def generate_slug_before_insert(mapper, connect, instance):
    if not instance.slug:
        base_slug = instance.title.lower().replace(" ", "-")
        slug = base_slug
        count = 1

        # use db session
        with Session(engine) as session:
            while session.query(Article).filter_by(slug=slug).first():
                slug = f"{base_slug}-{count}"
                count += 1
            instance.slug = slug


@event.listens_for(Article, "after_insert")
def update_last_updated(mapper, connect, instance):
    instance.last_updated_at = datetime.utcnow()
