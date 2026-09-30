from sqlmodel import Field, SQLModel


class TaskCreate(SQLModel):
    name: str = Field(max_length=100, min_length=1)


class TaskUpdate(SQLModel):
    name: str = Field(max_length=100, min_length=1)
    status: bool | None = None
