from fastapi import FastAPI

from api.v1 import tasks_router
from core.database import Base, engine
from models import Task  # noqa: F401

app = FastAPI()
app.include_router(tasks_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def health():
    return {"message": "I'am alive"}
