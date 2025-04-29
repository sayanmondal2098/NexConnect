from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base
from src.models.user import User

class GitHubToken(Base):
    __tablename__ = "github_tokens"

    # ID for the GitHub token record
    id = Column(Integer, primary_key=True, index=True)
    
    # The user associated with this GitHub token
    user_id = Column(Integer, ForeignKey("users.id"))

    # GitHub OAuth data
    access_token = Column(String, nullable=False)
    refresh_token = Column(String, nullable=True)  # Store refresh token if required
    token_type = Column(String, nullable=False)
    scope = Column(String, nullable=False)

    # Relationship with the user model
    user = relationship("User", back_populates="github_token")
