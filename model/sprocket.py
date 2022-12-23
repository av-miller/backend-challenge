import uuid

from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID

from model import Base


class Sprocket(Base):
    __tablename__ = 'sprocket'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    teeth = Column(Integer())
    pitch_diameter = Column(Integer())
    outside_diameter = Column(Integer())
    pitch = Column(Integer())
