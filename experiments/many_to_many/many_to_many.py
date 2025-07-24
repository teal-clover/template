import asyncio
from datetime import datetime
from pydantic import EmailStr
from sqlmodel import Relationship, SQLModel, Field, select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATABASE_URL = "postgresql+asyncpg://pguser:password@localhost:5432/tododb"

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class UserTask(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    task_id: int = Field(foreign_key="task.id", primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr = Field(max_length=100, index=True, unique=True)
    tasks: list["Task"] = Relationship(
        back_populates="users",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=100, index=True)
    description: str = Field(default=None)
    users: list[User] = Relationship(
        back_populates="tasks",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )


async def reset_database():
    SQLModel.metadata.drop_all(engine.sync_engine)
    SQLModel.metadata.create_all(engine.sync_engine)


async def create_sample_data():
    async with async_session() as session:
        user1 = User(email="user1@example.com")
        user2 = User(email="user2@example.com")

        task1 = Task(title="Task1", description="Description1")
        task2 = Task(title="Task2", description="Description2")

        user1.tasks.append(task1)
        user1.tasks.append(task2)
        user2.tasks.append(task2)

        session.add_all([user1, user2, task1, task2])
        await session.commit()


async def show_users_and_tasks():
    async with async_session() as session:
        result = await session.exec(select(User))
        users = result.all()
        print()
        print("--- Users and their tasks ---")
        for user in users:
            print(f"{user.email}:")
            for task in user.tasks:
                print(f"  - {task.title}")


async def show_tasks_and_users():
    async with async_session() as session:
        result = await session.exec(select(Task))
        tasks = result.all()
        print()
        print("--- Tasks and their users ---")
        for task in tasks:
            print(f"{task.title}:")
            for user in task.users:
                print(f"  - {user.email}")


async def main():
    await create_sample_data()
    await show_users_and_tasks()
    await show_tasks_and_users()


if __name__ == "__main__":
    asyncio.run(main())
