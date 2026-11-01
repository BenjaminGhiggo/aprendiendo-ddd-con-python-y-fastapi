import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from orm import metadata, iniciar_mapeos


@pytest.fixture
def sesion():
    engine = create_engine("sqlite://")      # base de datos en memoria
    metadata.create_all(engine)              # crea las tablas
    iniciar_mapeos()                         # mapea el modelo a las tablas
    yield sessionmaker(bind=engine)()
    clear_mappers()                          # limpia el mapeo tras cada test
