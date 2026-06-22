from app.database.db import engine
from app.database.base import Base

from app.models.document import Document

Base.metadata.create_all(bind=engine)

print("Tables created successfully")