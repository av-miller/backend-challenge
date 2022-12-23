from sqlalchemy import Column, Integer, String

from app.orm import Base, uuid_gen


class Sprocket(Base):
    __tablename__ = 'sprocket'

    id = Column(String(), primary_key=True, default=uuid_gen)
    teeth = Column(Integer())
    pitch_diameter = Column(Integer())
    outside_diameter = Column(Integer())
    pitch = Column(Integer())
