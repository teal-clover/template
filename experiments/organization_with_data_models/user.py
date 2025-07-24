from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr

from .mutual import UserTask

# if TYPE_CHECKING:
#     from .task import TaskPublic, Task
import organization_with_data_models.task as task


class UserPublic(SQLModel):
    id: int = Field(default=None, primary_key=True)
    email: EmailStr = Field(max_length=100, index=True, unique=True)


class UserPublicWithTasks(UserPublic):
    tasks: list[task.TaskPublic] = []


class User(UserPublic, table=True):
    tasks: list[task.Task] = Relationship(
        back_populates="users",
        link_model=UserTask,
        sa_relationship_kwargs={"lazy": "selectin"},
    )


from .task import TaskPublic

UserPublicWithTasks.model_rebuild()  # ts requires TaskPublic
