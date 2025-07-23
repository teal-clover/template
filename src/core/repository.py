# core/repository.py

from typing import TypeVar, Generic, Type, Optional, List
from sqlmodel import select
from src.core.database import Base
from src.core.dependencies import DBSessionDep
from src.task.models import TaskPublic

T = TypeVar("T", bound=TaskPublic)

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], session: DBSessionDep):
        self.model = model
        self.session = session

    async def get(self, item_id: int) -> Optional[T]:
        result = await self.session.exec(
            select(self.model).where(getattr(self.model, "id") == item_id)
        )
        return result.one()
        

    async def get_all(self) -> List[T]:
        result = (await self.session.exec(select(self.model))).all() # returns a sequence
        return list(result)

    async def create(self, item: T) -> T:
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def update(self, item: T, data: dict) -> T:
        for field, value in data.items():
            setattr(item, field, value)
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def delete(self, item: T) -> None:
        await self.session.delete(item)
        await self.session.commit()
