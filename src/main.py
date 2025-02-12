from fastapi import FastAPI
from src.core.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers.users import user_router as users


app = FastAPI(title="NexConnect")


# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Database
Base.metadata.create_all(bind=engine)



@app.get("/")
def root():
    return {"message": "Welcome to NexConnect!"}


app.include_router(users, prefix="/users", tags=["Users"])
