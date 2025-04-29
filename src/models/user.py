from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.core.database import Base

class User(Base):
    __tablename__ = "users"

    # Use UUID for user id
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=True)  # For password-based login
    # social_login_provider = Column(String, nullable=True)  # E.g., GitHub, Google
    # social_login_id = Column(String, nullable=True)  # The unique ID from the social provider
    role = Column(String, default="viewer")  # Role can be 'admin', 'viewer', etc.
    active = Column(Integer, default=1)  # 1 means active, 0 means inactive

    # Relationship with GitHub tokens (one-to-one)
    github_token = relationship("GitHubToken", back_populates="user", uselist=False)
