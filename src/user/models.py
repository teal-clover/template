from pydantic import EmailStr
from sqlmodel import Relationship, Field
from typing import TYPE_CHECKING
from src.core.database import Base
from src.task.models import TaskPublic, UserTask

if TYPE_CHECKING:
    from src.task.models import Task


# class Status(Enum):
#     DONE = "done"
#     TODO = "todo"


class UserBase(Base):
    email: EmailStr = Field(max_length=100, index=True, unique=True) # 


class UserCreate(UserBase):
    pass


class UserPublic(UserBase):
    id: int

class UserPublicWithUser(UserBase):
    tasks: list[TaskPublic]


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    tasks: list["Task"] = Relationship(
        back_populates="users",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )

# class UserSchema(User, table=False):
#     pass
