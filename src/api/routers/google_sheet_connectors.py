from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.services.google_sheet_service import download_google_sheet


google_sheet_router = APIRouter()

@google_sheet_router.get("/download")
def download_google_sheet_data(sheet_url: str):
    download_google_sheet(sheet_url)
    return {"message": "Downloaded"}