from fastapi import APIRouter

from backend.app.schema.task import TaskCreate, TaskUpdate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.get(path="")
async def get_tasks():
    pass


@router.post(path="")
async def create_tasks(body: TaskCreate):
    pass


@router.get(path="/{id}")
async def get_task(id: int):
    pass


@router.put(path="/{id}")
async def update_task(id: int, body: TaskUpdate):
    pass


@router.delete(path="/{id}")
async def delete_task(id: int):
    pass
