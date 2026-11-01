import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import StaticPool

from orm import metadata, iniciar_mapeos


@pytest.fixture
def sesion():
    # StaticPool + check_same_thread=False: una sola conexión en memoria compartida
    # entre hilos (FastAPI corre el endpoint en otro hilo).
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    metadata.create_all(engine)
    iniciar_mapeos()
    yield sessionmaker(bind=engine)()
    clear_mappers()
