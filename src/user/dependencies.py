from typing import Annotated
from fastapi import Depends
from src.core.dependencies import DBSessionDep
from src.user.controller import UserController
from src.user.repository import UserRepository


async def get_user_controller(session: DBSessionDep) -> UserController:
    user_repository = UserRepository(session)
    return UserController(user_repository)


UserControllerDep = Annotated[UserController, Depends(get_user_controller)]
