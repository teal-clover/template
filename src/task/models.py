from datetime import datetime
from sqlmodel import Relationship, SQLModel, Field

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.user.models import User, UserPublic


# class Status(Enum):
#     DONE = "done"
#     TODO = "todo"


class UserTask(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    task_id: int = Field(foreign_key="task.id", primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)


class TaskBase(SQLModel):
    title: str = Field(max_length=100, index=True)
    description: str = Field(default=None)


class TaskPublic(TaskBase):
    id: int
    users: list["UserPublic"]


class TaskCreate(TaskBase):
    pass


class Task(TaskBase, table=True):
    id: int = Field(default=None, primary_key=True)
    users: list["User"] = Relationship(
        back_populates="tasks",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )
