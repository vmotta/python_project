from pathlib import Path

from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlmodel import SQLModel, Session, create_engine

from app.core.config import settings


def _ensure_sqlite_directory() -> None:
    db_file = settings.sqlite_file
    Path(db_file).parent.mkdir(parents=True, exist_ok=True)


_ensure_sqlite_directory()
engine = create_engine(settings.database_url, echo=False, connect_args={"check_same_thread": False})


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Ensure relational integrity with SQLite.
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
