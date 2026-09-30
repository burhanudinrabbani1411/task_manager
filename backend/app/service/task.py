from typing import Any

from sqlmodel import Session, select

from backend.app.models.task import Task
from backend.app.schema.task import TaskCreate, TaskUpdate


def get_tasks_service(session: Session):
    statment = select(Task)
    return session.exec(statment).all()


def create_task_service(session: Session, body: TaskCreate):
    task = Task.model_validate(body)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def get_task_service(session: Session, id: int):
    return session.get(Task, id)


def update_task_service(session: Session, task: Task, body: TaskUpdate):
    new_body: dict[str, Any] = body.model_dump(exclude_unset=True)

    for key, value in new_body.items():
        setattr(task, key, value)

    session.add(task)
    session.commit()
    session.refresh(task)

    return task


def delete_task_service(session: Session, task: Task):
    session.delete(task)
    session.commit()
