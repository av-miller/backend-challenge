from typing import Dict

from sqlalchemy.orm import sessionmaker

from app.orm.sprocket import Sprocket


class SprocketDao:

    def __init__(self, sql_engine):
        self.sql_engine = sql_engine

    def find(self, identifier: str):
        """
        Finds sprocket by ID
        :param identifier:
        :return:
        """
        with sessionmaker(bind=self.sql_engine)() as session:
            return session.query(Sprocket).filter(Sprocket.id == identifier).first()

    def list(self):
        """
        Lists all sprockets. No pagination or chunking
        :return:
        """
        with sessionmaker(bind=self.sql_engine)() as session:
            return session.query(Sprocket).all()

    def add(self, sprocket: Sprocket):
        """
        Persists sprocket in database
        :param sprocket:
        :return:
        """
        with sessionmaker(bind=self.sql_engine)() as session:
            session.add(sprocket)
            session.commit()
            session.refresh(sprocket)

    def update(self, identifier: str, fields: Dict):
        """
        Updates sprocket fields
        :param identifier:
        :param fields:
        :return:
        """
        with sessionmaker(bind=self.sql_engine)() as session:
            session.query(Sprocket).filter(Sprocket.id == identifier).update(fields)
            session.commit()
