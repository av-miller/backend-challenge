import uuid

from sqlalchemy import Column, JSON
from sqlalchemy.dialects.postgresql import UUID

from model import Base


class Factory(Base):
    __tablename__ = 'factory'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chart_data = Column(JSON(), nullable=True)
