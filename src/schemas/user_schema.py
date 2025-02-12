from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: Optional[str] = None
    social_login_provider: Optional[str] = None
    social_login_id: Optional[str] = None
    active: Optional[int] = 1

class UserLogin(BaseModel):
    email: str
    password: Optional[str] = None
    social_login_provider: Optional[str] = None
    social_login_id: Optional[str] = None
    active: Optional[int] = 1

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    social_login_provider: Optional[str] = None
    social_login_id: Optional[str] = None
    role: Optional[str] = None
    active: Optional[int] = 1


class UserLogOut(BaseModel):
    user_id: str
    social_login_provider: Optional[str] = None
    social_login_id: Optional[str] = None
    active: Optional[int] = 0

