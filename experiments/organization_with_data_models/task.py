from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

from .mutual import UserTask

if TYPE_CHECKING:
    from .user import UserPublic, User


class TaskPublic(SQLModel):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=100, index=True)
    description: str = Field(default=None)


class TaskPublicWithUsers(TaskPublic):
    users: list["UserPublic"]


class Task(TaskPublic, table=True):
    users: list["User"] = Relationship(
        back_populates="tasks",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )

from .user import UserPublic
TaskPublicWithUsers.model_rebuild()  # ts requires UserPublic

