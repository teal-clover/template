# core/controller.py

from typing import Generic, TypeVar, List
from fastapi import HTTPException
from sqlmodel import SQLModel

from src.core.repository import BaseRepository

T = TypeVar("T", bound=SQLModel)

class BaseController(Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self.repo = repository

    async def get(self, item_id: int) -> T:
        try:
            item = await self.repo.get(item_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        if item is None:
            raise HTTPException(status_code=404)
        return item

    async def get_all(self) -> List[T]:
        return await self.repo.get_all()

    async def create(self, item: T) -> T:
        return await self.repo.create(item)

    async def update(self, item_id: int, data: T) -> T:
        item = await self.get(item_id)
        return await self.repo.update(item, data.model_dump())

    async def delete(self, item_id: int) -> None:
        item = await self.get(item_id)
        await self.repo.delete(item)
