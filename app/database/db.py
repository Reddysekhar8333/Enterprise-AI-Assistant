from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus # for encoding special characters in the password when constructing the database URL

load_dotenv()

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:"
    f"{quote_plus(os.getenv('DB_PASSWORD'))}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
