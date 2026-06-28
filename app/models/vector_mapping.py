from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from app.database.base import Base


class VectorMapping(Base):

    __tablename__ = "vector_mappings"

    id = Column(
        Integer,
        primary_key=True
    )

    chunk_id = Column(
        Integer,
        ForeignKey("chunks.id")
    )

    vector_position = Column(
        Integer
    )