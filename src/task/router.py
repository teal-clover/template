from fastapi import APIRouter
from src.task.dependencies import TaskControllerDep
from src.core.models import Task, TaskCreate, TaskPublic


router = APIRouter(tags=["tasks"], prefix="/tasks")

@router.post("/create", response_model=TaskPublic)
async def create_task(task: TaskCreate, controller: TaskControllerDep) -> TaskPublic:
    db_task = Task.model_validate(task)
    return await controller.create(db_task)

@router.put("/update/{task_id}")
async def update_task(task_id: int, task: Task, controller: TaskControllerDep) -> Task:
    return await controller.update(task_id, task)

@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, controller: TaskControllerDep) -> None:
    await controller.delete(task_id)

@router.get("/{task_id}")
async def retrieve_task(task_id: int, controller: TaskControllerDep) -> Task:
    return await controller.get(task_id)
