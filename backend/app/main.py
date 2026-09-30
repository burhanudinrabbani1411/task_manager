from fastapi import FastAPI

from backend.app.database import create_db_and_table

from .routes import task

app = FastAPI()


@app.on_event("startup")  # type: ignore
def on_startup():
    create_db_and_table()


app.include_router(task.router)
