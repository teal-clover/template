# from datetime import datetime
# from sqlmodel import Relationship, SQLModel, Field


# class UserTask(SQLModel, table=True):
#     user_id: int = Field(foreign_key="user.id", primary_key=True)
#     task_id: int = Field(foreign_key="task.id", primary_key=True)
#     created_at: datetime = Field(default_factory=datetime.now)


# class UserBase(SQLModel):
#     email: str = Field(max_length=100, index=True, unique=True)


# class UserPublic(SQLModel):
#     pass

# class User(UserBase, table=True):
#     id: int = Field(default=None, primary_key=True)
#     tasks: list["Task"] = Relationship(back_populates="users", link_model=UserTask)

# class TaskBase(SQLModel):
#     title: str = Field(max_length=100, index=True)
#     description: str = Field(default=None)


# class TaskPublic(TaskBase):
#     id: int
#     users: list["UserPublic"]


# class TaskCreate(TaskBase):
#     pass


# class Task(TaskBase, table=True):
#     id: int = Field(default=None, primary_key=True)
#     users: list["User"] = Relationship(back_populates="tasks", link_model=UserTask)


from src.user.models import UserBase, UserPublic, User
from src.task.models import UserTask, TaskBase, TaskPublic, TaskCreate, Task

TaskPublic.model_rebuild()