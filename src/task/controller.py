from src.core.controller import BaseController
from src.task.models import Task
from src.task.repository import TaskRepository


class TaskController(BaseController[Task]):
    def __init__(self, repository: TaskRepository):
        super().__init__(repository)
