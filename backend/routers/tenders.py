from fastapi import APIRouter

router = APIRouter()  # This line is important!

@router.get("/")
def get_tenders():
    return {"tenders": []}

@router.post("/")
def create_tender():
    return {"message": "Tender created"}