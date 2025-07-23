from typing import Annotated
from fastapi import Depends
from src.core.dependencies import DBSessionDep
from src.task.controller import TaskController
from src.task.repository import TaskRepository


async def get_task_controller(session: DBSessionDep) -> TaskController:
    task_repository = TaskRepository(session)
    return TaskController(task_repository)


TaskControllerDep = Annotated[TaskController, Depends(get_task_controller)]
