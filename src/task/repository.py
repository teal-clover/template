from src.core.repository import BaseRepository

# from src.core.models import Task
# from src.core.models import User
from src.core.models import Task
from src.core.models import (
    User,  # noqa: F401
)  # doesnt work without it, seems to be related to how sqlalchemy works  https://stackoverflow.com/a/59241485


class TaskRepository(BaseRepository):
    class Meta:
        model = Task
        lookup_field = "id"
