from datetime import datetime
from sqlmodel import Field, SQLModel


class UserTask(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    task_id: int = Field(foreign_key="task.id", primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
