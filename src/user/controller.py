from src.core.controller import BaseController
from src.user.models import User
from src.user.repository import UserRepository


class UserController(BaseController[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)
