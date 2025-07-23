from datetime import datetime
from sqlmodel import Relationship, Field

from typing import TYPE_CHECKING

from src.core.database import Base
from src.core.intermediary_models import UserTask

if TYPE_CHECKING:
    from src.user.models import User, UserPublic


# class Status(Enum):
#     DONE = "done"
#     TODO = "todo"


class TaskBase(Base):
    title: str = Field(max_length=100, index=True)
    description: str = Field(default=None)


class TaskPublic(TaskBase):
    id: int


class TaskPublicWithUsers(TaskPublic):
    users: list["UserPublic"]


class TaskCreate(TaskBase):
    pass


class TaskCreateWithUsers(TaskCreate):
    users: list["UserPublic"]


class Task(TaskBase, table=True):
    id: int = Field(default=None, primary_key=True)
    users: list["User"] = Relationship(
        back_populates="tasks",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )
