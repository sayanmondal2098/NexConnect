from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_connectors():
    return {"connectors": ["Salesforce", "Shopify", "Google Sheets"]}
