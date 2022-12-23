from sqlalchemy.orm import sessionmaker

from app.orm.factory import Factory


class FactoryDao:

    def __init__(self, sql_engine):
        self.sql_engine = sql_engine

    def find(self, identifier: str):
        """
        Finds factory by ID
        :param identifier:
        :return:
        """
        with sessionmaker(bind=self.sql_engine)() as session:
            return session.query(Factory).filter(Factory.id == identifier).first()

    def list(self):
        """
        Lists all factories. No pagination or chunking
        :return:
        """
        with sessionmaker(bind=self.sql_engine)() as session:
            return session.query(Factory).all()
