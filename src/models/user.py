from sqlalchemy import Column, String, Integer
from src.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=True)
    social_login_provider = Column(String, nullable=True)
    social_login_id = Column(String, nullable=True)
    role = Column(String, default="viewer")
    active = Column(Integer, default=1)
    
