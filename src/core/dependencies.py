from typing import Annotated

from fastapi import Depends
from src.core.database import engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker


async def get_session():
    async_session = async_sessionmaker(
        engine, class_=AsyncSession
    )  # future=True, echo=True
    async with async_session() as session:
        yield session


DBSessionDep = Annotated[
    AsyncSession, Depends(get_session)
]  # session: AsyncSession = Depend(get_session)
