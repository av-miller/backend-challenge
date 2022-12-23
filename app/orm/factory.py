from sqlalchemy import Column, JSON, String

from app.orm import Base, uuid_gen


class Factory(Base):
    __tablename__ = 'factory'

    id = Column(String(), primary_key=True, default=uuid_gen)
    chart_data = Column(JSON(), nullable=True)
