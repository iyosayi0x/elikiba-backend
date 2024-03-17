import os


class Config:
    DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///elikiba.sqlite3")
    SECRET_KEY = os.environ.get("SECRET_KEY", 'development')
