from sqlmodel import Relationship, SQLModel, Field
from typing import TYPE_CHECKING
from src.task.models import UserTask

if TYPE_CHECKING:
    from src.task.models import Task


# class Status(Enum):
#     DONE = "done"
#     TODO = "todo"


class UserBase(SQLModel):
    email: str = Field(max_length=100, index=True, unique=True)


class UserPublic(SQLModel):
    pass


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    tasks: list["Task"] = Relationship(
        back_populates="users",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )
