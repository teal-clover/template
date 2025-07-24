from pydantic import EmailStr
from .mutual import UserTask
from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .task import Task


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr = Field(max_length=100, index=True, unique=True)
    tasks: list["Task"] = Relationship(
        back_populates="users",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )
