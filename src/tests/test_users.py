from fastapi.testclient import TestClient
from src.core.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.database import Base

from src.main import app  # Assuming your FastAPI app is instantiated in src/main.py

SQLALCHEMY_DATABASE_URL = "sqlite:///./NexConnect.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={"email": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_login_user():
    client.post("/register", json={"email": "test@example.com", "password": "testpassword"})
    response = client.post("/login", json={"email": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"

def test_get_user():
    client.post("/register", json={"email": "test@example.com", "password": "testpassword"})
    response = client.post("/login", json={"email": "test@example.com", "password": "testpassword"})
    user_id = response.json()["user_id"]
    response = client.get(f"/user/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_update_user():
    client.post("/register", json={"email": "test@example.com", "password": "testpassword"})
    response = client.post("/login", json={"email": "test@example.com", "password": "testpassword"})
    user_id = response.json()["user_id"]
    response = client.put(f"/user/{user_id}", json={"email": "updated@example.com", "password": "newpassword"})
    assert response.status_code == 200
    assert response.json()["email"] == "updated@example.com"

def test_get_user_by_email():
    client.post("/register", json={"email": "test@example.com", "password": "testpassword"})
    response = client.get("/user", params={"email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_logout_user():
    client.post("/register", json={"email": "test@example.com", "password": "testpassword"})
    response = client.post("/login", json={"email": "test@example.com", "password": "testpassword"})
    user_id = response.json()["user_id"]
    response = client.post(f"/user/{user_id}/logout")
    assert response.status_code == 200
    assert response.json()["message"] == "Logout successful"
