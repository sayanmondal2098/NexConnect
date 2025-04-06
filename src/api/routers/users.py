from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.user_schema import UserCreate, UserLogin
from src.services.auth_service import create_user, authenticate_user, get_user_by_email, get_user_by_id, update_user, log_out_user

user_router = APIRouter()

@user_router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@user_router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    authenticated_user = authenticate_user(db, user)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": authenticated_user.id}

@user_router.get("/user/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.put("/user/{user_id}")
def update_user_data(user_id: str, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@user_router.get("/user")
def get_user_by_email_address(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.post("/user/{user_id}/logout")
def logout_user(user_id: str, db: Session = Depends(get_db)):
    success = log_out_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found or already logged out")
    return {"message": "Logout successful"}


@user_router.get("/user/example")
def example_test():
    return {"message": "Example"}
