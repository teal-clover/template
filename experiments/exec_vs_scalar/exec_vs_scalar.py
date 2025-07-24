import asyncio
from datetime import datetime
from pydantic import EmailStr
from sqlmodel import Relationship, SQLModel, Field, select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "postgresql+asyncpg://pguser:password@localhost:5432/tododb"

engine = create_async_engine(DATABASE_URL, echo=False)


class UserTask(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    task_id: int = Field(foreign_key="task.id", primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: EmailStr = Field(max_length=100, index=True, unique=True)
    tasks: list["Task"] = Relationship(
        back_populates="users",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    users: list["User"] = Relationship(
        back_populates="tasks",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )


async def reset_database():
    SQLModel.metadata.drop_all(engine.sync_engine)
    SQLModel.metadata.create_all(engine.sync_engine)


async def test_select_model():
    print("--- select(User) ---")
    async with AsyncSession(engine) as session:
        stmt = select(User)

        users_exec = (await session.exec(stmt)).all()
        print("exec():", users_exec)

        users_scalars = (await session.scalars(stmt)).all()
        print("scalars():", users_scalars)

        users_execute = (await session.execute(stmt)).all()
        print("execute():", users_execute)


async def test_select_columns():
    print("--- select(User.id, User.email) ---")
    async with AsyncSession(engine) as session:
        stmt = select(User.id, User.email)

        rows_exec = (await session.exec(stmt)).all()
        print("exec():", rows_exec)

        rows_scalars = (await session.scalars(stmt)).all()
        print("scalars():", rows_scalars)

        rows_execute = (await session.execute(stmt)).all()
        print("execute():", rows_execute)


async def main():
    await test_select_model()
    await test_select_columns()


if __name__ == "__main__":
    asyncio.run(main())
