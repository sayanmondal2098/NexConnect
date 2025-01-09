# DB session creation, engine, etc.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from NexConnect.src.config.settings import DB_URL

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
