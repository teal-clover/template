from fastapi import HTTPException
from sqlmodel import SQLModel

from src.core.repository import BaseRepository


class BaseController:
    def __init__(self, repository: BaseRepository):
        self.repo = repository

    async def get(self, item_id: int) -> SQLModel:
        item = await self.repo.get(item_id)
        if item is None:
            raise HTTPException(status_code=404)
        return item
    
    async def get_all(self) -> list[SQLModel]:
        item = await self.repo.get_all()
        return item

    async def create(self, item: SQLModel) -> SQLModel:
        return await self.repo.create(item)

    async def update(self, item_id: int, data: SQLModel) -> SQLModel:
        item = await self.get(item_id)
        return await self.repo.update(item, data.model_dump())

    async def delete(self, item_id: int) -> None:
        item = await self.get(item_id)
        await self.repo.delete(item)
