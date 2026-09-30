import os
from collections.abc import Generator

from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine

load_dotenv()

DATABASE_URL: str | None = os.getenv("DATABASE_URL")

assert DATABASE_URL
engine = create_engine(DATABASE_URL)


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
