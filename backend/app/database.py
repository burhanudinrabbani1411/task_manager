import os

from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine

load_dotenv()

DATABASE_URL: str | None = os.getenv("DATABASE_URL")

assert DATABASE_URL
engine = create_engine(DATABASE_URL)


def create_db_and_table():
    SQLModel.metadata.create_all(engine)
