from pydantic import BaseModel
from typing import List

class SymptomInput(BaseModel):
    symptoms: str

class SymptomResponse(BaseModel):
    conditions: List[str]
    next_steps: List[str]
    disclaimer: str
