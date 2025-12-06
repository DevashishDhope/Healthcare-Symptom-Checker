from fastapi import APIRouter, HTTPException
from ..models import SymptomInput, SymptomResponse
from ..services.llm_service import analyze_symptoms_service
from ..utils.safety import validate_symptom_input

router = APIRouter()

@router.post("/analyze", response_model=SymptomResponse)
async def analyze_symptoms(input_data: SymptomInput):
    if not validate_symptom_input(input_data.symptoms):
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a description of your symptoms.")
    
    try:
        response = analyze_symptoms_service(input_data.symptoms)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
