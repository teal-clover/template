from .mutual import UserTask
from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=100, index=True)
    description: str = Field(default=None)
    users: list["User"] = Relationship(
        back_populates="tasks",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )
