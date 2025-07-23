from datetime import datetime

from sqlmodel import Field

from src.core.database import Base


class UserTask(Base, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    task_id: int = Field(foreign_key="task.id", primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
