import os
import json
import google.generativeai as genai
from typing import Dict, Any
from ..models import SymptomResponse
from ..utils.safety import DISCLAIMER_TEXT

LLM_API_KEY = os.getenv("LLM_API_KEY")

# Configure Gemini
if LLM_API_KEY:
    genai.configure(api_key=LLM_API_KEY, transport='rest')

SYSTEM_PROMPT = """
You are a helpful medical assistant. 
Based on the provided symptoms, suggest possible conditions and next steps.
Strictly output JSON with keys: "conditions" (list of strings), "next_steps" (list of strings), "disclaimer" (string).
The disclaimer must be: "This is for educational purposes only. Consult a doctor for medical advice."
Do NOT provide a diagnosis. Do NOT provide treatment instructions.
Ensure the tone is calm, objective, and supportive.
"""

def mock_analyze_symptoms(text: str) -> Dict[str, Any]:
    """
    Mock response for when no API key is provided or for testing.
    """
    return {
        "conditions": [
            "Common Cold",
            "Seasonal Allergies",
            "Tension Headache"
        ],
        "next_steps": [
            "Rest and drink plenty of fluids.",
            "Monitor symptoms for changes.",
            "Consult a healthcare provider if symptoms persist or worsen."
        ],
        "disclaimer": DISCLAIMER_TEXT
    }

def call_llm_api(text: str) -> Dict[str, Any]:
    """
    Calls the Google Gemini API to analyze symptoms.
    """
    if not LLM_API_KEY:
        print("No LLM_API_KEY found. Using mock response.")
        return mock_analyze_symptoms(text)

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Combine system prompt and user input for Gemini
        full_prompt = f"{SYSTEM_PROMPT}\n\nSymptoms: {text}"
        
        # Force JSON response
        response = model.generate_content(
            full_prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        
        return json.loads(response.text)
    except Exception as e:
        print(f"Error calling LLM API: {e}")
        return mock_analyze_symptoms(text) # Fallback to mock on error

def analyze_symptoms_service(text: str) -> SymptomResponse:
    """
    Service function to orchestrate the analysis.
    """
    # 1. Basic validation is done in the route or pydantic, but we can add more here if needed.
    
    # 2. Call LLM (or mock)
    result = call_llm_api(text)
    
    # 3. Ensure disclaimer is present and correct (enforce safety)
    result["disclaimer"] = DISCLAIMER_TEXT
    
    return SymptomResponse(**result)
