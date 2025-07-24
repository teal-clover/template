from src.core.dependencies import DBSessionDep
from src.core.repository import BaseRepository
from src.task.models import Task
# from src.core.models import (
#     User,  # noqa: F401
# )  # doesnt work without it, seems to be related to how sqlalchemy works  https://stackoverflow.com/a/59241485
# # it's true only when model is not imported, but bc i use core now it's not necessary


class TaskRepository(BaseRepository[Task]):
    def __init__(self, session: DBSessionDep):
        super().__init__(Task, session)
