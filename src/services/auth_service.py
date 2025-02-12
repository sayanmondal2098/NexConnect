from sqlalchemy.orm import Session
from passlib.context import CryptContext
from src.models.user import User
from src.schemas.user_schema import UserCreate, UserLogin
from uuid import uuid4


# to do - Implement Radis server to get data quickly from cache and reduce the load on the database

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(db: Session, user_data: UserCreate):
    user_id = str(uuid4())
    new_user = User(
        id=user_id, 
        username=user_data.username, 
        email=user_data.email, 
        hashed_password=get_password_hash(user_data.password) if user_data.password else None,
        social_login_provider=user_data.social_login_provider,
        social_login_id=user_data.social_login_id,
        role=user_data.role,
        active=user_data.active
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, user_data: UserLogin):
    user = db.query(User).filter(User.email == user_data.email).first()
    if not isinstance(user, User):
        print(f"Expected User object, got {type(user)}")
        return None
    print(user.email)
    if not user:
        return None
    if user_data.password and not pwd_context.verify(user_data.password, user.hashed_password):
        return None
    if user_data.social_login_provider and user_data.social_login_id != user.social_login_id:
        return None
    return user

    def authenticate_user_binary(db: Session, user_data: UserLogin) -> bool:
        user = authenticate_user(db, user_data)
        return user is not None

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: str):  
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: str, user_data: UserCreate):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    if user_data.username:
        user.username = user_data.username
    if user_data.email:
        user.email = user_data.email
    if user_data.password:
        user.hashed_password = get_password_hash(user_data.password)
    if user_data.social_login_provider:
        user.social_login_provider = user_data.social_login_provider
    if user_data.social_login_id:
        user.social_login_id = user_data.social_login_id
    if user_data.role:
        user.role = user_data.role
    if user_data.active:
        user.active = user_data.active
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: str):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user

def log_out_user(db: Session, user_id: UserLogin):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    user.active = 0
    db.commit()
    db.refresh(user)
    return user

