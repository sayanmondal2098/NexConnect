from fastapi import FastAPI
import os 
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from src.core.database import engine, Base

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.api.github import github_router as github




app = FastAPI(title="NexConnect")

load_dotenv()
# Load environment variables

# Retrieve GitHub App ID and Secret from environment variables
GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
print(f"GITHUB_CLIENT_ID: {GITHUB_CLIENT_ID}")
print(f"GITHUB_CLIENT_SECRET: {GITHUB_CLIENT_SECRET}")

# Ensure that the GitHub credentials are loaded correctly

# Create all tables (if they don't already exist)
Base.metadata.create_all(bind=engine)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# # Initialize Database
# Base.metadata.create_all(bind=engine)



@app.get("/")
def root():
    return {"message": "Welcome to NexConnect!"}


# app.include_router(users, prefix="/users", tags=["Users"])
# # app.include_router(google_sheet_connectors, prefix="/google-sheet", tags=["Google Sheet Connectors"])
app.include_router(github, prefix="/auth/github", tags=["GitHub"])
