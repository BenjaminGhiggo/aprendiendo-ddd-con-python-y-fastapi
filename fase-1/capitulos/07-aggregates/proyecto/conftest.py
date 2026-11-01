import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import StaticPool

from orm import metadata, iniciar_mapeos


@pytest.fixture
def fabrica_sesion():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    metadata.create_all(engine)
    iniciar_mapeos()
    yield sessionmaker(bind=engine)
    clear_mappers()


@pytest.fixture
def sesion(fabrica_sesion):
    return fabrica_sesion()
