from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_workflows():
    return {"workflows": []}