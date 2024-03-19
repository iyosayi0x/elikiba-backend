from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class ArticleSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    is_headline: bool = Field(default=False)
    title: str = Field(nullable=False)
    slug: str = Field(nullable=True)
    type: str = Field(default="article")
    author: str = Field(nullable=False)
    content: str = Field(nullable=False)
    excerpt: str = Field(nullable=False)
    read_minutes: int = Field(nullable=False)
    tags: str = Field(
        nullable=False,
        description="Article tags, separate with comma(,) for multiple tags"
    )
    created_at: datetime = Field(nullable=False)
    last_updated_at: datetime = Field(nullable=False)
