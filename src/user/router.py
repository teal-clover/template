from fastapi import APIRouter
from src.user.dependencies import UserControllerDep
from src.core.models import User, UserCreate, UserPublic


router = APIRouter(tags=["users"], prefix="/users")


@router.post("/create", response_model=UserPublic)
async def create_user(user: UserPublic, controller: UserControllerDep) -> User:
    db_user = User.model_validate(user)
    return await controller.create(db_user)


@router.put("/update/{user_id}")
async def update_user(user_id: int, user: User, controller: UserControllerDep) -> User:
    return await controller.update(user_id, user)


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, controller: UserControllerDep) -> None:
    await controller.delete(user_id)


@router.get("/{user_id}")
async def retrieve_user(user_id: int, controller: UserControllerDep) -> User:
    return await controller.get(user_id)


@router.get("")
async def retrieve_users(controller: UserControllerDep) -> list[User]:
    return await controller.get_all()
