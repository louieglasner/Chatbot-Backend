from fastapi import APIRouter

router = APIRouter()

SYMPTOMS = ["headache", "fever", "cough", "nausea"]

@router.get("/symptoms")
async def get_symptoms():
    return SYMPTOMS
