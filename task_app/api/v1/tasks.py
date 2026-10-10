from fastapi import APIRouter, Depends, status

from schemas.tasks import TaskIn, TaskOut, TaskUpdate
from services.tasks import TaskService

router = APIRouter(tags=["tasks"])


@router.post("/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskIn, service: TaskService = Depends()):
    return service.create_task(task)


@router.get("/tasks", response_model=list[TaskOut])
def get_tasks(service: TaskService = Depends()):
    return service.get_tasks()


@router.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int, service: TaskService = Depends()):
    return service.get_task(task_id)


@router.patch("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, data: TaskUpdate, service: TaskService = Depends()):
    return service.update_task(task_id, data)


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, service: TaskService = Depends()):
    service.delete_task(task_id)
