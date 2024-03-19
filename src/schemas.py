from pydantic import BaseModel, Field, ConfigDict
import uuid
from datetime import datetime


class ArticleSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, primary_key=True, nullable=False)
    is_headline: bool = Field(default=False)
    title: str = Field(nullable=False)
    slug: str = Field(nullable=False)
    type: str = Field(default="article")
    author: str = Field(nullable=False)
    content: str = Field(nullable=False)
    excerpt: str = Field(nullable=False)
    read_minutes: int = Field(nullable=False)
    tags: str = Field(nullable=False)
    created_at: datetime = Field(nullable=False, default=datetime.utcnow)
    last_updated_at: datetime = Field(nullable=False, default=datetime.utcnow)
