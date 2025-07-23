from fastapi import FastAPI

from src.task.router import router as task_router
from src.user.router import router as user_router

app = FastAPI()


@app.get("/")
def health():
    return {"Hello": "World"}

app.include_router(task_router)
app.include_router(user_router)
