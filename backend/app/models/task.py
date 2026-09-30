from datetime import datetime

from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None, nullable=False, max_length=100)
    status: bool = Field(default=False, nullable=False)
    created_at: str = Field(default=datetime.now())  # noqa: DTZ005
