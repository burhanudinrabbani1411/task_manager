from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from backend.app.database import get_session
from backend.app.schema.task import TaskCreate, TaskUpdate
from backend.app.service import task as task_sevice

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

SessionDeep = Annotated[Session, Depends(get_session)]


@router.get(path="")
async def get_tasks(session: SessionDeep):
    return task_sevice.get_tasks(session)


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
