from fastapi import Depends
from sqlalchemy import create_engine

from config.settings import Settings
from dao.factory_dao import FactoryDao
from dao.sprocket_dao import SprocketDao
from orm import Base


def get_settings():
    return Settings()


def get_sql_engine(settings=Depends(get_settings)):
    engine = create_engine(settings.db_url)
    Base.metadata.create_all(engine)
    return engine


def get_sprocket_dao(sql_engine=Depends(get_sql_engine)) -> SprocketDao:
    return SprocketDao(sql_engine)


def get_factory_dao(sql_engine=Depends(get_sql_engine)) -> FactoryDao:
    return FactoryDao(sql_engine)
