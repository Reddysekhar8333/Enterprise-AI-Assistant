from app.database.db import engine
from app.database.base import Base

from app.models.chunk import Chunk

from app.models.document import Document

from app.models.vector_mapping import VectorMapping

Base.metadata.create_all(bind=engine)

print("Tables created successfully")