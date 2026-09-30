from http.client import NO_CONTENT
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from backend.app.database import get_session
from backend.app.models.task import Task
from backend.app.schema.response import SuccessResponse
from backend.app.schema.task import TaskCreate, TaskUpdate
from backend.app.service import task as task_sevice

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

SessionDeep = Annotated[Session, Depends(get_session)]


@router.get(path="", status_code=status.HTTP_200_OK)
async def get_tasks(session: SessionDeep) -> SuccessResponse:
    tasks = task_sevice.get_tasks(session)
    return SuccessResponse(
        success=True,
        message="Success Get Tasks",
        data=tasks,
    )


@router.post(path="", status_code=status.HTTP_201_CREATED)
async def create_tasks(session: SessionDeep, body: TaskCreate) -> SuccessResponse:
    task: Task = task_sevice.create_task(session, body)
    return SuccessResponse(
        success=True,
        message="Success creat new Task",
        data=task,
    )


@router.get(path="/{id}", status_code=status.HTTP_200_OK)
async def get_task(session: SessionDeep, id: int) -> SuccessResponse:
    task: Task | None = task_sevice.get_task(session, id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return SuccessResponse(
        success=True,
        message="Success get Task",
        data=task,
    )


@router.patch(path="/{id}", status_code=status.HTTP_200_OK)
async def update_task(
    session: SessionDeep, id: int, body: TaskUpdate
) -> SuccessResponse:
    task: Task | None = task_sevice.get_task(session, id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )

    updated_task: Task = task_sevice.update_task(session, task, body)
    return SuccessResponse(
        success=True,
        message="Success Update Task",
        data=updated_task,
    )


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(session: SessionDeep, id: int) -> None:
    task: Task | None = task_sevice.get_task(session, id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    task_sevice.delete_task(session, task)
