from sqlmodel import SQLModel
from src.core.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine


engine = create_async_engine(settings.DATABASE_URL, echo=True)

class Base(SQLModel):
    pass