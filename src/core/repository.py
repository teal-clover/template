from sqlmodel import SQLModel, select
from src.core.dependencies import DBSessionDep


class BaseRepository:
    class Meta:
        model = SQLModel
        lookup_field = "id"

    def __init__(self, session: DBSessionDep):
        self.session = session
        self.model = self.Meta.model

    async def get(self, item_id: int) -> SQLModel | None:
        return (
            await self.session.scalars(
                select(self.model).where(self.model.id == item_id)
            )
        ).first()

    async def get_all(self) -> list[SQLModel]:
        return await self.session.scalars(select(self.model))

    async def create(self, item: SQLModel) -> SQLModel:
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def update(self, item: SQLModel, data: dict) -> SQLModel:
        for field, value in data.items():
            setattr(item, field, value)
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def delete(self, item: SQLModel) -> None:
        await self.session.delete(item)
        await self.session.commit()
