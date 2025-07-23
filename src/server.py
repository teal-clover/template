from fastapi import FastAPI

from src.task.router import router as task_router

app = FastAPI()


@app.get("/")
def health():
    return {"Hello": "World"}

app.include_router(task_router)
